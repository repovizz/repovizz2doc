# List of repovizz2 API calls
Here are the currently available repovizz2 API calls:
* **/api/v1.0/user** [`GET`](#getuser)
* **/api/v1.0/datapacks** [`POST`](#postdatapack)
* **/api/v1.0/datapacks/{id}** [`GET`](#getdatapack) [`POST`](#repostdatapack)
* **/api/v1.0/datapacks/{id}/content** [`GET`](#getalldatapackcontent)
* **/api/v1.0/datapacks/{id}/content/{id}** [`GET`](#getdatapackcontent) [`POST`](#postdatapackcontent)
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
      xhr.setRequestHeader('Authorization', "Bearer " + token);
    },
    success : function(r) {
      console.log(r);
    }
  });
  ```
  
<a name="getdatapack"></a>
### Retrieve datapack
----
  Downloads an existing datapack (but not the files inside its data nodes).

* **URL**
  `/api/v1.0/datapacks`
* **Method:**
  `GET`
  
*  **URL Params**
  `datapack id` <br>
  The id of the datapack to be retrieved.

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br>
    **Content:** 
    ```
    {
      "id": "07a35daf-11d4-4935-bdc4-e21caebac7de",
      "name": "MYO_various",
      "owner": 2,
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
      url: "https://repovizz2.upf.edu/api/v1.0/datapacks/f4572fb6-0c2c-41c3-9eb8-4dbbcd98f72d",
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
<a name="repostdatapack"></a>
### Edit datapack
----
  Edits a datapack by replacing its structure.

* **URL**
  `/api/v1.0/datapacks/`
* **Method:**
  `POST`
  
*  **URL Params**
  `datapack id` <br>
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
    
   * **Code:** 422 UNPROCESSABLE ENTITY <br>
    **Content:** `{ error : ''The request was well-formed but was unable to be followed due to semantic errors.' }`

* **Sample Call:**

  ```javascript
  $.ajax({
    type: "POST",
    url:  "https://repovizz2.upf.edu/api/v1.0/datapacks/07a35daf-11d4-4935-bdc4-e21caebac7de",
    data: JSON.stringify({
      'structure': new_json_structure
    }),
    dataType: "json",
    beforeSend: function(xhr){
      xhr.setRequestHeader('Authorization', "Bearer " + token);
    },
    success: function(r){
      console.log(r);
    }
  });
  ```
