# project

#### initial setup

project created on github with readme .gitignore for python and licence and cloned down

python -m venv env_project

pip freeze > requirements.txt

mkdir django_project

mkdir static_code_analysis_reports

#### installs

python -m pip install --upgrade pip

https://pypi.org/project/safety/

pip install safety

safety check > static_code_analysis_reports/safety_output.txt

https://pypi.org/project/bandit

pip install bandit

bandit -r * > static_code_analysis_reports/bandit_output.txt

https://pypi.org/project/flake8/

pip install flake8

flake8 <filename> --exclude=env_project > static_code_analysis_reports/flake8_output.txt

https://pypi.org/project/pylint/

pip install pylint

pylint <filename> --ignore=env_prjoect > static_code_analysis_reports/pylint_output.txt

https://pypi.org/project/autopep8/

pip install autopep8

autopep8 --in-place --aggressive --aggressive <filename>

https://pypi.org/project/black/

pip install black

black {source_file_or_directory}

https://pypi.org/project/yapf/

pip install yapf

https://pypi.org/project/Django/

pip install django 

python -m django --version

https://pypi.org/project/python-dotenv/

pip install python-dotenv

https://pypi.org/project/coverage/

pip install coverage

coverage run --source='.' manage.py test

coverage report > ../static_code_analysis_reports/coverage_output.txt


https://pypi.org/project/selenium/

pip install selenium

https://pypi.org/project/webdriver-manager/

pip install webdriver-manager


https://pypi.org/project/django-crispy-forms/

pip install django-crispy-forms

https://pypi.org/project/django-allauth/

pip install django-allauth

#### creating project 

the . on the end stops creating an extra folder

cd django_project

django-admin startproject config .

cd config 

create .env

#### running django

run development server 

python manage.py runserver

#### create app

python manage.py startapp <app name>


#### authentication

authentication views

https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views


custom user model recommended

https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project


#### database 

python manage.py makemigrations

python manage.py makemigrations <app name>

python manage.py migrate


#### django create super user

python manage.py createsuperuser


#### tests

python manage.py test

python manage.py test <app name>

python manage.py test <app name>.tests.<test name>

python manage.py test functional_tests.<test name>


#### static 

to collect static content for production 

python manage.py collectstatic

### docker commands

create Dockerfile

then 

docker build .

create docker-compose.yml

then 

docker-compose up

stopped with control+c

or run in detach mode

docker-compose up -d

stopped with docker-compose down

then to issue django commands on docker container

container must be running 

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python -m pip install --upgrade pip

then for install to take affect

docker-compose down

docker-compose up -d --build

#### check docker logs

docker-compose logs

#### docker database POSTgres

docker-compose exec web python /code/django_project/manage.py makemigrations

docker-compose exec web python /code/django_project/manage.py migrate

docker-compose exec web python /code/django_project/manage.py createsuperuser

docker-compose exec web python /code/django_project/manage.py test

docker-compose exec web rm -r /code/django_project/skills/migrations

docker volume ls

docker volume rm project_postgres_data

#### static files docker

docker-compose exec web python /code/django_project/manage.py collectstatic

#### creating app and projects on docker

docker-compose exec web python /code/django_project/manage.py startapp 

#### 

-f flag to use a different alt compose file

docker-compose -f docker-compose-prod.yml up -d --build


docker exec project env

#### acccess docker files

docker exec -t -i mycontainer /bin/bash

docker exec -tiu postgres project_db_1 psql

\l for databases

\dt tables


#### horoku

heroku create

set environment variables 

heroku stack:set container -a intense-plains-14836

heroku addons:create heroku-postgresql:hobby-dev -a intense-plains-14836

heroku git:remote -a intense-plains-14836

git push heroku main

heroku run python /code/django_project/manage.py migrate

heroku run python /code/django_project/manage.py createsuperuser