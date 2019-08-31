#!/usr/bin/python3
"""Module for basemodel"""

import datetime
import models
import uuid
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


Base = sqlalchemy.ext.declarative.declarative_base()


class BaseModel:
    """Base class for data models
    Attributes:
        id (str): a random UUID string unique to each instance
        created_at (datetime.datetime): time stamp when instance was created
        updated_at (datetime.datetime): time stamp when instance was updated

    """

    id = sqlalchemy.Column(
        'id',
        sqlalchemy.String(60),
        nullable=False,
        primary_key=True
    )
    created_at = sqlalchemy.Column(
        'created_at',
        sqlalchemy.DateTime,
        nullable=False
    )
    updated_at = sqlalchemy.Column(
        'updated_at',
        sqlalchemy.DateTime,
        nullable=False
    )

    def __init__(self, *args, **kwargs):
        """Create new instance of BaseModel"""

        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' in kwargs:
            kwargs['created_at'] = datetime.datetime.strptime(
                kwargs['created_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
        else:
            self.created_at = datetime.datetime.utcnow()
        if 'updated_at' in kwargs:
            kwargs['updated_at'] = datetime.datetime.strptime(
                kwargs['updated_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
        else:
            self.updated_at = datetime.datetime.utcnow()
        for name, value in kwargs.items():
            if name != '__class__':
                setattr(self, name, value)

    def __str__(self):
        """Return the instance's ID, class name, and attributes as a string"""

        return '[{}] ({}) {}'.format(
            type(self).__name__,
            self.id,
            str(self.__dict__)
        )

    def delete(self):
        """Remove this instance from storage"""

        models.storage.delete(self)

    def save(self):
        """Update the instance's update time"""

        self.updated_at = datetime.datetime.utcnow()
        if self not in models.storage:
            models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return this instance's attributes as a dict
        The returned dict also contains a key called "__class__" containing the
        instance's class name. datetime.datetime objects are converted to
        strings in ISO 8601 format.

        """

        ret = dict(self.__dict__)
        ret['__class__'] = type(self).__name__
        ret['created_at'] = ret['created_at'].isoformat()
        ret['updated_at'] = ret['updated_at'].isoformat()
        if '_sa_instance_state' in ret:
            del ret['_sa_instance_state']
        return ret
