# Spinning Up On Local System

- [Optional] Install virtual environment: On your terminal, run `python -m venv env`
- [Optional] Activate installed virtual environment: On your terminal, run `source/env/Scripts/activate`
- On your terminal, run `pip install fastapi` to Install FsstAPI
- On your terminal, run `pip install uvicorn` to install uvicorn server
- On your terminal, run `pip install sqlalchemy` to install sqlalchemy orm
- On your terminal, run `pip install pydantic` to install pydantic

* Please refer to requirements.txt for a full list of all the dependencies and packages used to carry out this project

# API endpoints

These endpoints to interact with in utilizing this app.

## create device status

**POST**

- For creating device status parameters
  [http://localhost:8000/{deviceId}/status]

**_Parameters_**

|         Field |   Required   |   Type   | Description            |
| ------------: | :----------: | :------: | ---------------------- |
|    `deviceId` |   required   |  string  | device Id              |
|    `pressure` | not required | integer  | device pressure        |
|   `timestamp` |   required   | datetime | (ISO 8601) date format |
|      `status` |   required   |  string  | devcie status          |
| `temperature` | not required | integer  | device temperature     |

\*status can only have one of the following values [ON, OFF, ACTIVE, INACTIVE]

## status histogram

**GET**

- For obtaining the histogram of status for a given device
  [http://localhost:8000/statuses/histogram/{deviceId}]

**_Parameters_**
`content-type: application/json`

|      Field | Required |  Type  | Description |
| ---------: | :------: | :----: | ----------- |
| `deviceId` | required | string | device Id   |

## Documentation

`Swagger UI` [/docs/](#schema/swagger-ui/)
`redoc` [/redoc/](#schema/redoc/)

# Simulator Dashboard

- The simulator was created using Locust which is a tool used for performance and load testing of app endpoints

## Running Simulator

- On your terminal, run `pip install locust` to install locust for load testing
- On your terminal, run `locust -f simulator.py`
- Follow the URL link [http://0.0.0.0:8089/] displayed from the command above. Note: If the given URL Link does not load the Locust's Web UI, please use [http://localhost:8089/] instead.
- From the interactive Web UI, select number of users to simulate, select spawn rate and select Host Url. Host URL is the URL that runs your project [http://localhost:8000/]
- CLick `Start Streaming` to start test
