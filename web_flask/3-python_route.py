#!/usr/bin/python3
"""Module for Flask server with routes that take parameters"""


from flask import Flask


site = Flask(__name__)
site.url_map.strict_slashes = False


@site.route('/')
def index():
    """Display the site's index"""

    return 'Hello HBNB!'


@site.route('/hbnb')
def hbnb():
    """A simple non-index page"""

    return 'HBNB'


@site.route('/c/<string:text>')
def c(text):
    """Display the content of a text parameter"""

    return 'C ' + text.replace('_', ' ')


@site.route('/python')
@site.route('/python/<string:text>')
def python(text='is cool'):
    """Display the content of a text parameter and include a default value"""

    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
