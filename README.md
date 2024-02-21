# Lab-Class 31-32

## Project:  Snacks API

Django Rest Framework, Docker Container, Postgresql

## Author: Negin Koushkakinejad

### Links and Resources

To create a virtual environment - python -m venv .venv

Activate the virtual environment - source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

Docker Setup:

docker-compose build

docker-compose up -d

docker-compose exec web python manage.py migrate

## How to Initialize/Run Your Application

Navigate to url/api/v1/snacks/ to navigate to API


How to Run Tests:

python manage.py test