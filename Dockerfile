FROM python:3.6

# create root directory for our project in the container
RUN mkdir /YoutubeFetch

# Set the working directory to /YoutubeFetch
WORKDIR /YoutubeFetch

# Copy the current directory contents into the container at /YoutubeFetch
ADD . /YoutubeFetch/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt