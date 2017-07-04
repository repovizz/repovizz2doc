# List of repovizz2 API calls
Here are the currently available repovizz2 API calls:
* **/api/v1.0/user** [`GET`](#getuser)
* **/api/v1.0/datapacks** [`POST`](#postdatapack)
* **/api/v1.0/datapacks/{id}** `GET` `POST`
* **/api/v1.0/datapacks/{id}/content** `GET`
* **/api/v1.0/datapacks/{id}/content/{id}** `POST` `GET`
<br><br><br><br>
<a name="getuser"></a>
### Get user information
----
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

<a name="postdatapack"></a>
### Upload new datapack
----
  Uploads a new datapack. This API call is used to upload only the JSON structure of the datapack, not the contents of files in the datapack. The JSON structure must adhere to the [datapack json schema](datapack_schema.json).

* **URL**
  `/api/v1.0/datapacks`
* **Method:**
  `POST`
  
*  **URL Params**
None

* **Data Params**
  ```
  {
    'name': my_username,
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
    url: "https://repovizz2.upf.edu/api/v1.0/datapacks",
    data: JSON.stringify({
      'name': datapack_name,
      'owner': owner_id,
      'structure': json_structure
    }),
    dataType: "json",
    beforeSend: function(xhr){
      xhr.setRequestHeader('Authorization', "Bearer " + token);
    },
    success : function(r) {
      console.log(r);
    }
  });
  ```
