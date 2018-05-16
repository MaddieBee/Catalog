#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine

Base = declarative_base()

 
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())    
    '''role = '''
    


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)    
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())    


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    model = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(10))
    year = Column(String(10))
    country = Column(String(80))
    classification = Column(String(80))
    transaction = relationship(Transaction)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('users.id'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())    
     

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
            'time_created': self.time_created,
            'time_updated': self.time_updated,
            'transaction_id': self.transaction_id            
        }

engine = create_engine('sqlite:///cellocatalog.db')

Base.metadata.create_all(engine)



