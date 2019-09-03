#!/usr/bin/python3
"""A simple Flask server using our real HBNB data"""


from flask import Flask, render_template
import models


site = Flask(__name__)
site.url_map.strict_slashes = False


@site.teardown_appcontext
def closeStorageAfterRequest(error):
    """Close and reload the storage engine between requests"""

    models.storage.close()


@site.route('/states')
def page_showStates():
    """List all states"""

    states = sorted(models.storage.all('State').values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states)


@site.route('/states/<string:id>')
def page_showStateAndCities(id):
    """List a state and its cities"""

    state = models.storage.tryGet('State', id, None)
    cities = None
    if state is not None:
        cities = sorted(state.cities, key=lambda c: c.name)
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
