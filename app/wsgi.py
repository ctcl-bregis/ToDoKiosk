# ToDoKiosk - CTCL 2023
# File: app/wsgi.py
# Purpose: WSGI interface
# Created: October 31, 2023
# Modified: October 31, 2023

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()
