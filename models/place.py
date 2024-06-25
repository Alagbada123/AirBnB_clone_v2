#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    class Place(BaseModel, Base):
        """ A place to stay """

        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")

        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

else:
    class Place(BaseModel):
        """ A place to stay """

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """ Getter attribute amenities that returns the list of Amenity instances
            based on the attribute amenity_ids """
            from models import storage
            amenities_list = []
            for amenity_id in self.amenity_ids:
                key = "Amenity." + amenity_id
                amenity = storage.all()["Amenity"].get(key)
                if amenity:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

