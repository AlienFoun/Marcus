import os
import sys


sys.path.insert(0, 'the path to the project, where manage.py')
sys.path.insert(1, 'the path to the framework, where settings.py')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Marcus.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
