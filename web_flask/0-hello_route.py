#!/usr/bin/python3
"""Module for very basic Flask server"""


import flask


site = flask.Flask(__name__)


@site.route('/', strict_slashes=False)
def index():
    """Display the site's index"""

    return 'Hello HBNB!\n'


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
