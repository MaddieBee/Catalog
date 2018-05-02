#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

 
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    website = Column(String(250), nullable=False)
    picture = Column(String(400))
    role = 


Class Transaction(Base)
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    model = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(10))
    year = Column(String(10))
    country = Column(String(80))
    classification = Column(String(80))
    user = relationship(User)
    sold = Column(Integer, default=True)
     

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id': self.id,                
            'model': self.model,
            'description': self.description,
            'price': self.price,
            'year': self.year,
            'country': self.country,
            'classification': self.classification,
        }

engine = create_engine('sqlite:///cellocatalog.db')

Base.metadata.create_all(engine)



