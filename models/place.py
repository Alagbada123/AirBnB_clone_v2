import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review


class Place(BaseModel, Base):
    """ The place class, contains various attributes """
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True, nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # if storage is db use relationship
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete',
                               oreign_keys='Review.place_id')
    else:
        # else use getter
        @property
        def reviews(self):
            from models import storage
            # empty list to store reviews
            review_list = []
            for review in storage.all(Review).values():
                # append review to list
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    def __init__(self, *args, **kwargs):
        """
        Initializes a place
        """
        super().__init__(*args, **kwargs)
