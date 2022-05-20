#!/usr/local/bin/python

from flup.server.fcgi import WSGIServer
import sys
sys.path.insert(0, 'env/lib/python3.10/site-packages')

from app import app

if __name__ == '__main__':
    WSGIServer(app).run()