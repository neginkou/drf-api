# Lab-Class 31-32-33

## Project:  Snacks API

Django Rest Framework, Docker Container, Postgresql and JWT Authentication

## Author: Negin Koushkakinejad

### Links and Resources

To create a virtual environment - python -m venv .venv

Activate the virtual environment - source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

Install Gunicorn - pip install gunicorn

static files with Gunicorn - install Whitenoise

Docker Setup:

docker-compose build

docker-compose up -d

To start the server by building and running the Docker container - docker-compose build
docker-compose up

To stop the running container - docker-compose down

docker-compose exec web python manage.py migrate

## How to Initialize/Run Your Application

Navigate to url/api/v1/snacks/ to navigate to API


How to Run Tests:

python manage.py test