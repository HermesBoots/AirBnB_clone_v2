#!/usr/bin/python3
"""This is the user class"""


import models.base_model
import sqlalchemy.orm
import sqlalchemy
import os


class User(models.base_model.BaseModel, models.base_model.Base):
    """This is the class for user"""

    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = sqlalchemy.Column(
            'email',
            sqlalchemy.String(128),
            nullable=False
        )
        password = sqlalchemy.Column(
            'password',
            sqlalchemy.String(128),
            nullable=False
        )
        first_name = sqlalchemy.Column(
            'first_name',
            sqlalchemy.String(128),
            nullable=True
        )
        last_name = sqlalchemy.Column(
            'last_name',
            sqlalchemy.String(128),
            nullable=True
        )
        places = sqlalchemy.orm.relationship("Place", back_populates="user")
        reviews = sqlalchemy.orm.relationship("Review", back_populates="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
