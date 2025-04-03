# Open Charity backend


## Create and Activate Virtual Environement

  1. python3 -m venv .
  2. source bin/activate

## Install dependencies

  1. cat requirements.txt | xargs -n 1 pip install

## Update dependencies

  1. pip freeze > requirements.txt


## Run django server

  1. python manage.py runserver <port-number (optional)>

## Deactivate Virtual Environment

  1. deactivate
