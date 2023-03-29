from locust import HttpUser, task, between
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv('APIKEY')
endPoint = os.getenv('ENDPOINT')

class QuickstartUser(HttpUser):
    wait_time = between(5,9)

    @task
    def index(self):
        print("executing my_task")
        self.client.get(
            url=endPoint, 
            headers={"API-Key":apiKey},
        )