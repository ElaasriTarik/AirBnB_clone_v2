#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import shlex

place_amenity = Table("place_amenity", Base.metadata, 
                        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
                        )


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


    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)
    else:
        @property
        def reviews(self):
            reviews_obj = models.storage.all()
            res = []
            for obj in reviews_obj:
                obj = obj.replace('.', ' ')
                obj = shlex.split(obj)
                if obj[0] == 'City':
                    if obj[0].place_id == self.id:
                        res.append(obj[0])
                return (res)

    @property
    def amenities(self):
        """ Returns amenity_ids """
        return self.amenity_ids
    
    @amenities.setter
    def amenities(self, obj=None):
        """ appends an amenity to amenity_ids """
        if obj is not None and type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
