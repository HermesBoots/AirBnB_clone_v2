#!/usr/bin/python3
"""Complete the HBNB layout with an HTML template and a database"""


from flask import Flask, Response, render_template
import models


site = Flask(__name__)
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
    ret = Response()
    ret.headers['Content-Type'] = 'text/html; charset=latin1'
    ret.data = render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    ).encode('latin1')
    return ret


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
