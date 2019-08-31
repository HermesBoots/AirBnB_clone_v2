#!/usr/bin/python3
"""Module for basic Flask server"""


import flask


site = flask.Flask(__name__)


@site.route('/', strict_slashes=False)
def index():
    """Display the site's index"""

    return 'Hello HBNB!\n'


@site.route('/hbnb', strict_slashes=False)
def hbnb():
    """A simple non-index page"""

    return 'HBNB\n'


site.run(host='0.0.0.0', port=5000)
