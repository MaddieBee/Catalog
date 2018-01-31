from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Cello, Base, CatalogItem


engine = create_engine('sqlite:///cellocatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Inventory for David Tecchler 

luthier1 = Luthier(name="David Tecchler") 

session.add(luthier1)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier1)

session.add(celloItem7)
session.commit()




luthier2 = Luthier(name="Armando Altavilla")

session.add(luthier2)
session.commit()

celloItem1 = CelloItem(model="C1470", description="Finely crafted and varnished by hand.     ", price="   ", year="1926", country="Italy", 
			luthier=luthier2)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier2)

session.add(celloItem7)
session.commit()






luthier3 = Luthier(name="    ")

session.add(luthier3)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier3)

session.add(celloItem7)
session.commit()






luthier4 = Luthier(name="    ")

session.add(luthier4)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier4)

session.add(celloItem7)
session.commit()





luthier5 = Luthier(name="    ")

session.add(luthier5)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier5)

session.add(celloItem7)
session.commit()





luthier6 = Luthier(name="    ")

session.add(luthier6)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier6)

session.add(celloItem7)
session.commit()





luthier7 = Luthier(name="    ")

session.add(luthier7)
session.commit()

celloItem1 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="    ", description="   ", price="   ", year="  ", country="  ", 
			luthier=luthier7)

session.add(celloItem7)
session.commit()
