#!/usr/bin/python3
"""This is the place class"""


import models
import models.base_model
import sqlalchemy
import sqlalchemy.orm
import os


place_amenity = sqlalchemy.Table(
    'place_amenity',
    models.base_model.Base.metadata,
    sqlalchemy.Column(
        'place_id',
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    sqlalchemy.Column(
        'amenity_id',
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)
"""association table for places and amenities"""


class Place(models.base_model.BaseModel, models.base_model.Base):
    """This is the class for Place"""

    __tablename__ = "places"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = sqlalchemy.Column(
            'city_id',
            sqlalchemy.String(60),
            sqlalchemy.ForeignKey('cities.id'),
            nullable=False
        )
        user_id = sqlalchemy.Column(
            'user_id',
            sqlalchemy.String(60),
            sqlalchemy.ForeignKey('users.id'),
            nullable=False
        )
        name = sqlalchemy.Column(
            'name',
            sqlalchemy.String(128),
            nullable=False
        )
        description = sqlalchemy.Column(
            'description',
            sqlalchemy.String(1024),
            nullable=True
        )
        number_rooms = sqlalchemy.Column(
            'number_rooms',
            sqlalchemy.Integer,
            nullable=False,
            default=0
        )
        number_bathrooms = sqlalchemy.Column(
            'number_bathrooms',
            sqlalchemy.Integer,
            nullable=False,
            default=0
        )
        max_guest = sqlalchemy.Column(
            'max_guest',
            sqlalchemy.Integer,
            nullable=False,
            default=0
        )
        price_by_night = sqlalchemy.Column(
            'price_by_night',
            sqlalchemy.Integer,
            nullable=False,
            default=0
        )
        latitude = sqlalchemy.Column(
            'latitude',
            sqlalchemy.Float,
            nullable=True
        )
        longitude = sqlalchemy.Column(
            'longitude',
            sqlalchemy.Float,
            nullable=True
        )
        reviews = sqlalchemy.orm.relationship("Review", back_populates="place")
        amenities = sqlalchemy.orm.relationship(
            "Amenity",
            secondary='place_amenity',
            back_populates="place_amenities",
            viewonly=False
        )
        city = sqlalchemy.orm.relationship("City", back_populates="places")
        user = sqlalchemy.orm.relationship("User", back_populates="places")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Get all associated reviews"""

            ret = [
                review
                for review in models.storage.all('Review')
                if review.place_id == self.id
            ]
            return ret

        @property
        def user(self):
            """Get the user owning this place"""

            return models.storage.get('User', self.user_id)

        @property
        def amenities(self):
            """Get all associated amenities"""

            ret = [
                amenity
                for amenity in models.storage.all('Amenity')
                if amenity.id in amenity_ids
            ]
            return ret

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        @property
        def city(self):
            """Get the city this place is in"""

            return models.storage.get('City', self.city_id)
