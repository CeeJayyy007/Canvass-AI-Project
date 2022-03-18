from json import dumps
from locust import HttpUser, task, between
import random
import json

# randomly generated data for device input parameters
status = ["ON", "OFF", "ACTIVE", "INACTIVE"]

# simulator APpUser class
class AppUser(HttpUser):
    
    # interval between requests
    wait_time = between(2, 5)

    # Endpoint

    @task
    def create_device_status(self):
        self.client.post(f"/devices/sensor_{random.randint(1,10)}/status",  data=json.dumps({'status': random.choice(status),
                         'pressure': random.randint(100,1000), 'temperature': random.randint(100,300)}))
