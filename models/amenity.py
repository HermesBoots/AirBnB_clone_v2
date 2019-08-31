#!/usr/bin/python3
"""This is the amenity class"""


import models.base_model
import models.place
import sqlalchemy
import sqlalchemy.orm
import os


class Amenity(models.base_model.BaseModel, models.base_model.Base):
    """Amenity attributes"""

    __tablename__ = "amenities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = sqlalchemy.Column(
            sqlalchemy.String(128),
            nullable=False
        )
        place_amenities = sqlalchemy.orm.relationship(
            "Place",
            secondary='place_amenity',
            back_populates="amenities"
        )

    else:
        name = ""
