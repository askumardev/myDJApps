# myDJApps
### First time setup
* python3 --version
* sudo apt install python3-pip
* pip --version
* python3 -m pip install Django==5.0.6
* sudo apt install python3-django
* django-admin --version
* mkdir myDJApps
* cd myDJApps/
* pipenv install django
* pip freeze
* django-admin startproject myProject
* cd myProject/
* python manage.py startapp myapp
* python manage.py runserver

### after project and app creation
#### cd code/myDJApps/myProject

* pipenv shell
* python manage.py runserver
