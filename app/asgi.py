# ToDoKiosk - CTCL 2020-2023
# File: app/asgi.py
# Purpose: ASGI interface
# Created: October 31, 2023
# Modified: October 31, 2023

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
