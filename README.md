# Project:  Snacks API

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

How to Run Tests:

python manage.py test