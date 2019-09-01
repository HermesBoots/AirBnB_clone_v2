#!/usr/bin/python3
"""Module for Flask server with routes that take parameters"""


import flask


site = flask.Flask(__name__)
site.url_map.strict_slashes = False


@site.route('/')
def index():
    """Display the site's index"""

    return 'Hello HBNB!\n'


@site.route('/hbnb')
def hbnb():
    """A simple non-index page"""

    return 'HBNB\n'


@site.route('/c/<string:text>')
def c(text):
    """Display the content of a text parameter"""

    return 'C ' + text.replace('_', ' ') + '\n'


@site.route('/python')
@site.route('/python/<string:text>')
def python(text='is cool'):
    """Display the content of a text parameter and include a default value"""

    return 'Python ' + text.replace('_', ' ') + '\n'


@site.route('/n/<int:n>')
def n(n):
    """Determine whether a parameter is an integer"""

    return str(n) + ' is a number\n'


@site.route('/number_template/<int:n>')
def number_template(n):
    """Show a web template based on the route parameter"""

    return flask.render_template('5-number.html', n=n)


@site.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Show a web template with a conditional statement"""

    return flask.render_template('6-number_odd_or_even.html', n=n)


site.run(host='0.0.0.0', port=5000)
