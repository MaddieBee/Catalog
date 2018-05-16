#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Item, User


engine = create_engine("sqlite:///cellocatalog.db")
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



users = [
    User(id="1",
        name="David Tecchler",
        email="davidtecchler@gmail.com"),

    User(id="2",
        name="Armando Altavilla",
        email="armandoaltavilla@gmail.com"), 
    
    User(id="3",
        name="Lukas Stahl",
        email="LukasStahl@gmail.com"), 
            
    User(id="4",
        name="Bernd Dimbath",
        email="BerndD@gmail.com"), 
    
    User(id="5",
        name="Johann Eberle",
        email="JohannEber@gmail.com")

]


for user in users:
    session.add(user)
    session.commit()



items = [
        Item(
            model="Emanuel Wilfer Gofriller", 
            description="Responsive and resonant with a full-bodied and warm sound.", 
			price="$12,000.00", 
            year="2017", 
            country="Germany", 
            classification="Advanced"), 

        Item(
            model="Sheng Liu", 
            description="Full Sound and warm tone.  Sound consistent among all registries.", 
			price="$3,700.00", 
            year="2004",
            country="China",
            classification="Master"),

        Item(
            model="Sheng Liu 550",
            description="Full Sound and warm tone.  Sound consistent among all registries.", 
			price="$6,700.00",
            year="2002",
            country="China",
            classification="Beginner"),

        Item(
            model="Giani 370",
            description="Finely crafted and varnished by hand.", 
			price="$14,560.00",
            year="1966",
            country="Italy",
            classification="Student"),
        
        Item(
            model="Del Grasso Strad",
            description="Amazing warm sound, fine rich resonance across all registries.",
            price="$64,600.00",
            year="1891",
            country="Italy",
            classification="Advanced"),

        Item(
            model="Thomas Smith",
            description="Hand crafted my master craftsman in London.  Warm, big sound.",
            price="$47,000.00",
            year="1750", 
            country="England",
            classification="Master"),


        Item(
            model="Becker 440", 
            description="Hand crafted and varnished.  Beautiful warm and rich sound.",
            price="$16,500.00",
            year="2003",
            country="Germany",
            classification="Advanced"),

        Item(
            model="C1470",
            description="Finely crafted and varnished by hand.",
            price="$13,560.00",
        	year="1926",
            country="Italy"),
        
        
        Item(
            model="Heinrich Gill",
            description="Bold and open, somewhere between bright and warm.",
        	price="$8,375.00",
            year="1990",
            country="Germany",
            classification="Beginner"),
        
        
        Item(
            model="Guarneri",
            description="Warm sound, loud resonance.", 
            price="$8,400.00", 
            year="2003",
        	country="Italy",
            classification="Advanced"),
        
        Item(
            model="Janika Wilfer 420",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$8,250.00",
            year="1993",
            country="Germany",
            classification="Student"),
        
        Item(
            model="C970",
            description="Finely crafted and varnished by hand.",
            price="$12,360.00",
        	year="1974",
            country="Italy",
            classification="Beginner"),
        
        
        Item(
            model="Emanuel Wilfer 920",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$7,250.00",
            year="1983",
            country="Germany",
            classification="Advanced"),
        
        
        
        Item(
            model="Emanuel Wilfer 540",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$8,250.000",
            year="1997",
            country="Germany",
            classification="Master"),


        Item(
            model="Calin Wultur #7", 
            description="European tonewoods.", 
            price="$7,500.00", 
            year="2017",
            country="Germany", 
            classification="Student"),

        Item(
            model="Sheng Liu",
            description="Full Sound and warm tone. Sound consistent among all registries.", 
            price="$5,700.00",
            year="2006",
            country="China",
            classification="Advanced"),	

        Item(
            model="Leonhardt 924",
            description="Extremely powerful sound! This is a cello you can dig into, but provides plenty of volume contrast.",
            year="1984",
            country="Germany",
            classification="Advanced"),      
      
        Item(
            model="Dimbath X5 Gofriller",
            description="Huge sound! This cello has a soaring upper end with a bold and robust lower register.",
            price="$13,000.00",
            year="2016",
            country="Germany",
            classification="Master"),

        Item(
            model="Guarneri 330",
            description="Warm sound, loud resonance.",
            price="$28,400.00",
            year="1902",
            country="Italy",
            classification="Master"),
            
        Item(
            model="Sheng Liu Master",
            description="Full Sound and warm tone. Sound consistent among all registries.", 
            price="$15,700.00",
            year="1976",
            country="China",
            classification="Advanced"),
                  
        Item(
            model="Szlachtowski Professional Grade",
            description="Very responsive and well-balanced, the tone and volume are nicely even across the strings.", 
            price="$16,000.00",
            year="1991",
            country="Poland",
            classification="Advanced"),
            
        Item(
            model="L470", 
            description="Finely crafted and varnished by hand.", 
            price="$13,560.00", 
            year="1947",
            country="Italy",
            classification="Advanced"),
        
        Item(
            model="Heinrich Gill 730",
            description="Bold and open, somewhere between bright and warm.",
        	price="$14,375.00", 
            year="1972", 
            country="Germany",
            classification="Advanced"),
        
        Item(
            model="Guarneri X3",
            description="Warm sound, loud resonance.",
            price="$11,500.00",
            year="2013",
        	country="Italy",
            classification="Student"),
        
        Item(
            model="Janika 220",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$8,750.00",
            year="2003",
            country="Germany",
            classification="Student"),
        
           
        Item(
            model="M70", 
            description="Finely crafted and varnished by hand.",
            price="$11,360.00",
            year="1994",
            country="Italy",
            classification="Advanced"),
        
           
        Item(
            model="Regarri 520", 
            description="Hand crafted, warm sound and even resonabce.",
            price="$6,250.00",
        	year="1998",
            country="Italy", 
            classification="Student"),
        
        
        Item(
            model="Wilfer 330", 
            description="Hand crafted, warm sound and even resonabce.",
        	price="$16,250.00",
            year="1927",
            country="Germany",
            classification="Advanced"),
        
        Item(
            model="Soloist 729",
            description="Finely crafted and varnished by hand.",
        	price="$17,000.00",
            year="1934",
            country="Italy",
            classification="Advanced"),
        
        Item(
            model="Heinrich Gill 730",
            description="Bold and open, somewhere between bright and warm.",
        	price="$14,375.00",
            year="1972", 
            country="Germany",
            classification="Advanced"),
        
        Item(
            model="Guarneri X3",
            description="Warm sound, loud resonance.",
            price="$17,500.00",
        	year="2013",
            country="Italy",
            classification="Master"),
           
        Item(
            model="Janika 220",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$8,750.00",
            year="2003",
            country="Germany",
            classification="Student"),
        
        
        Item(
            model="Strad 330",
            description="Finely crafted and varnished by hand.",
            price="$28,560.00",
        	year="1894",
            country="Italy",
            classification="Master"),
        
        
        Item(
            model="Regarri 720",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$6,250.00",
            year="1998",
            country="Italy",
            classification="Beginner"),
        
        Item(
            model="Wilfer 740",
            description="Hand crafted, warm sound and even resonabce.",
        	price="$16,250.00",
            year="1927",
            country="Germany",
            classification="Advanced")
]

for item in items:
    session.add(item)
    session.commit()



print ("Added Users, and Cellos Yo!!! ^_^ ")