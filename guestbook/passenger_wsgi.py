"""
WSGI config for guestbook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys


sys.path.insert(0, '/home/z/zelll/zelll.beget.tech/guestbook')
sys.path.insert(1, '/home/z/zelll/.local/lib/python3.7/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guestbook.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
