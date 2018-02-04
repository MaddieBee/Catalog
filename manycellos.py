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

celloItem1 = CelloItem(model="Emanuel Wilfer Gofriller", description="Responsive and resonant with a full-bodied and warm sound.", 
			price="$12,000.00", year="2017", country="Germany", 
			luthier=luthier1)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="Sheng Liu", description="Full Sound and warm tone.  Sound consistent among all registries.", 
			price="$3,700.00", year="2004", country="China", 
			luthier=luthier1)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="Sheng Liu 550", description="Full Sound and warm tone.  Sound consistent among all registries.", 
			price="$6,700.00", year="2002", country="China", 
			luthier=luthier1)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="Giani 370", description="Finely crafted and varnished by hand.",
			price="$14,560.00", year="1966", country="Italy", 
			luthier=luthier1)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="Del Grasso Strad", description="Amazing warm sound, fine rich resonance across all registries.",
			price="$64,600.00", year="1891", country="Italy", 
			luthier=luthier1)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="Thomas Smith", description="Hand crafted my master craftsman in London.  Warm, big sound.",
			price="$47,000.00", year="1750", country="England", 
			luthier=luthier1)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="Becker 440", description="Hand crafted and varnished.  Beautiful warm and rich sound.",
			price="$16,500.00", year="2003", country="Germany", 
			luthier=luthier1)

session.add(celloItem7)
session.commit()


# Inventory for Armando Altavilla

luthier2 = Luthier(name="Armando Altavilla")

session.add(luthier2)
session.commit()

celloItem1 = CelloItem(model="C1470", description="Finely crafted and varnished by hand.",
			price="$13,560.00", year="1926", country="Italy", 
			luthier=luthier2)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="Heinrich Gill", description="Bold and open, somewhere between bright and warm.",
			price="$8,375.00", year="1990", country="Germany", 
			luthier=luthier2)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="Guarneri", description="Warm sound, loud resonance.", 
			price="$8,400.00", year="2003", country="Italy", 
			luthier=luthier2)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="Janika Wilfer 420", description="Hand crafted, warm sound and even resonabce.",
			price="$8,250.00", year="1993", country="Germany", 
			luthier=luthier2)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="C970", description="Finely crafted and varnished by hand.",
			price="$12,360.00", year="1974", country="Italy", 
			luthier=luthier2)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="Emanuel Wilfer 920", description="Hand crafted, warm sound and even resonabce.",
			price="$7,250.00", year="1983", country="Germany", 
			luthier=luthier2)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="Emanuel Wilfer 540", description="Hand crafted, warm sound and even resonabce.",
			price="$8,250.000", year="1997", country="Germany", 
			luthier=luthier2)

session.add(celloItem7)
session.commit()




# Inventory for Madison Bold

luthier3 = Luthier(name="Madison Bold")

session.add(luthier3)
session.commit()

celloItem1 = CelloItem(model="Calin Wultur #7", description="European tonewoods.",
			price="$7,500.00", year="2017", country="Germany", 
			luthier=luthier3)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="Sheng Liu", description="Full Sound and warm tone. Sound consistent among all registries.", 
			price="$5,700.00", year="2006", country="China", 
			luthier=luthier3)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="Leonhardt 924", description="Extremely powerful sound! This is a cello you can dig into, but provides plenty of volume contrast.",
			price="$9,980.00", year="1984", country="Germany", 
			luthier=luthier3)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="Dimbath X5 Gofriller", description="Huge sound! This cello has a soaring upper end with a bold and robust lower register.",
			price="$13,000.00", year="2016", country="Germany", 
			luthier=luthier3)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="Guarneri 330", description="Warm sound, loud resonance.", 
			price="$28,400.00", year="1902", country="Italy", 
			luthier=luthier3)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="Sheng Liu Master", description="Full Sound and warm tone. Sound consistent among all registries.", 
			price="$15,700.00", year="1976", country="China", 
			luthier=luthier3)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="Szlachtowski Professional Grade", description="Very responsive and well-balanced, the tone and volume are nicely even across the strings.", 
			price="$16,000.00", year="1991", country="Poland", 
			luthier=luthier3)

session.add(celloItem7)
session.commit()






luthier4 = Luthier(name="Bernd Dimbath")

session.add(luthier4)
session.commit()

celloItem1 = CelloItem(model="L470", description="Finely crafted and varnished by hand.",
			price="$13,560.00", year="1947", country="Italy", 
			luthier=luthier4)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
			price="$14,375.00", year="1972", country="Germany", 
			luthier=luthier4)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="Guarneri X3", description="Warm sound, loud resonance.", 
			price="$11,500.00", year="2013", country="Italy", 
			luthier=luthier4)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
			price="$8,750.00", year="2003", country="Germany", 
			luthier=luthier4)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="M70", description="Finely crafted and varnished by hand.",
			price="$11,360.00", year="1994", country="Italy", 
			luthier=luthier4)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="Regarri 520", description="Hand crafted, warm sound and even resonabce.",
			price="$6,250.00", year="1998", country="Italy", 
			luthier=luthier4)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="Wilfer 330", description="Hand crafted, warm sound and even resonabce.",
			price="$16,250.00", year="1927", country="Germany", 
			luthier=luthier4)

session.add(celloItem7)
session.commit()





luthier5 = Luthier(name="Johann Eberle")

session.add(luthier5)
session.commit()

celloItem1 = CelloItem(model="Soloist 729", description="Finely crafted and varnished by hand.",
			price="$17,000.00", year="1934", country="Italy", 
			luthier=luthier5)

session.add(celloItem1)
session.commit()

celloItem2 = CelloItem(model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
			price="$14,375.00", year="1972", country="Germany", 
			luthier=luthier5)

session.add(celloItem2)
session.commit()

celloItem3 = CelloItem(model="Guarneri X3", description="Warm sound, loud resonance.", 
			price="$17,500.00", year="2013", country="Italy", 
			luthier=luthier5)

session.add(celloItem3)
session.commit()

celloItem4 = CelloItem(model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
			price="$8,750.00", year="2003", country="Germany", 
			luthier=luthier5)

session.add(celloItem4)
session.commit()

celloItem5 = CelloItem(model="Strad 330", description="Finely crafted and varnished by hand.",
			price="$28,560.00", year="1894", country="Italy", 
			luthier=luthier5)

session.add(celloItem5)
session.commit()

celloItem6 = CelloItem(model="Regarri 720", description="Hand crafted, warm sound and even resonabce.",
			price="$6,250.00", year="1998", country="Italy", 
			luthier=luthier5)

session.add(celloItem6)
session.commit()

celloItem7 = CelloItem(model="Wilfer 740", description="Hand crafted, warm sound and even resonabce.",
			price="$16,250.00", year="1927", country="Germany", 
			luthier=luthier5)

session.add(celloItem7)
session.commit()




print "Added Cellos!"