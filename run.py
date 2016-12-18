#! /usr/bin/env python3

from vmailmanager import app
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    app.run(debug=True)
else:
    app.run(threaded=True)