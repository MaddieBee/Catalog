import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Luthier(Base):
    __tablename__ = 'luthier'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class CelloItem(Base):
    __tablename__ = 'cello_item'

    model = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(10))
    year = Column(String(10))
    country = Column(String(80))
    classification = Column(String(80))
    luthier_id = Column(Integer, ForeignKey('luthier.id'))
    luthier = relationship(Luthier)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'model': self.model,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'year': self.year,
            'country': self.country,
            'classification': self.classification,
        }

engine = create_engine('sqlite:///cellocatalog.db')

Base.metadata.create_all(engine)

''' class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String)
'''

