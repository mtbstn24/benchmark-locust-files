from locust import HttpUser, task, between
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv('APIKEY')

class QuickstartUser(HttpUser):
    wait_time = between(5,9)

    @task
    def index(self):
        print("executing my_task")
        self.client.get(
            url="/json", 
            headers={"API-Key":apiKey},
        )