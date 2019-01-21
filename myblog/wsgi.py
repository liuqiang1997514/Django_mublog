"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from os.path import join,dirname,abspath 


from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
os.environ.['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

application = get_wsgi_application()



PROJECT_DIR = dirname(dirname(abspath(__file__)))   
sys.path.insert(0,PROJECT_DIR)
