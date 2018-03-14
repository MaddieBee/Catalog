#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, jsonify, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Luthier, Base, Cello, User

from flask import session as login_session 

app = Flask(__name__)

engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Main Page.  Displays all Luthier's cellos.  WELL????

@app.route('/')
@app.route('/index', methods=['GET'])
def showLuthiers():
    luthier = session.query(Luthier).first()
    items = session.query(Cello).filter_by(luthier_id=luthier.id, luthier=luthier)
    output = ''
    for i in items:
        output += "Model:  " + i.model 
        output += '</br>'
        output += "Country: " + i.country 
        output += '</br>' 
        output += "Classification:  " + i.classification 
        output += '</br>'
        output += "Price  " + i.price 
        output += '</br>'       
        output += '</br>'       

    return output


@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")

@app.route('/cellos/')
def showCellos():
    cellos = session.query(Cello.id,
                            Cello.model,
                            Cello.description,
                            Cello.price,
                            Cello.year,
                            Cello.country,
                            Cello.classification).all()
    print("Well, at least I tried")
    return render_template('cellos.html', cellos=cellos)


@app.route('/edit/')    
def editLuthier():
    return render_template('editluthier.html')



@app.route('/delete/')    
def deleteLuthier():
    return render_template('deleteluthier.html')

'''
ERROR list object is not callable

@app.route('/users')
def showUsers():
    users = session.query(User).all()   Testing
    return users 
'''




'''
Turkeybutt
ERROR - BuildError: Could not build url for endpoint 'Luthiers'. Did you mean 'luthier' instead?

# Loads the error pag

@app.route('/luthier/')
def luthier():
    luthiers = session.query(Luthier).all()
    # return "This page will show all of the luthiers"
    return render_template('luthiers.html', luthiers=luthiers)

'''


# Show a Luthier's Cellos

''' @app.route('/luthier/<int:luthier_id>/')
@app.route('/luthier/<int:luthier_id>/cello')
def showLuthiers(luthier_id):
    luthier = session.query(Luthier).filter_by(id=luthier_id).one()
    items = session.query(celloItem).filter_by(luthier_id=luthier.id).all()
    return render_template('cello.html', items=items, luthier=luthier)
''' 


'''
@app.route('/cello/<int:luthier_id>/all')
@app.route('/cellos/')
def celloItem(): 
    if request.method == 'GET':
        cellos = session.query(Cello).filter_by(id=luthier_id, luthier=luthier).one()
        items = session.query(Cello).filter_by(luthier_id=luthier.id).all()

        return render_template('cello.html', cellos=cellos, items=items)
        
    return render_template('cello.html, luthier=luthier, items=items, luthier_id=luthier_id')
'''


# Add a new Luthier
@app.route('/luthier/new/', methods=['GET', 'POST'])
def newLuthier():
    if request.method == 'POST':
        newLuthier = Luthier(name=request.form['name'])
        session.add(newLuthier)
        session.commit()
        print("Is this even working new luthiers?")
        return redirect(url_for('showLuthiers'))
    else:
        return render_template('newluthier.html')
    # return "This page will be for adding a new Luthier"


@app.route('/luthiers/<int:luthier_id>/<int:cello_id>/edit',
           methods=['GET', 'POST'])
def editCelloItem(luthier_id, cello_id):
    editedItem = session.query(CelloItem).filter_by(id=cello_id).one()
    if request.method == 'POST':
        if request.form['model']:
            editedItem.model = request.form['model']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['year']:
            editedItem.year = request.form['year']
        if request.form['country']:
            editedItem.country = request.form['country']
        if request.form['classification']:
            editedItem.classification = request.form['classification']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('luthierInventory', luthier_id=luthier_id))
    else:
        return render_template(
            'editcelloitem.html', luthier_id=luthier_id, cello_id=cello_id, item=editedItem)

# Create a new Cello listing   THIS WORKS (at least a little bit)

@app.route('/luthier/new/', methods=['GET', 'POST'])
def newCelloItem():
    if request.method == 'POST':
        newItem = celloItem(model=request.form['model'],
                            description=request.form['description'],
                            price=request.form['price'],
                            year=request.form['year'],
                            country=request.form['country'],
                            classification=request.form['classification'])
        session.add(newItem)
        session.commit()

        print("Okay so did we get this far?")
        return redirect(url_for('newCelloItem.html'))
    else:
        return render_template('newcelloitem.html')

    return render_template('newcelloitem.html')


@app.route('/cello/')
def main():
    print("cello.html page")
    return render_template('cello.html')






if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)


'''
# Show all catalogs 


@app.route('/catalogs/', methods=['GET, 'POST'])
def showCatalogs(): 







@app.route('/luthier/')
def showLuthiers():
    luthiers = session.query(Luthier).first()
    return "This page will show all of the luthiers"
    return render_template('luthiers.html', luthiers=luthiers)
    items = session.query(Luthier).filter_by(luthier_id
    	=luthier.id)

    output += '</br>'
    return output

@app.route('/deletecelloitem/')    
def deleteCello():
    return render_template('deletecelloitem.html')


@app.route('/editcelloitem/')    
def editCello():
    return render_template('editcelloitem.html')



# When using strings, no need to specify data type.  But for integers 
# you must specify the data type.

# @app.route('/post/<int:post_id')
# def show_post(post_id):
    # show the post with the given id, the id is an integer
#    return 'Post %d' post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

'''


'''
URLs with Variables
"path.<type:variable_name>/path"

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return
'''