# Spinning Up On Local System

- Install python
- git clone https://github.com/CeeJayyy007/Canvass-AI-Project.git
- [Optional] Install virtual environment: On your terminal, run `python -m venv env`
- [Optional] Activate installed virtual environment: On your terminal, run `source/env/Scripts/activate`
- Install the project requirements: On your terminal, run `pip install -r requirements.txt`
- To run the API, on your terminal, run `uvicorn main:app`

\* Please refer to requirements.txt for a full list of all the dependencies and packages used to carry out this project \* Project uses sqlite database

# API endpoints

The endpoints to interact with in utilizing this app.

## create device status

**POST**

- For creating device status parameters
  [http://localhost:8000/devices/{deviceId}/status]

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
- From the interactive Web UI, select `Number of users (peak concurrency)` to simulate, select `Spawn rate (users started/second)`
  and select `Host` Url. Host URL is the URL that you run your project on [http://localhost:8000/]
- Click `Start Swarming` to start test

# Additional Information

## Limitations and Challenges

1. Inanbility to include tests with the project due to time constraints

## Final Words

Special appreciation to the team and everyone involved in this process for the privilege to learn and participate. It has really been an opportunity to learn and grow and I am sincerely grateful!
