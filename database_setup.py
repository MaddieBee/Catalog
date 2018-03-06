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
    email = Column(String(250), nullable=False)
    website = Column(String(250), nullable=False)
    picture = Column(String(400))


class Luthier(Base):
    __tablename__ = 'luthiers'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Cello(Base):
    __tablename__ = 'cellos'

    model = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(10))
    year = Column(String(10))
    country = Column(String(80))
    classification = Column(String(80))
    luthier_id = Column(Integer, ForeignKey('luthiers.id'))
    luthier = relationship(Luthier)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
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



