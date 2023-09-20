#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(float, nullable=True)
    longitude = Column(float, nullable=True)
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan",
                           passive_deletes=True)

    def reviews(self):
        """Getter method for reviews."""
        from models import storage
        review_objs = storage.all("Review")
        return [review for review in review_objs.values()
                if review.place_id == self.id]
