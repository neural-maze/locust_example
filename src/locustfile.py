import json
import random

from locust import HttpUser, task, constant_pacing

def load_json_file(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data
    
COMMENTS = load_json_file("./example_comments.json")

class LoadTestAlbums(HttpUser):    
    wait_time = constant_pacing(1)
    
    @task
    def post_albums(self):
        comment = random.choice(COMMENTS)
        self.client.post("/predict-sentiment", json=comment)
