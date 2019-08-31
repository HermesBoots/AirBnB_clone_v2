#!/usr/bin/python3
"""Module for the Storage interface"""


import abc


class Storage (abc.ABC):
    """Storage base class enabling persistence of data models"""

    @abc.abstractmethod
    def __contains__(self, obj):
        """Test if the obj exists in storage"""
        pass

    @abc.abstractmethod
    def all(self, cls=None):
        """Get all stored objects"""
        pass

    @abc.abstractmethod
    def delete(self, cls, id=None):
        """Remove a stored data model object, but don't commit this yet"""
        pass

    @abc.abstractmethod
    def get(self, cls, id):
        """Get a data model object given its class or class name and its ID"""
        pass

    @abc.abstractmethod
    def new(self, obj):
        """Add a new data model object to storage, but don't save it yet"""
        pass

    @abc.abstractmethod
    def save(self):
        """Save all stored instances, committing all unsaved changes"""
        pass

    @abc.abstractmethod
    def tryGet(self, cls, id, default):
        """Try to get an object from storage, return default if not found"""
        pass
