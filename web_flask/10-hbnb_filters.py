#!/usr/bin/python3
"""Render the filters section of the HBNB site using the database data"""


from flask import Flask, render_template
import models


site = Flask(__name__)
site.url_map.strict_slashes = False


@site.teardown_appcontext
def reloadAfterRequest(error):
    """Close and reopen the storage connection after each request"""

    models.storage.close()


@site.route('/hbnb_filters')
def page_hbnbFilters():
    """Show the filters section of the HBNB home page"""

    states = models.storage.all('State').values()
    states = sorted(states, key=lambda s: s.name)
    cities = {
        state.id: sorted(state.cities, key=lambda c: c.name)
        for state in states
    }
    amenities = models.storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda a: a.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        cities=cities,
        amenities=amenities
    )


if __name__ == '__main__':
    site.run(host='0.0.0.0', port=5000)
