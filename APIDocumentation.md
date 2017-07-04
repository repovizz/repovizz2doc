# List of repovizz2 API calls
Here are the currently available repovizz2 API calls:
* **/api/v1.0/user** [`GET`](#getuser)
* **/api/v1.0/datapacks** [`POST`](#postdatapack)
* **/api/v1.0/datapacks/{id}** [`GET`](#getdatapack) [`POST`](#repostdatapack)
* **/api/v1.0/datapacks/{id}/content** [`GET`](#getalldatapackcontent)
* **/api/v1.0/datapacks/{id}/content/{id}** [`GET`](#getdatapackcontent) [`POST`](#postdatapackcontent)
<br><br><br><br>
<a name="getuser"></a>
----
### Get user information
  Returns json data about the user making the request.

* **URL**
  `/api/v1.0/user`
* **Method:**
  `GET`
  
*  **URL Params**
None

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br>
  **Content:** 
    ```
    {
    	'folders': [...],
    	'username': my_username,
    	'id': my_id,
    	'datapacks': [...],
    	'_links': {
    		'self': '/api/v1.0/users/my_username',
    		'collection': '/api/v1.0/users'
    	},
    	'groups': [...],
    	'email': 'email@email.com'
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
   **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
        url: "https://repovizz2.upf.edu/api/v1.0/user",
        dataType: "json",
        type : "GET",
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Authorization', "Bearer " + access_token);
        },
        success : function(r) {
            console.log(r);
        }
    });
  ```
----
<a name="postdatapack"></a>
### Upload new datapack
  Uploads a new datapack. This API call is used to upload only the JSON structure of the datapack, not the contents of data nodes (i.e. files) inside the datapack structure. The JSON structure must adhere to the [datapack json schema](datapack_schema.json).

* **URL**
  `/api/v1.0/datapacks`
* **Method:**
  `POST`
  
*  **URL Params**
None

* **Data Params**
  ```
  {
    'name': datapack_name,
    'owner': my_id,
    'structure': json_structure
  }
  ```

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      "item": {
        "name": datapack_name,
        "owner": owner_id,
        "folder": folder_id,
        "id": datapack_id,
        "structure": {...}
        },
        "group_edit_permissions": []
      },
      "result": "OK"
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   
   * **Code:** 409 CONFLICT <br>
    **Content:** `{ error : 'Datapack my_datapack already exists with id (...)' }`
    
   * **Code:** 422 UNPROCESSABLE ENTITY <br>
    **Content:** `{ error : ''The request was well-formed but was unable to be followed due to semantic errors.' }`

* **Sample Call:**

  ```javascript
  $.ajax({
    url:  "https://repovizz2.upf.edu/api/v1.0/datapacks",
    type: "POST",
    data: JSON.stringify({
      'name': datapack_name,
      'owner': owner_id,
      'structure': json_structure
    }),
    dataType: "json",
    beforeSend: function(xhr){
      xhr.setRequestHeader('Authorization', "Bearer " + access_token);
    },
    success : function(r) {
      console.log(r);
    }
  });
  ```

----
<a name="getdatapack"></a>
### Retrieve datapack
  Downloads an existing datapack (but not the files inside its data nodes).

* **URL**
  `/api/v1.0/datapacks/datapack_id`
* **Method:**
  `GET`
  
*  **URL Params**
  `datapack_id` <br>
  The id of the datapack to be retrieved.

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      "id": datapack_id,
      "name": "MYO_various",
      "owner": owner_id,
      "structure": {...}
      "folder": folder_id,
      "group_edit_permissions": [...],
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   
   * **Code:** 403 FORBIDDEN <br>
    **Content:** `{ error : 'Method not allowed.' }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "https://repovizz2.upf.edu/api/v1.0/datapacks/" + datapack_id,
      dataType: "json",
      type : "GET",
      beforeSend: function (xhr) {
          xhr.setRequestHeader('Authorization', "Bearer " + access_token);
      },
      success : function(r) {
          console.log(r);
      }
    });
  ```

----
<a name="repostdatapack"></a>
### Edit datapack
  Edits a datapack by replacing its structure.

* **URL**
  `/api/v1.0/datapacks/datapack_id`
* **Method:**
  `POST`
  
*  **URL Params**
  `datapack_id` <br>
  The id of the datapack to be edited.

* **Data Params**
  ```
  {
    'structure': new_json_structure
  }
  ```

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      "result": "OK"
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   
   * **Code:** 403 FORBIDDEN <br>
    **Content:** `{ error : 'Method not allowed.' }`
    
   * **Code:** 422 UNPROCESSABLE ENTITY <br>
    **Content:** `{ error : ''The request was well-formed but was unable to be followed due to semantic errors.' }`

* **Sample Call:**

  ```javascript
  $.ajax({
    type: "POST",
    url:  "https://repovizz2.upf.edu/api/v1.0/datapacks/" + datapack_id,
    data: JSON.stringify({
      'structure': new_json_structure
    }),
    dataType: "json",
    beforeSend: function(xhr){
      xhr.setRequestHeader('Authorization', "Bearer " + access_token);
    },
    success: function(r){
      console.log(r);
    }
  });
  ```

----
<a name="getalldatapackcontent"></a>
### Retrieve all `data` nodes from a datapack

* **URL**
  `/api/v1.0/datapacks/datapack_id/content`
* **Method:**
  `GET`
  
*  **URL Params**
  `datapack_id` <br>
  The id of the datapack to be edited.

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      datanode_link_1: {
        "class": "data",
        "link": datanode_link_1,
        "mime": datanode_link_1_mimetype,
        "name": datanode_link_1_name,
        "text": datanode_link_1_text
      },
      ...,
      datanode_link_N: {
        "class": "data",
        "link": datanode_link_N,
        "mime": datanode_link_N_mimetype,
        "name": datanode_link_N_name,
        "text": datanode_link_N_text
      },
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   
   * **Code:** 403 FORBIDDEN <br>
    **Content:** `{ error : 'Method not allowed.' }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "https://repovizz2.upf.edu/api/v1.0/datapacks/" + datapack_id + "/content",
      dataType: "json",
      type : "GET",
      beforeSend: function (xhr) {
          xhr.setRequestHeader('Authorization', "Bearer " + access_token);
      },
      success : function(r) {
          console.log(r);
      }
    });
  ```
  
----
<a name="getdatapackcontent"></a>
### Retrieve file from datapack
  Downloads a file from a `data` node inside a datapack.

* **URL**
  `/api/v1.0/datapacks/datapack_id/content/datanode_link`
* **Method:**
  `GET`
  
*  **URL Params**
  `datapack_id` <br>
  The id of the datapack from which you wish to retrieve a file.
  <br><br>
  
  `datanode_link` <br>
  The `link` attribute of the data node whose file you wish to retrieve.

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    The requested file.
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   
   * **Code:** 403 FORBIDDEN <br>
    **Content:** `{ error : 'Method not allowed.' }`

* **Sample Call:**

    ```
    $.ajax({
      url : "https://repovizz2.upf.edu/datapack/" + datapack_id + "/content/" + datanode_link,
      type : 'GET',
      beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', "Bearer " + access_token);
      },
      success : function(r) {              
        console.log(r);
      }
    });
    ```
    
----
<a name="postdatapackcontent"></a>
### Upload file inside datapack
  Uploads a file into a `data` node inside a datapack. This API call also serves when you wish to replace a file.

* **URL**
  `/api/v1.0/datapacks/datapack_id/content/datanode_link`
* **Method:**
  `POST`
  
*  **URL Params**
  `datapack_id` <br>
  The id of the datapack whose file you wish to replace.
  <br><br>
  
  `datanode_link` <br>
  The `link` attribute of the data node whose file you wish to replace.

* **Data Params**
The file you wish to upload. Should be posted inside a form as `multipart/form-data`.

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      "result": "OK"
    }
    ```
 
* **Error Response:**

   * **Code:** 401 UNAUTHORIZED <br>
    **Content:** `{ error : "You are unauthorized to make this request." }`
   <br><br>
   * **Code:** 403 FORBIDDEN <br>
    **Content:** `{ error : 'Method not allowed.' }`

* **Sample Call:**

  ```javascript
  var formData = new FormData();
  var file = new Blob([file_to_be_uploaded], { type: file_mimetype });
  formData.append(datanode_link, file);
  
  $.ajax({
    url: "https://repovizz2.upf.edu/api/v1.0/datapacks/" + datapack_id + "/content/" + datanode_link,
    type: 'POST',
    data: formData, 
    cache: false,
    contentType: false,
    processData: false,
    beforeSend: function(xhr){
      xhr.setRequestHeader('Authorization', "Bearer " + token);
    },
    success: function(r){
      console.log(r)
    }
  });
  ```
