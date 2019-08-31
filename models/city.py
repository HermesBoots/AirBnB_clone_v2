#!/usr/bin/python3
"""Module for city model"""


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
