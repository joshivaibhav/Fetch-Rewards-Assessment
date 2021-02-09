# Fetch Rewards Back-end Engineering Assessment

# Dependencies / Requirements
In order to run this project, you will need to install Python in your system, specifically Python3. Navigate to the Python website [here](https://www.python.org/downloads/) and follow the instructions to install Python3 as per your platform (Windows, MacOS, etc.)

Once you have Python installed, you will need the dependencies / requirements for this project. The requirements.txt file contains the libraries that you will need. Pip is a popular command that is used to install packages in Python. Open the terminal and run the command below

```
pip install -r requirements.txt
```
# Running this project

Once you have the requirements installed, navigate to the project folder and open up the terminal. Fire up the flask server by the below command:

```
python api_server.py
```
You should see output as below :-
```
*  Serving Flask app "api_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 414-182-867
 * Running on http://127.0.0.1:5000/

```

The server is up and running at http:\\127.0.0.1:5000/. Now its time to test the API and view the responses.

# REST API Specifications

The following table shows the different API endpoints and their specifications. 

| API endpoint   |Body Parameters                |Methods Allowed              |Body / Payload Type |End_point description|  
|----------------|-------------------------------|-----------------------------|--------------------|---------------------|
|/add_points|`'payer'`, `'points'`, `'transaction_timestamp'` |`POST`|`JSON`|Add payer points to user account|
|/deduct_points |`'points_to_deduct'`|`DELETE`|`JSON`|deduct points from the user account|
|/get_balance   |None|`GET`|No payload|retrieve the points balance in the user account|

# Testing the API

You can test the API by running the test_api_server script :-
```
python api_server.py
```
# Viewing the response
There are number of ways to view the response of the API endpoint. You can either use the terminal go for a convenient API client like Postman. Examples for both are provided below.

## 1) Using the 'curl' command
Curl is a very handy command to fire HTTP requests from the terminal.

### ---> Add points to user account (/add_points)

### Request

      Method = `POST`
      Parameters = `payer`, `points`, `transaction_timestamp` 
      Content-Type = `application/json`

### Command (Windows):
    curl -X POST -H "Content-Type: application/json" --data "{\"payer\": \"UNILIVER\", \"points\":\"200\", \"transaction_timestamp\": \"02/04 5PM\"}" http://127.0.0.1:5000/add_points
    
### Command (Linux, Mac):
    curl -i -H 'Accept: application/json''payer='DANNON'&'points'=300'&'transaction_timestamp'="10/31 10AM' http://localhost:5000/add_points/
    
### Response
    Successfully added points to the user's account
    
### Headers
    HTTP/1.0 200 OK
    Content-type: application/json
    Content-Length: 47
    Server: Werkzeug/1.0.1 Python/3.6.8
    Date: Sun, 07 Feb 2021 18:40:11 GM

### ---> Deduct points from user account (/deduct_points)

### Request

      Method = `DELETE`
      Parameters = `points_to_deduct`
      Content-Type = `application/json`

### Command (Windows):
    curl -X DELETE -H "Content-Type: application/json" --data "{\"points-to_deduct\": \"5000\"}" http://127.0.0.1:5000/deduct_points
    
### Command (Linux, Mac):
    curl -X DELETE -H "Content-Type: application/json" --data "{\"points-to_deduct\": \"5000\"}" http://127.0.0.1:5000/deduct_points
    
### Response

    [["DANNON",-100,"now"],["UNILEVER",-200,"now"],["MILLER COORS",-4700,"now"]]
    
### Headers
    HTTP/1.0 200 OK
    Content-type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.6.8
    Date: Sun, 07 Feb 2021 18:40:11 GM

### ---> Get points balance (/get_balance)

### Request
      Method = `GET`
      Content-Type = `application/json`

### Command (Windows):
    curl -H "Content-Type: application/json" http://127.0.0.1:5000/get_balance
    
### Command (Linux, Mac):
    curl -H "Content-Type: application/json" http://127.0.0.1:5000/get_balance
    
### Response
      {
         "DANNON":1000,
         "MILLER COORS":5300,
         "UNILEVER":0
       }
    
### Headers
    HTTP/1.0 200 OK
    Content-type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.6.8
    Date: Sun, 07 Feb 2021 18:40:11 GM
    
## 2) Using Postman API Client
 Postman is a popular API client that makes it easy for developers to create, share, test and document APIs. It can be used as a browser extension or as a native standalone app as per the platform. Install Postman from [here](https://www.postman.com/downloads/). 
 

### ---> Add points to user account (/add_points)

### Request Parameters and Response

      Method = `POST`
      Parameters = `payer`, `points`, `transaction_timestamp` 
      Content-Type = `application/json`
      
      The image below shows the postman configuration for the request. The response is also shown below in the same image
   ![/add_points](https://github.com/joshivaibhav/Fetch-Rewards-Assessment/blob/main/imgs/add_points_postman.JPG)

    
    
### ---> Deduct points from user account (/deduct_points)

### Request Parameters and Response

      Method = `DELETE`
      Parameters = `points_to_deduct`
      Content-Type = `application/json`
      
      The image below shows the postman configuration for the request. The response is also shown below in the same image
   ![/deduct_points](https://github.com/joshivaibhav/Fetch-Rewards-Assessment/blob/main/imgs/deduct_points_postman.JPG)
    

### ---> Get points balance (/get_balance)

### Request Parameteres and Response
      Method = `GET`
      Content-Type = `application/json`
      
      The image below shows the postman configuration for the request. The response is also shown below in the same image
   ![/get_balance](https://github.com/joshivaibhav/Fetch-Rewards-Assessment/blob/main/imgs/get_balance_postman.JPG)
    
    

# Useful Docs and References
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [Pip Installer for Python](https://pypi.org/project/pip/)
* [Postman Tutorial](https://learning.postman.com/docs/getting-started/introduction/)



