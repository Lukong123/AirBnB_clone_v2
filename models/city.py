#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
import os


class City(BaseModel):

    """ connecting city to the database table"""
    __tablename__ = "cities"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable = False)
        state_id = Column(String(60), ForeingKey("states.id"), nullable = False)
        places = relationship("Place", passive_deletes = True, backref = "cities")
