#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Luthier, Base, Cello, User

from flask import session as login_session 
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests 

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Cello Catalog"

engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state tokens
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    #return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

    # DISCONNECT - Revoke a current user's token and reset their login_session



@auth.verify_password
def verify_password(username_or_token, password):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True




'''@app.route('/clientOAuth')
def start():
    return render_template('clientOAuth.html')


@app.route('/oauth/<provider>', methods = ['POST'])
def login(provider):
    #STEP 1 - Parse the auth code
    auth_code = request.json.get('auth_code')
    print "Step 1 - Complete, received auth code %s" % auth_code
    if provider == 'google':
        #STEP 2 - Exchange for a token
        try:
            # Upgrade the authorization code into a credentials object
            oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(auth_code)
        except FlowExchangeError:
            response = make_response(
                json.dumps('Failed to upgrade the authorization code.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
          
        # Check that the access token is valid.
        access_token = credentials.access_token
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
               % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
        # If there was an error in the access token info, abort.
        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.headers['Content-Type'] = 'application/json'
            return response 
            
        # Verify that the access token is used for the intended user.
        gplus_id = credentials.id_token['sub']
        if result['user_id'] != gplus_id:
            response = make_response(
                json.dumps("Token's user ID doesn't match given user ID."), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # # Verify that the access token is valid for this app.
        if result['issued_to'] != CLIENT_ID:
            response = make_response(
                json.dumps("Token's client ID does not match app's."), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        stored_credentials = login_session.get('credentials')
        stored_gplus_id = login_session.get('gplus_id')
        if stored_credentials is not None and gplus_id == stored_gplus_id:
            response = make_response(json.dumps('Current user is already connected.'),
                                     200)
            response.headers['Content-Type'] = 'application/json'
            return response
            print "Step 2 Complete! Access Token : %s " % credentials.access_token

        #STEP 3 - Find User or make a new one
        
        #Get user info
        h = httplib2.Http()
        userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.access_token, 'alt':'json'}
        answer = requests.get(userinfo_url, params=params)
      
        data = answer.json()

        name = data['name']
        picture = data['picture']
        email = data['email']
        
        
     
        #see if user exists, if it doesn't make a new one
        user = session.query(User).filter_by(email=email).first()
        if not user:
            user = User(username = name, picture = picture, email = email)
            session.add(user)
            session.commit()

        

        #STEP 4 - Make token
        token = user.generate_auth_token(600)

        

        #STEP 5 - Send back token to the client 
        return jsonify({'token': token.decode('ascii')})
        
        #return jsonify({'token': token.decode('ascii'), 'duration': 600})
    else:
        return 'Unrecoginized Provider'

@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})
'''

@app.route('/index', methods=['GET'])
def showluthiers():
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
        print("well, outputs?")
    return output 


@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("main.html")

@app.route('/cellos/')
def showcellos():
    cellos = session.query(Cello.id,
                            Cello.model,
                            Cello.description,
                            Cello.price,
                            Cello.year,
                            Cello.country,
                            Cello.classification).all()
    print("Well, at least I tried")
    return render_template('cellos.html', cellos=cellos)


@app.route('/cellos/JSON')
def cellos_json():
    """Show all consoles as JSON"""
    cellos = session.query(Cello).all()
    return jsonify(luthiers=[c.serialize for c in cellos])


@app.route('/edit/')    
def editluthier():
    return render_template('editluthier.html')



@app.route('/delete/')    
def deleteluthier():
    return render_template('deleteluthier.html')

'''
ERROR list object is not callable

@app.route('/users')
def showUsers():
    users = session.query(User).all()   Testing
    return users 
'''

@app.route('/')
@app.route('/luthiers/')
def show_luthiers():
    """Show all manufacturers. If user is logged user can add, edit and delete manufacturers"""
    luthiers = session.query(Luthier).all()
    if 'username' in login_session:
        return render_template('luthiers.html', luthiers=luthiers)
    else:
        return render_template('publicluthiers.html', luthiers=luthiers)



@app.route('/luthiers/JSON')
def luthiers_json():
    """Show all luthiers as JSON"""
    luthiers = session.query(Luthier).all()
    return jsonify(luthiers=[l.serialize for l in luthiers])




@app.route('/luthier/<int:luthier_id>/cellos/')
def show_cellos(luthier_id):
    manufacturer = session.query(
        Luthier).filter_by(id=luthier_id).one()
    cellos = session.query(Cello).filter_by(
        luthier_id=luthier_id).all()
    if 'username' in login_session:
        return render_template('luthiercellos.html', luthier=Luthier.id, cellos=cellos)
    else:
        return render_template('publicluthiercellos.html', luthier=Luthier.id, cellos=cellos)

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
def newluthier():
    if request.method == 'POST':
        newluthier = Luthier(name=request.form['name'])
        session.add(newluthier)
        session.commit()
        print("Is this even working new luthiers?")
        return redirect(url_for('showluthiers'))
    else:
        return render_template('newluthier.html')
    # return "This page will be for adding a new Luthier"


@app.route('/luthiers/<int:luthier_id>/<int:cello_id>/edit',
           methods=['GET', 'POST'])
def editcello(luthier_id, cello_id):
    editeditem = session.query(cello_id).filter_by(id=cello_id).one()
    if request.method == 'POST':
        if request.form['model']:
            editeditem.model = request.form['model']
        if request.form['description']:
            editeditem.description = request.form['description']
        if request.form['price']:
            editeditem.price = request.form['price']
        if request.form['year']:
            editeditem.year = request.form['year']
        if request.form['country']:
            editeditem.country = request.form['country']
        if request.form['classification']:
            editeditem.classification = request.form['classification']
        session.add(editeditem)
        session.commit()
        return redirect(url_for("editcello.html", luthier_id=luthier_id))
    else:
        return render_template(
            'editcello.html', luthier_id=luthier_id, cello_id=cello_id, item=editeditem)

# Create a new Cello listing   THIS WORKS (at least a little bit)

@app.route('/cello/new/', methods=['GET', 'POST'])
def newcello():
    if request.method == 'POST':
        newitem = newcello.item(model=request.form['model'],
                            description=request.form['description'],
                            price=request.form['price'],
                            year=request.form['year'],
                            country=request.form['country'],
                            classification=request.form['classification'])
        session.add(newitem)
        session.commit()

        print("Okay so did we get this far?")
        return redirect(url_for('newcello.html'))
    else:
        return render_template('newcello.html')


@app.route('/main/')
def main():
    print("cello.html page")
    return render_template('main.html')






if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
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
