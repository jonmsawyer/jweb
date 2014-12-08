"""
WSGI config for jweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

#WSGIPythonPath /home/jonmsawyer/dev-www.jonmsawyer.com/jweb/jweb:/home/jonmsawyer/.virtualenv/jweb/lib/python2.7/site-packages

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/jonmsawyer/.virtualenvs/jweb/local/lib/python2.7/site-packages')

# Add the app's directory to PYTHONPATH
sys.path.append('/home/jonmsawyer/dev-www.jonmsawyer.com/jweb/jweb')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jweb.settings")

# Activate our virtual env
activate_env=os.path.expanduser('/home/jonmsawyer/.virtualenvs/jweb/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
