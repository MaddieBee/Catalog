import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String)

class Luthier(Base):
	__tablename__ = 'luthier'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class CelloItem(Base):
	__tablename__ = 'cello_item'

	model = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	price = Column(String(10))
	year = Column(String(10))
	country = Column(String(80))
	luthier_id = Column(Integer, ForeignKey('luthier.id'))
	luthier = relationship(luthier)




engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.create_all(engine)