#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = "states"


    name = Column(String(128), nullable = False)

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ cities by state"""
            cities_list = []
            for city_id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list

