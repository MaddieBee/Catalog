#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, jsonify, url_for, g, flash, make_response, abort
from flask import session as login_session 
from sqlalchemy import create_engine, asc, desc 
from sqlalchemy.orm import sessionmaker
from database_setup import *
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2, os, random, string, datetime, json, requests


'''
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
'''

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
    return render_template('login2.html', STATE=state)


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
        print ("Token's client ID doesn't match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    #Check to see if user schon logged in.  
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id


    # Get user info
    h = httplib2.Http()
    userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt':'json'}
    answer = requests.get(userinfo_url, params=params)
  
    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Add the Provider to the Login Session
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getuser(data["email"])
    if not user_id:
        user_id = newuser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print ("done!")
    return output



    # DISCONNECT - Revoke a current user's token and reset their login_session


@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("main.html")




@app.route('/')
@app.route('/items/')
def showitems():
    """Show all items. If user is logged user can add, edit and delete items"""
    items = session.query(Item).order_by(asc(Item.model))
    return render_template('items.html', items=items)
    

# Show a Luthier's Cellos

@app.route('/item/<int:item_id>/')
def celloitems(item_id):
    items = session.query(Item).filter_by(id=item_id).all()
    return render_template('celloitems.html', items=items, item_id=item_id)
 


@app.route('/showitem/')
def showitem(Item_id):
    items = session.query(Item).one()
    return render_template('items.html', items=item_id)
    items = session.query(Item_id).filter_by(item_id=item_id)

    return items


@app.route('/items/JSON')
def items_json():
    """Show all items as JSON"""
    items = session.query(Item).all()
    return jsonify(items=[i.serialize for i in items])


'''
@app.route('/cellos/JSON')
def items_json():
    """Show all consoles as JSON"""
    items = session.query(Item).all()
    return jsonify(items=[i.serialize for i in items])
'''


# Add a new Luthier
@app.route('/item/new/', methods=['GET', 'POST'])
def newitem():
    if 'username' in login_session:
        if request.method == 'POST':
            newitem = Item(model=request.form['model'],
                        description=request.form['description'],   
                        price=request.form['price'],
                        year=request.form['year'],
                        country=request.form['country'],
                        classification=request.form['classification']                            
            )
            session.add(newitem)
            flash("New Item Successfully Added")
            session.commit()
            return redirect(url_for('showitems'))
        else:
            return render_template('newitem.html')     

    else:
        return redirect('/login')
    # return "This page will be for adding a new item"
    
    

@app.route('/edit/', methods=['GET', 'POST'])    
def edititem(item_id):
    if 'username' in login_session:
        switchitup = session.query(Item).filter_by(id=item_id).one()

        if request.method == 'POST':
            if request.form['name']:
                switchitup.model = request.form['model'],
                switchitup.description = request.form['description'],   
                switchitup.price = request.form['price'],
                switchitup.year = request.form['year'],
                switchitup.country = request.form['country'],
                switchitup.classification = request.form['classification']  
        
                session.commit()
            return redirect(url_for('showitems', item_id=switchitup.id))

        else:
            items = session.query(Item.id, Item.model).all()


            return render_template('edititem.html', item=switchitup, items=items)

    else:
        return redirect('/login')


@app.route('/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editcello(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['model']:
            item.model = request.form['model']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['price']:
            item.price = request.form['price']
        if request.form['year']:
            item.year = request.form['year']
        if request.form['country']:
            item.country = request.form['country']
        if request.form['classification']:
            item.classification = request.form['classification']
        session.add(item)
        session.commit()
        return render_template('edititem.html', item=item, item_id=item.id)
    else:
        return render_template(
            'edititem.html', item=item, item_id=item.id)



@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteitem(item_id):
    if 'username' in login_session:
        delete_item = session.query(
            Item).filter_by(id=item_id).one()

        if request.method == 'POST':
            session.delete(delete_item)
            session.commit()
            flash('Item Successfully Deleted %s' %
                delete_item.name)
            return redirect(url_for('showitems'))
        else:
            return render_template('deleteitem.html', item=delete_item)
    else:
        return redirect('/login')


'''
@app.route('/cellos/')
def showcellos():
    if items in session.query(Item.id,
        Item.model,
        Item.description,
        Item.price,
        Item.country,
        Item.classification,                                            
    
    return render_template('cellos.html', items=Item.id, items=items)
'''

'''
@app.route('/item/<int:item_id>/items/')
def showitems(item_id):
    items = session.query(Item).filter_by(id=item_id).all()
    if 'username' in login_session:
        return render_template('celloitems.html', items=items)
    else:
        return render_template('publiccelloitems.html', items=items)
'''


@app.route('/users')
def showusers():
    users = session.query(User.id,
                          User.name,
                          User.email,
                          User.picture).all()
    
    return render_template('users.html', users=users)

'''
@app.route('/cello/<int:item_id>/all')
@app.route('/cellos/')
def celloItem(): 
    if request.method == 'GET':
        cellos = session.query(Cello).filter_by(id=item.id, Item).one()
        items = session.query(Cello).filter_by(item_id=item.id).all()

        return render_template('cello.html', cellos=cellos, items=items)
        
    return render_template('cello.html, item=item, items=items, item_id=item_id')
'''

def getuser(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/api/users/<int:id>')
def get_user(id):
    user = session.query(User).filter_by(id=id).one()
    if not user: abort(400)
    return jsonify({'username': user.username})




'''
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
'''    

'''
@app.route('/deletecelloitem/')    
def deleteCello():
    return render_template('deletecelloitem.html')


@app.route('/editcelloitem/')    
def editCello():
    return render_template('editcelloitem.html')
'''





def newuser(login_session):
    #newuser = User(name=login_session['username'], email=login_session[
     #              'email'], picture=login_session['picture'])
    newuser = User(name=login_session['username'],
                    email=login_session['email'], picture=login_session['picture'])
    session.add(newuser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

'''
@app.route('/users', methods = ['POST'])
def new_user():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        print ("missing arguments")
        abort(400) 
        
    if session.query(User).filter_by(email = email).first() is not None:
        print ("existing user")
        user = session.query(User).filter_by(email=email).first()
        return jsonify({'message':'user already exists'}), 200#, 
            {'Location': url_for('get_user', id = user.id, _external = True)}
        
    user = User(email = email)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'email': user.email }), 201#, 
        {'Location': url_for('get_user', id = user.id, _external = True)}
'''

@app.route('/disconnect')
def disconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print ("Le Access Token ist None")
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    h.request(url, 'GET')[0]
    login_session.clear()

    flash("Login session has successfully been terminated!  Auf Wiedersehen!")
    return redirect(url_for('showitems'))
    


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



# When using strings, no need to specify data type.  But for integers 
# you must specify the data type.

# @app.route('/post/<int:post_id')
# def show_post(post_id):
    # show the post with the given id, the id is an integer
#    return 'Post %d' post_id
