# Fetch Rewards Back-end Engineering Assessment

# Dependencies / Requirements
In order to run this project, you will need to install Python in your system, specifically Python3. Navigate to the Python website [here](https://www.python.org/downloads/) and follow the instructions to install Python3 as per your platform (Windows, MacOS, etc.)

Once you have Python installed, you will need the dependencies / requirements for this project. The requirements.txt file contains the libraries that you will need. Pip is a popular command that is used to install packages in Python. Open the terminal and run the command below

```
pip install -r requirements.txt
```

# Install Requirements
```
bash
cd Fetch_Rewards
make package
```

# Assumptions
* add_points REST endpoint accept parameters as a json constisting of payerName, points and transactionDate

# Run the app
```
bash
cd Fetch_Rewards
make app
```

# Run the tests
```
bash
cd Fetch_Rewards
make test
```

# REST API

The REST API to the app is described below.

## Add points to the User account

### Request

`POST /add_points/`

    curl -i -H 'Accept: application/json''payerName='DANNON'&'points'=300'&'transactionDate'="10/31 10AM' http://localhost:5000/add_points/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json


## Deduct points from the User account

### Request

`DELETE /delete_points/`

    curl -i -H 'Accept: application/json''points_to_deduct'=5000 http://localhost:5000/delete_points/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    [["DANNON",-100,"now"],["UNILEVER",-200,"now"],["MILLER COORS",-4700,"now"]]

`GET /balance/`

    curl -i -H 'Accept: application/json' http://localhost:5000/delete_points/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"DANNON":1000,"MILLER COORS":5300,"UNILEVER":0}

# Useful Docs and References
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [Pip Installer for Python] (https://pypi.org/project/pip/)
* [Postman Docs] (https://learning.postman.com/docs/getting-started/introduction/)

