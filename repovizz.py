import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from requests_oauthlib import OAuth2Session
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep

SCRIPT_PORT = 50009

REPOVIZZ_URL = "http://repovizz2.upf.edu"
SCRIPT_URL = "http://localhost:{}".format(SCRIPT_PORT)


class RepoVizzClient(object):
    def __init__(self, client_id, client_secret, repovizz_url=REPOVIZZ_URL):
        self.client_id = client_id
        self.client_secret = client_secret
        self.repovizz_url = repovizz_url
        self.miniserver = None
        self.request_data = None
        self.oauthclient = None
        self.authenticated = True

    def start_auth(self, async=False):
        self.request_data = None
        # self.start_server(async)
        return self.get_auth_url()


    def start_server(self, async=True):
        if not async:
            self._mini_server_main()
        else:
            if not self.miniserver:
                self.miniserver = Thread(target=self._mini_server_main,args=(async,))
                self.miniserver.daemon = True
                self.miniserver.start()

    def _mini_server_main(self, async=True):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('127.0.0.1', SCRIPT_PORT))
        s.listen(1)
        response = 'HTTP/1.0 200 OK\nConnection: close\nContent-Length: 10\nContent-Type: text/html\n\nThank you.'
        while True:
            (conn, addr) = s.accept()
            self.request_data = conn.recv(1024)
            conn.send(response)
            conn.close()
            if not async:
                break
        s.close()

    def get_auth_url(self):
        authorization_base_url = self.repovizz_url + '/oauth/authorize'
        redirect_uri = SCRIPT_URL
        scope = ['basic']
        self.oauthclient = OAuth2Session(self.client_id, scope=scope, redirect_uri=redirect_uri)
        authorization_url, state = self.oauthclient.authorization_url(authorization_base_url)
        return authorization_url

    def finish_auth(self):
        while not self.request_data:
            sleep(0.1)
        url_auth_with_token = 'http://'+self.request_data.split()[4]+self.request_data.split()[1]
        token_url = self.repovizz_url + "/oauth/token"
        self.oauthclient.fetch_token(
            token_url,
            client_secret=self.client_secret,
            authorization_response=url_auth_with_token)
        self.authenticated = True

    def get(self, url, raw=False, *args, **kwargs):
        r = self.oauthclient.get(self.repovizz_url+url, *args, **kwargs)
        if raw:
            return r
        return r.json()

    def post(self, url, raw=False, *args, **kwargs):
        r = self.oauthclient.post(self.repovizz_url+url, *args, **kwargs)
        if raw:
            return r
        return r.json()