#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import shlex
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
    
    def cities(self):
        """returns list of cities"""
        cities_obj = models.storage.all()
        res = []
        for obj in cities_obj:
            obj = obj.replace('.', ' ')
            obj = shlex.split(obj)
            if obj[0] == 'City':
                if obj[0].state_id == self.id:
                    res.append(obj[0])
        return (res)
