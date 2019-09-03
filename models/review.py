#!/usr/bin/python3
"""This is the review class"""


import models
import models.base_model
import sqlalchemy
import sqlalchemy.orm
import os


class Review(models.base_model.BaseModel, models.base_model.Base):
    """This is the class for Review"""

    __tablename__ = "reviews"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = sqlalchemy.Column(
            'text',
            sqlalchemy.String(1024),
            nullable=False
        )
        place_id = sqlalchemy.Column(
            'place_id',
            sqlalchemy.String(60),
            sqlalchemy.ForeignKey('places.id'),
            nullable=False
        )
        user_id = sqlalchemy.Column(
            sqlalchemy.String(60),
            sqlalchemy.ForeignKey('users.id'),
            nullable=False
        )
        place = sqlalchemy.orm.relationship("Place", back_populates="reviews")
        user = sqlalchemy.orm.relationship("User", back_populates="reviews")

    else:
        place_id = ""
        user_id = ""
        text = ""

        @property
        def place(self):
            """Get the place this review is for"""

            return models.storage.get('Place', self.place_id)

        @property
        def user(self):
            """Get the user who wrote this review"""

            return models.storage.get('User', self.user_id)
