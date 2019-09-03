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


@site.route('/states_list')
def page_showStates():
    """List all the stored states"""

    states = models.storage.all('State').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
