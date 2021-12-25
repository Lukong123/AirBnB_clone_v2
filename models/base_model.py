#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class BaseModel:
    """ Classes will inherit from BaseModel to get common values(id, created_at, updated_at)"""
    id = Column(String(60), unique = True, nullable = False, primary_key = True)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow())
    updated_at = Column(DateTime, nullable = False, default = datetime.utnow())

    
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, 'id', str(uuid.uuid4()))
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    
    def save(self):
        """Updates updated_at with current time when instance is changed"""
        if not self.created_at:
            self.created_at = self.updated_at
        models.storage.new(self)
        models.storage.save()

        
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary


    def delete(self):
        """ deletes current instant for storage"""
        from models import storage
        storage.delete(self)
