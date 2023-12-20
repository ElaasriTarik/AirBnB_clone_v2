#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from os import getenv
from models.review import Review

from sqlalchemy.orm import relationship
import shlex


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    @property
    def reviews(self):
        if getenv("HBNB_MYSQL_DB") == "db":
            reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
        else:
            """returns list of reviews"""
        reviews_obj = models.storage.all()
        res = []
        for obj in reviews_obj:
            obj = obj.replace('.', ' ')
            obj = shlex.split(obj)
            if obj[0] == 'City':
                if obj[0].place_id == self.id:
                    res.append(obj[0])
            return (res)
