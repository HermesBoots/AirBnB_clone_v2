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


@site.route('/states_list')
def page_showStates():
    """List all the stored states"""

    states = models.storage.all('State').values()
    return flask.render_template('7-states_list.html', states=states)


site.run(host='0.0.0.0', port=5000)
