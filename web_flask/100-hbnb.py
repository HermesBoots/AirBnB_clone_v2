#!/usr/bin/python3
"""Complete the HBNB layout with an HTML template and a database"""


import flask
import models


site = flask.Flask(__name__)
site.url_map.strict_slashes = False


@site.teardown_appcontext
def reloadStorageAfterRequest(error):
    """Close and reopen storage between requests"""

    models.storage.close()


@site.route('/hbnb')
def page_home():
    """Show the complete home page with locations, amenities, and places"""

    states = models.storage.all('State').values()
    states = sorted(states, key=lambda s: s.name)
    cities = {
        state.id: sorted(state.cities, key=lambda c: c.name)
        for state in states
    }
    amenities = models.storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda a: a.name)
    places = models.storage.all('Place').values()
    places = sorted(places, key=lambda p: p.name)
    ret = flask.Response()
    ret.headers['Content-Type'] = 'text/html; charset=latin1'
    ret.data = flask.render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    ).encode('latin1')
    return ret


site.run(host='0.0.0.0', port=5000)
