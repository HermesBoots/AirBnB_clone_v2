#!/usr/bin/python3
"""Module for city model"""


import models
import models.base_model
import sqlalchemy
import sqlalchemy.orm
import os


class City(models.base_model.BaseModel, models.base_model.Base):
    """Stores a city and its relationships to other models"""

    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = sqlalchemy.Column(
            'name',
            sqlalchemy.String(128),
            nullable=False
        )
        state_id = sqlalchemy.Column(
            'state_id',
            sqlalchemy.String(60),
            sqlalchemy.ForeignKey('states.id'),
            nullable=False
        )
        places = sqlalchemy.orm.relationship('Place', back_populates='city')
        state = sqlalchemy.orm.relationship('State', back_populates='cities')
    else:
        state_id = ""
        name = ""

        @property
        def places(self):
            """Get the places for rent in this city"""

            ret = [
                state
                for state in models.storage.all('State').values()
                if state.id == self.state_id
            ]
            return ret

        @property
        def state(self):
            """Get the state this city is in"""

            return models.storage.get('State', self.state_id)
