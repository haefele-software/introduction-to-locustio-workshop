This workshop covers the basics of Locust.io

URL: https://locust.io/

The following is an excerpt from the docs @ https://docs.locust.io/en/stable/

What is Locust?
===============

Locust is an easy to use, scriptable and scalable performance testing tool.
You define the behaviour of your users in regular Python code, instead of using a clunky UI or domain specific language.
This makes Locust infinitely expandable and very developer friendly.

Installing Locust (Web-UI):
===========================

1. Install Python 3.6 or later: https://docs.python-guide.org/starting/installation/
2. Install Locust using pip.

`$ pip3 install locust`

3. Validate your installation and show the Locust version number:

`$ locust -V`

If everything worked, move on, otherwise consult the docs


Installing Locust (Docker)

1. Install the docker image to your machine

`docker pull locustio/locust`

Docker Run:
-----------

The docker image can be used like this (assuming that the locustfile.py exists in the current working directory):

`docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py`

Docker Compose:
---------------

`docker-compose up --scale worker=4`

 

 