#!/usr/bin/python
#: optional path to your local python site-packages folder
import sys
from flup.server.fcgi import WSGIServer
sys.path.insert(0, 'venv/lib/python2.1.2/site-packages')

from app import app

if __name__ == '__main__':
    WSGIServer(app).run()
