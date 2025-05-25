# Dockerfile name has to be Dockerfile   

# Python in Docker Hub has a lot of tags. These are different images, each one is for a diff. need.
# Simple Tags
# 3.14.0b1-bookworm, In this container, Python 3.14.0b1 is installed on Debian Bookworm OS.
# 3.14-rc-bookworm⁠

# 3.14.0b1-slim-bookworm, 3.14-rc-slim-bookworm, 3.14.0b1-slim, 3.14-rc-slim⁠

# 3.14.0b1-bullseye, 3.14-rc-bullseye⁠

# 3.14.0b1-slim-bullseye, 3.14-rc-slim-bullseye⁠

# 3.14.0b1-alpine3.21, 3.14-rc-alpine3.21, 3.14.0b1-alpine, 3.14-rc-alpine⁠

# 3.14.0b1-alpine3.20, 3.14-rc-alpine3.20⁠

# 3.14.0b1-windowsservercore-ltsc2025, 3.14-rc-windowsservercore-ltsc2025⁠, this is for Windows(Server) OS

# to install the base image (OS), we need to use the FROM command
FROM python:3.10-slim
# in this case, we get python 3.10 installed on light weight Alpine Linux OS.

# in the container's root directory, we need to create a folder for our app.
WORKDIR /flask-loan-app
# WORKDIR is used to set the working directory (folder) inside the container.
# this will create a directory called flask-loan-app in the container.
# rn, our container is like a mini OS in which only pyhton is installed. 

# we need to install the dependencies (flask, flask-cors, etc.) in the container(to the root folder).
COPY artefacts/requirements.txt .
# This copies the requirements.txt file from the artefacts folder in the host machine to the current working directory in the container.
# the . at the end means the current working directory in the container.
# we only need this file only once, to install the dependencies, later it's useless.

RUN pip install -r requirements.txt

# This command upgrades pip to the latest version.
# pip is the package manager for Python, and it is used to install and manage Python packages.
# This command installs the Python packages listed in the requirements.txt file.
# RUN is used to run a command in the container.
# This is done in a single layer, so the image size is small.

COPY . /flask-loan-app/
# This copies the entire current directory on our host machine to the /flask-loan-app directory in the container.
# Copies all the files and folders of session_4 (of current dir) to the flask loan app folder in the container.



CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]
# this order  must be followed, otherwise it won't work.
# This command runs the Flask application using the Python interpreter.
# CMD is used to specify the command to run when the container starts.
# host is localhost, port is 8000, which is a window of our container from which our container can talk to the outside world, and we need to expose this port so that our conatiner ("python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0") can talk to this port.
# --host=0.0.0 means that the app will be accessible from any IP address.

# RUN works only when we create an image, but CMD works whenever we create a container from the image, when the container is started.

# in terminal, we can run the following command to build the image:
# >docker build -t mark .
# -t is used to tag the image with a name, in this case, mark.
# . means the current directory, which contains the Dockerfile. 
# this will create an image called mark in the local docker registry.
# we can check the image by running the following command:  
# >docker images
# this will show all the images(commands) in the local docker registry/container.
# to run the image, we can use the following command:
# >docker run -p 8000:8000 mark
# -p is used to publish the container's port to the host machine's port.
# 8000:8000 means that the host(local) machine's port 8000 is mapped to the container's port 8000.
# Now we get the following message:
# * Running on all addresses (  
# * Running on http://127.0.0.1:8000
# * Running on http://172.17.0.2:8000
# Now it's running on our local machine, and we can paste any of the address in the POSTMAN and test it. Here, we're talking(IP address) with our container.
# we're running the container from the image we have created.
# Docker Desktop is not used in production in comapnies. We use terminal to run the commands.
#docker run -p 8000:8000 --name flask-loan-app-container mark1
# --name is used to give a name to the container, in this case, flask-loan-app-container.
# this will create a container called flask-loan-app-container from the image mark1.

#docker run -d -p 8000:8000 mark1
# -d is used to run the container in detached mode, which means that the container will run in the background.
# this is used when we want to run the container in the background and not see the logs in the terminal.

#docker container run -it -p 8000:8000 mark2 bash
# -it is used to run the container in interactive mode, which means that we can interact with the container's terminal.
# bash is used to run the bash shell in the container.  

#docker container ls --all
# this will show all the container ID's in the local docker registry, we can use that ID to run the container or stop the container.


#creating repositories in docker hub
#in github, we upload the code, in dockerhun we upload the image
#docker login
#docker image tag mark2:latest shivam13juna/example2-docker:latest
# this will tag the image mark2(current/local container) with the name shivam13juna/example2-docker:latest, shivam13juna is the name of the account, example2-docker is the repo name, and latest is the tag name.
#docker push shivam13juna/example2-docker:latest 
# once we push the image to the docker hub, we can use it in any other machine.
#docker pull shivam13juna/example2-docker:latest
#we can now use this image in any other machine, and we can run the same commands as we did before, this is why docker is used - it's like a plug and play(no installation required in other machine), its portable.

#We have to rebuild the image every time we make a change in the code, and then we have to run the image again.
# this is a lot of work, so we can use docker-compose to do this for us.

#When we build the image (reusing few layers), it will take less time to build the image, as it'll use cached layers. 
#if something changes frequently, we can put that in the last layer, so that the other layers will be cached and won't be rebuilt every time. 

#In Reality, companies release swarms, which is a docker container.
#If a container goes down, another container will take its place, and the user won't even know that the container has gone down.
#how to manahe this swarm is where Kubernetes comes in.
#Kubernetes is a container orchestration tool, which means that it manages the containers for us. This is done by DevOps.

#Dcoker Captain Udemy Course to learn more about Docker.

