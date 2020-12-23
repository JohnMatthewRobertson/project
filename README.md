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

#### creating project 

the . on the end stops creating an extra folder

cd django_project

django-admin startproject config .

cd config 

create .env

#### running djanog

run development server 

python manage.py runserver
