from json import dumps
from locust import HttpUser, task, between
import random
import json

status = ["ON", "OFF", "ACTIVE", "INACTIVE"]
pressure = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
temperature = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280]


# 
class AppUser(HttpUser):
    
    # interval between requests
    wait_time = between(2, 5)

    # Endpoint

    @task
    def create_device_status(self):
        self.client.post(f"/devices/sensor_{random.randint(1,10)}/status",  data=json.dumps({'status': random.choice(status),
                         'pressure': random.choice(pressure), 'temperature': random.choice(temperature)}))
