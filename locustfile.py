import json

from locust import HttpUser, task

def load_json_file(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data
    
ARTISTS = load_json_file("./example_artists.json")

class LoadTestAlbums(HttpUser):
    @task
    def post_albums(self):
        for artist in ARTISTS:
            self.client.post("/albums", json=artist)
    