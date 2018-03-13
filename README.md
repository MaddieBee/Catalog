Item Catalog Project for Udacity Full Stack Nanodegree.  
~~ Maddie Bold ~~


A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items.


Required Software:

	Vagrant

	Python


In Order to get this application running follow these steps:   

1. Clone Udacity's Full Stack Nanodegree reposity for the virtual machine :
	[fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Find the *catalog* folder and replace it with the contents of this respository.


Running the Software:

Inside the Vagrant folder, launch the virtual machine with  
	
	"vagrant up"

Next run:
	
	"vagrant ssh"

Change directories to the correct folder with the following two commands:

	"cd /vagrant"

	"cd catalog"

To make sure you are in the correct place type:

	"ls"

You should see numerous files, including database_setup.py, application.py, and cellocatalog.db.

First, run the python file that will create your database:
	
	"python database_setup.py"

Next, populate the database file with the information provided in manycellos.py:

	"python manycellos.py"

Finally, initialize the application:

	"python application.py"


In a web browser, navigate to :

	"http://0.0.0.0:8000/"
