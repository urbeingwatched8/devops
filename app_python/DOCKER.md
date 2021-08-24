My Dockerfile is pretty simple, but I avoided putting credentials or personal info there. 

Docker setup:
1.curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
2. sudo apt-get install docker-ce docker-ce-cli containerd.io

I added Dockerfile and docker-compose.yml according to documentation with a few differences due to using a different DB (https://docs.docker.com/samples/django/#create-a-django-project)

An important step is running 'sudo docker-compose run web django-admin startproject composeexample .'
And adding a few changes to the file settings.py and urls.py - allowed hosts and installed apps

To run Docker rootless this was helpful - https://docs.docker.com/engine/security/rootless/

Docker image uploaded to https://hub.docker.com/layers/urbeingwatched8/devopslab1/newestapp/images/sha256-51d966d8f716818f9c9403c0cf6ee7a28fa71a50a6762deba1f83aa15c2ba40d?context=repo