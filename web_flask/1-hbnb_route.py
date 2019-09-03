#!/usr/bin/python3
"""Module for basic Flask server"""


from flask import Flask


site = Flask(__name__)


@site.route('/', strict_slashes=False)
def index():
    """Display the site's index"""

    return 'Hello HBNB!'


@site.route('/hbnb', strict_slashes=False)
def hbnb():
    """A simple non-index page"""

    return 'HBNB'


site.run(host='0.0.0.0', port=5000)
