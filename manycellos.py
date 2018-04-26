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
users = [
        User(name="Madison",
             lastname="Bold",
             email="maddiebold@gmail.com", 
             website="https://github.com/MaddieBee", 
             picture="https://avatars3.githubusercontent.com/u/29990310?s=400&u=3405c9ac763980b083e00bfdf21f8fc88178d479&v=4")
]

for user in users:
    session.add(user)
    session.commit()


# Inventory for David Tecchler 

luthiers = [
    Luthier(id="1",
            name="David",
            lastname="Tecchler"
            ),
     Luthier(id="2",
            name="Armando",
            lastname="Altavilla"
            ),
    Luthier(id="3",
            name="Madison",
            lastname="Bold"
            ),
    Luthier(id="4",
            name="Bernd",
            lastname="Dimbath"
            ),
    Luthier(id="5",
            name="Johann",
            lastname="Eberle"
            )        
        ]

for luthier in luthiers:
    session.add(luthier)
    session.commit()




cellos = [
        Cello(
            model="Emanuel Wilfer Gofriller", 
            description="Responsive and resonant with a full-bodied and warm sound.", 
					price="$12,000.00", 
            year="2017", 
            country="Germany", 
            classification="Advanced", 
            luthier_id=1),

        Cello(
            model="Sheng Liu", 
            description="Full Sound and warm tone.  Sound consistent among all registries.", 
					price="$3,700.00", 
            year="2004",
            country="China",
            classification="Master",
            luthier_id=1),

        Cello(
            model="Sheng Liu 550",
            description="Full Sound and warm tone.  Sound consistent among all registries.", 
					price="$6,700.00",
            year="2002",
            country="China",
            classification="Beginner",
            luthier_id=1),

        Cello(
            model="Giani 370",
            description="Finely crafted and varnished by hand.", 
					price="$14,560.00",
            year="1966",
            country="Italy",
            classification="Student",
            luthier_id=1),
        
        Cello(
            model="Del Grasso Strad",
            description="Amazing warm sound, fine rich resonance across all registries.",
            price="$64,600.00",
            year="1891",
            country="Italy",
            classification="Advanced",
            luthier_id=1),

        Cello(
            model="Thomas Smith",
            description="Hand crafted my master craftsman in London.  Warm, big sound.",
            price="$47,000.00",
            year="1750", 
            country="England",
            classification="Master",
            luthier_id=1),


        Cello(
            model="Becker 440", 
            description="Hand crafted and varnished.  Beautiful warm and rich sound.",
            price="$16,500.00",
            year="2003",
            country="Germany",
            classification="Advanced",
            luthier_id=1),

        Cello(
            model="C1470", description="Finely crafted and varnished by hand.",	price="$13,560.00",
        						year="1926", country="Italy", luthier_id=2),
        
        
        Cello(
            model="Heinrich Gill", description="Bold and open, somewhere between bright and warm.",
        						price="$8,375.00", year="1990", country="Germany", classification="Beginner", luthier_id=2),
        
        
        Cello(
            model="Guarneri", description="Warm sound, loud resonance.", price="$8,400.00", year="2003",
        						country="Italy", classification="Advanced",luthier_id=2),
        
        Cello(
            model="Janika Wilfer 420", description="Hand crafted, warm sound and even resonabce.",
        						price="$8,250.00", year="1993", country="Germany", classification="Student", luthier_id=2),
        
        Cello(
            model="C970", description="Finely crafted and varnished by hand.", price="$12,360.00",
        						year="1974", country="Italy", classification="Beginner",luthier_id=2),
        
        
        Cello(
            model="Emanuel Wilfer 920", description="Hand crafted, warm sound and even resonabce.",
        						price="$7,250.00", year="1983", country="Germany", classification="Advanced", luthier_id=2),
        
        
        
        Cello(
            model="Emanuel Wilfer 540", description="Hand crafted, warm sound and even resonabce.",
        						price="$8,250.000", year="1997", country="Germany", classification="Master", luthier_id=2),


        Cello(
            model="Calin Wultur #7", 
            description="European tonewoods.", 
            price="$7,500.00", 
            year="2017",
            country="Germany", 
            classification="Student",
            luthier_id=3),

        Cello(
            model="Sheng Liu",
            description="Full Sound and warm tone. Sound consistent among all registries.", 
            price="$5,700.00",
            year="2006",
            country="China",
            classification="Advanced",	
            luthier_id=3),

        Cello(
            model="Leonhardt 924",
            description="Extremely powerful sound! This is a cello you can dig into, but provides plenty of volume contrast.",
            year="1984",
            country="Germany",
            classification="Advanced",      
            luthier_id=3),    
      
        Cello(
            model="Dimbath X5 Gofriller",
            description="Huge sound! This cello has a soaring upper end with a bold and robust lower register.",
            price="$13,000.00",
            year="2016",
            country="Germany",
            classification="Master",
            luthier_id=3),    

        Cello(
            model="Guarneri 330",
            description="Warm sound, loud resonance.",
            price="$28,400.00",
            year="1902",
            country="Italy",
            classification="Master",
            luthier_id=3),
            
        Cello(
            model="Sheng Liu Master",
            description="Full Sound and warm tone. Sound consistent among all registries.", 
            price="$15,700.00",
            year="1976",
            country="China",
            classification="Advanced",
            luthier_id=3),
                  
        Cello(
            model="Szlachtowski Professional Grade",
            description="Very responsive and well-balanced, the tone and volume are nicely even across the strings.", 
            price="$16,000.00",
            year="1991",
            country="Poland",
            classification="Advanced",
            luthier_id=3),          
            

        Cello(
            model="L470", description="Finely crafted and varnished by hand.", price="$13,560.00", year="1947",
        						country="Italy", classification="Advanced", luthier_id=4),
        
        
        Cello(
            model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
        						price="$14,375.00", year="1972", country="Germany", classification="Advanced", luthier_id=4),
        
        Cello(
            model="Guarneri X3", description="Warm sound, loud resonance.", price="$11,500.00", year="2013",
        						country="Italy", classification="Student", luthier_id=4),
        
        Cello(
            model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
        						price="$8,750.00", year="2003", country="Germany", classification="Student", luthier_id=4),
        
        
        
        Cello(
            model="M70", description="Finely crafted and varnished by hand.", price="$11,360.00", year="1994",
        						country="Italy", classification="Advanced", luthier_id=4),
        
        
        
        Cello(
                model="Regarri 520", description="Hand crafted, warm sound and even resonabce.",	price="$6,250.00",
        						year="1998", country="Italy", classification="Student", luthier_id=4),
        
        
        Cello(
            model="Wilfer 330", description="Hand crafted, warm sound and even resonabce.",
        						price="$16,250.00", year="1927", country="Germany", classification="Advanced", luthier_id=4),
        




        Cello(
            model="Soloist 729", description="Finely crafted and varnished by hand.",
        						price="$17,000.00", year="1934", country="Italy", classification="Advanced", luthier_id=5),
        
        Cello(
            model="Heinrich Gill 730", description="Bold and open, somewhere between bright and warm.",
        						price="$14,375.00", year="1972", country="Germany", classification="Advanced", luthier_id=5),
        
        Cello(
            model="Guarneri X3", description="Warm sound, loud resonance.", price="$17,500.00",
        						year="2013", country="Italy", classification="Master", luthier_id=5),
        
        
        Cello(
            model="Janika 220", description="Hand crafted, warm sound and even resonabce.",
        						price="$8,750.00", year="2003", country="Germany", classification="Student", luthier_id=5),
        
        
        Cello(
            model="Strad 330", description="Finely crafted and varnished by hand.", price="$28,560.00",
        						year="1894", country="Italy", classification="Master", luthier_id=5),
        
        
        Cello(
            model="Regarri 720", description="Hand crafted, warm sound and even resonabce.",
        						price="$6,250.00", year="1998", country="Italy", classification="Beginner", luthier_id=5),
        
        Cello(
            model="Wilfer 740", description="Hand crafted, warm sound and even resonabce.",
        						price="$16,250.00", year="1927", country="Germany", classification="Advanced", luthier_id=5),


]

for cello in cellos:
    session.add(cello)
    session.commit()


print ("Added Users, Luthiers, and Cellos Yo!!! ^_^ ")