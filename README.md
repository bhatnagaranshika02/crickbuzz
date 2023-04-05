# crickbuzz
Assignment for crickbuzz interview round2.

## Steps for Installation
Have python3 installed in your system

- Navigate to cricbuzz root folder `cd cricbuzz`
- Create virtual environment `python -m venv venv`
- Install required packages `pip install -r requirements.txt`
- Run Migrations `python manage.py migrate`
- Run Fixture for Site Data `python manage.py loaddata fixtures/records.json`
- Run Fixture for Subscription Data `python manage.py loaddata fixtures/subscriptions.json`

## Run application

`python manage.py runserver`