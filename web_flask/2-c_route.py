#!/usr/bin/python3
"""Module for Flask server with several simple routes"""


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


@site.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """Display the content of a text parameter"""

    return 'C ' + text.replace('_', ' ') + '\n'


site.run(host='0.0.0.0', port=5000)
