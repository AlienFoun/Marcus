# -*- coding: utf-8 -*-
import os
import sys
import platform

sys.path.insert(0, 'the path to the project, where manage.py')

sys.path.insert(0, 'the path to the framework, where settings.py')

sys.path.insert(0, 'path to env virtual environment'.format(platform.python_version()[0:3]))

os.environ["DJANGO_SETTINGS_MODULE"] = "Marcus.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
