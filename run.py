#! /usr/bin/env python3

from vmailmanager.main import app
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    app.run(debug=True)
else:
    app.run(threaded=True, port=5001)
