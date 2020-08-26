# Youtube Fetch Video Api
An API to fetch latest videos from youtube sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

The server fetches latest videos async after every 2 minutes and saves it to the db.

## Technologies Used
Python 
Django
Django Rest Framework

## Method Used to fetch Data

Used Celery [Docs](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) to fetch videos after every 2 minutes using [Youtube Data Api](https://developers.google.com/youtube/v3/docs/search/list) and save it to the db

## Setup Guide
- Clone the project
- Go the project through the terminal and install all dependencies by using typing `pip install -r requirements.txt` in the terminal
- Run the server using `python mange.py runserver`
- Follow the steps below to configure and start celery to fetch data

## Celery Configuration
- Open the terminal and navigate to the project directory
- Start celery worker using `celery -A YoutubeFetch worker -l info`
- Start celery beat using `celery -A YoutubeFetch beat -l info`

## Building the Project with Docker
- Navigate to the project directory in terminal
- Run `docker-compose up`
- Access the project at http://localhost:8000