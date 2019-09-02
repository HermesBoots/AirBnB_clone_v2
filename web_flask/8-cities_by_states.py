#!/usr/bin/python3
"""A simple Flask server using our real HBNB data"""


import flask
import models


site = flask.Flask('HBNB', template_folder='web_flask/templates')
site.url_map.strict_slashes = False


@site.teardown_appcontext
def closeStorageAfterRequest(error):
    """Close and reload the storage engine between requests"""

    models.storage.close()


@site.route('/cities_by_states')
def page_showStatesAndCities():
    """List all the stored states and the cities within them"""

    states = models.storage.all('State').values()
    return flask.render_template('8-cities_by_states.html', states=states)


site.run(host='0.0.0.0', port=5000)
