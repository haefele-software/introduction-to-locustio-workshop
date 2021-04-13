from locust import HttpUser, TaskSet, task
import json

class Storage(object):
    def __init__(self):
        self.token = ""

storage = Storage()

class UserBehavior(TaskSet):

    @task
    def log_in(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        post_data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
        with self.client.post('/login', post_data, catch_response=True) as response:
          if  response.json()["token"] == "":
            response.failure(response.json())
          else:
            storage.token = response.json()["token"]
           
    @task
    def create_user(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip', 'Authorization': 'Bearer ' + storage.token}
        self.client.post("/users",data= json.dumps({
      "name": "morpheus",
      "job": "leader"
    }), 
    headers=headers, 
    name = "Create a new user")

    # @task
    # def update_created_post(self):
    #     headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
    #     self.client.put("/posts/1",data= json.dumps({
    #   "title": "foo2",
    #   "body": "bar2",
    #   "userId": 1
    # }), 
    # headers=headers, 
    # name = "Update a created post")

    # @task
    # def get_post(self):
    #     headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
    #     self.client.get("/posts", 
    # headers=headers, 
    # name = "Get posts")

    @task
    def stop(self):
        self.interrupt()
 
 
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    
   
