#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Luthier, Cello, User


engine = create_engine("sqlite:///cellocatalog.db", pool_pre_ping=True)
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

# Add Users To Database
user = User(name="Madison Mikhaela Bold", email="maddiebold@gmail.com", website="https://github.com/MaddieBee", picture="https://avatars3.githubusercontent.com/u/29990310?s=400&u=3405c9ac763980b083e00bfdf21f8fc88178d479&v=4")

session.add(user)
session.commit()


# Inventory for David Tecchler 
luthier1 = Luthier(name="David Tecchler") 

session.add(luthier1)
session.commit()


cello1 = Cello(model="Emanuel Wilfer Gofriller", description="Responsive and resonant with a full-bodied and warm sound.", 
						price="$12,000.00", year="2017", country="Germany", classification="Advanced", luthier=luthier1)

session.add(cello1)
session.commit()

cello2 = Cello(model="Sheng Liu", description="Full Sound and warm tone.  Sound consistent among all registries.", 
						price="$3,700.00", year="2004", country="China", classification="Master", luthier=luthier1)

session.add(cello2)
session.commit()

cello3 = Cello(model="Sheng Liu 550", description="Full Sound and warm tone.  Sound consistent among all registries.", 
						price="$6,700.00", year="2002", country="China", classification="Beginner", luthier=luthier1)

session.add(cello3)
session.commit()

cello4 = Cello(model="Giani 370", description="Finely crafted and varnished by hand.", price="$14,560.00", year="1966", 
						country="Italy", classification="Student", luthier=luthier1)

session.add(cello4)
session.commit()

cello5 = Cello(model="Del Grasso Strad", description="Amazing warm sound, fine rich resonance across all registries.",
						price="$64,600.00", year="1891", country="Italy", classification="Advanced", luthier=luthier1)

session.add(cello5)
session.commit()

cello6 = Cello(model="Thomas Smith", description="Hand crafted my master craftsman in London.  Warm, big sound.",
						price="$47,000.00", year="1750", country="England", classification="Master", luthier=luthier1)

session.add(cello6)
session.commit()

cello7 = Cello(model="Becker 440", description="Hand crafted and varnished.  Beautiful warm and rich sound.",
						price="$16,500.00", year="2003", country="Germany", classification="Advanced", luthier=luthier1)

session.add(cello7)
session.commit()


# Inventory for Armando Altavilla
luthier2 = Luthier(name="Armando Altavilla")

session.add(luthier2)
session.commit()

cello1 = Cello(model="C1470", description="Finely crafted and varnished by hand.",	price="$13,560.00",
						year="1926", country="Italy", luthier=luthier2)

session.add(cello1)
session.commit()

cello2 = Cello(model="Heinrich Gill", description="Bold and open, somewhere between bright and warm.",
						price="$8,375.00", year="1990", country="Germany", classification="Beginner", luthier=luthier2)

session.add(cello2)
session.commit()

cello3 = Cello(model="Guarneri", description="Warm sound, loud resonance.", price="$8,400.00", year="2003",
						country="Italy", classification="Advanced", luthier=luthier2)

session.add(cello3)
session.commit()

cello4 = Cello(model="Janika Wilfer 420", description="Hand crafted, warm sound and even resonabce.",
						price="$8,250.00", year="1993", country="Germany", classification="Student", luthier=luthier2)

session.add(cello4)
session.commit()

cello5 = Cello(model="C970", description="Finely crafted and varnished by hand.", price="$12,360.00",
						year="1974", country="Italy", classification="Beginner", luthier=luthier2)

session.add(cello5)
session.commit()

cello6 = Cello(model="Emanuel Wilfer 920", description="Hand crafted, warm sound and even resonabce.",
						price="$7,250.00", year="1983", country="Germany", classification="Advanced", luthier=luthier2)

session.add(cello6)
session.commit()

cello7 = Cello(model="Emanuel Wilfer 540", description="Hand crafted, warm sound and even resonabce.",
						price="$8,250.000", year="1997", country="Germany", classification="Master", luthier=luthier2)

session.add(cello7)
session.commit()


# Inventory for Madison Bold
luthier3 = Luthier(name="Madison Bold")

session.add(luthier3)
session.commit()

cello1 = Cello(model="Calin Wultur #7", description="European tonewoods.", price="$7,500.00", year="2017",
						country="Germany", classification="Student", luthier=luthier3)

session.add(cello1)
session.commit()

cello2 = Cello(model="Sheng Liu", description="Full Sound and warm tone. Sound consistent among all registries.", 
						price="$5,700.00", year="2006", country="China", classification="Advanced",	luthier=luthier3)

session.add(cello2)
session.commit()

cello3 = Cello(model="Leonhardt 924", description="Extremely powerful sound! This is a cello you can dig into, but provides plenty of volume contrast.",
						price="$9,980.00", year="1984", country="Germany", classification="Advanced", luthier=luthier3)

session.add(cello3)
session.commit()

cello4 = Cello(model="Dimbath X5 Gofriller", description="Huge sound! This cello has a soaring upper end with a bold and robust lower register.",
						price="$13,000.00", year="2016", country="Germany", classification="Master", luthier=luthier3)

session.add(cello4)
session.commit()

cello5 = Cello(model="Guarneri 330", description="Warm sound, loud resonance.", price="$28,400.00", year="1902",
						country="Italy", classification="Master", luthier=luthier3)

session.add(cello5)
session.commit()

cello6 = Cello(model="Sheng Liu Master", description="Full Sound and warm tone. Sound consistent among all registries.", 
						price="$15,700.00", year="1976", country="China", classification="Advanced", luthier=luthier3)

session.add(cello6)
session.commit()

cello7 = Cello(model="Szlachtowski Professional Grade", description="Very responsive and well-balanced, the tone and volume are nicely even across the strings.", 
						price="$16,000.00", year="1991", country="Poland", classification="Advanced", luthier=luthier3)

session.add(cello7)
session.commit()


# Inventory for Bernd Dimbath
luthier4 = Luthier(name="Bernd Dimbath")

session.add(luthier4)
session.commit()

cello1 = Cello(model="L470", description="Finely crafted and varnished by hand.", price="$13,560.00", year="1947",
						country="Italy", classification="Advanced", luthier=luthier4)

session.add(cello1)
session.commit()

cello2 = Cello(model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
						price="$14,375.00", year="1972", country="Germany", classification="Advanced", luthier=luthier4)

session.add(cello2)
session.commit()

cello3 = Cello(model="Guarneri X3", description="Warm sound, loud resonance.", price="$11,500.00", year="2013",
						country="Italy", classification="Student", luthier=luthier4)

session.add(cello3)
session.commit()

cello4 = Cello(model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
						price="$8,750.00", year="2003", country="Germany", classification="Student", luthier=luthier4)

session.add(cello4)
session.commit()

cello5 = Cello(model="M70", description="Finely crafted and varnished by hand.", price="$11,360.00", year="1994",
						country="Italy", classification="Advanced",	luthier=luthier4)

session.add(cello5)
session.commit()

cello6 = Cello(model="Regarri 520", description="Hand crafted, warm sound and even resonabce.",	price="$6,250.00",
						year="1998", country="Italy", classification="Student", luthier=luthier4)

session.add(cello6)
session.commit()

cello7 = Cello(model="Wilfer 330", description="Hand crafted, warm sound and even resonabce.",
						price="$16,250.00", year="1927", country="Germany", classification="Advanced", luthier=luthier4)

session.add(cello7)
session.commit()


# Inventory for Johann Eberle
luthier5 = Luthier(name="Johann Eberle")

session.add(luthier5)
session.commit()

cello1 = Cello(model="Soloist 729", description="Finely crafted and varnished by hand.",
						price="$17,000.00", year="1934", country="Italy", classification="Advanced", luthier=luthier5)

session.add(cello1)
session.commit()

cello2 = Cello(model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
						price="$14,375.00", year="1972", country="Germany", classification="Advanced", luthier=luthier5)

session.add(cello2)
session.commit()

cello3 = Cello(model="Guarneri X3", description="Warm sound, loud resonance.", price="$17,500.00",
						year="2013", country="Italy", classification="Master", luthier=luthier5)

session.add(cello3)
session.commit()

cello4 = Cello(model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
						price="$8,750.00", year="2003", country="Germany", classification="Student", luthier=luthier5)

session.add(cello4)
session.commit()

cello5 = Cello(model="Strad 330", description="Finely crafted and varnished by hand.", price="$28,560.00",
						year="1894", country="Italy", classification="Master", luthier=luthier5)

session.add(cello5)
session.commit()

cello6 = Cello(model="Regarri 720", description="Hand crafted, warm sound and even resonabce.",
						price="$6,250.00", year="1998", country="Italy", classification="Beginner", luthier=luthier5)

session.add(cello6)
session.commit()

cello7 = Cello(model="Wilfer 740", description="Hand crafted, warm sound and even resonabce.",
						price="$16,250.00", year="1927", country="Germany", classification="Advanced", luthier=luthier5)

session.add(cello7)
session.commit()


print ("Added Cellos!")