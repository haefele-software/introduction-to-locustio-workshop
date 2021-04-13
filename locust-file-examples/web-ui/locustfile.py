#A locust file is just a normal Python module, it can import code from other files or packages.

import time
from locust import HttpUser, task, between

# Here we define a class for the users that we will be simulating. 
# It inherits from HttpUser which gives each user a client attribute, 
# which is an instance of HttpSession, that can be used to make HTTP 
# requests to the target system that we want to load test. When a test starts, 
# locust will create an instance of this class for every user that it simulates, 
# and each of these users will start running within their own green gevent thread.

class QuickstartUser(HttpUser):

    # Our class defines a wait_time that will make the simulated users wait 
    # between 1 and 2.5 seconds after each task is executed.

    wait_time = between(1, 2.5)

    # Methods decorated with @task are the core of your locust file. 
    # For every running user, Locust creates a greenlet (micro-thread), 
    # that will call those methods.   
    # 
    # When our QuickstartUser runs it’ll pick one of the declared tasks below and execute it at random.
    # Tasks can be weighted as below (@task(3)). In the case of "view_colour" locust is 3 times more likely 
    # to select that task to execute.
    #
    # Note that only methods decorated with @task will be picked, so you can define your own internal helper methods any way you like.

    @task
    def list_colours(self):

        # The self.client attribute makes it possible to make HTTP calls that will be logged by Locust. 
        # For information on how to make other kinds of requests, validate the response, etc, see the docs

        self.client.get("/colours", name="List colours")
    
    @task(3)
    def view_colour(self):

        # In this task we load 10 different URLs by using a variable query parameter. 
        # In order to not get 10 separate entries in Locust’s statistics - since the stats is grouped on the URL  

        for id in range(10):
            self.client.get(f"/colours/{id}")             

    # Additionally we’ve declared an on_start method. 
    # A method with this name will be called for each simulated user when they start. 

    def on_start(self):
        post_data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
        with self.client.post('/login', post_data, catch_response=True) as response:
          if  response.json()["token"] == "":
            response.failure(response.json())         