from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Cello, Base, CatalogItem


engine = create_engine('sqlite:///cellocatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = enginevagrant 