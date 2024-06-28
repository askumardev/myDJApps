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

### After project and app creation
#### cd code/myDJApps/myProject

* pipenv shell
* python manage.py runserver
* python3 manage.py makemigrations
* python3 manage.py migrate

### Super user
* python manage.py createsuperuser

### .ignore setup
* touch .gitignore
* echo '__pycache__/' >> .gitignore
* git add .gitignore
* git commit -m "Ignore __pycache__"

### ipython3
* cd code/myDJApps/myProject
* (myDJApps) $ export DJANGO_SETTINGS_MODULE=myProject.settings
* (myDJApps) $ ipython3

* In [1]: import os

* In [2]: import django

* In [3]: os.environ['DJANGO_SETTINGS_MODULE'] = 'myProject.settings'

* In [4]: django.setup()

* In [5]: from tourmate.models import Tour

* In [6]: to1 = Tour(origin="Japan", destination="India", number_of_nights=3, price=10000)

* In [7]: to1.origin
*Out[7]: 'Japan'