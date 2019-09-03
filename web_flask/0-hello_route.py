#!/usr/bin/python3
"""Module for very basic Flask server"""


import flask


app = flask.Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display the app's index"""

    return 'Hello HBNB!\n'


app.run(host='0.0.0.0', port=5000)
