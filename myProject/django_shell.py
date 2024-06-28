# django_shell.py
import os
import django
from IPython import embed

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
django.setup()

embed()