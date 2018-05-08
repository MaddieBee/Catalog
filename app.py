#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, jsonify, url_for, g, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Transaction, Item, User

from flask import session as login_session 
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests 


from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()



APPLICATION_NAME = "Cello Catalog"

engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']



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
        print (response)
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


@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})



'''
@app.route('/index', methods=['GET'])
 
def showitems():
    item = session.query(Item).first()
    items = session.query(Cello).filter_by(item_id=item.id, item=item)
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
'''

'''
@app.route('/')
<<<<<<< HEAD
@app.route('/luthiers/')
def showluthiers():
    """Show all manufacturers. If user is logged user can add, edit and delete manufacturers"""
    items = session.query(Item).all()
||||||| merged common ancestors
@app.route('/luthiers/')
def showluthiers():
    """Show all manufacturers. If user is logged user can add, edit and delete manufacturers"""
    luthiers = session.query(Luthier).all()
=======
@app.route('/items/')
def showitems():
    """Show all items. If user is logged user can add, edit and delete items"""
    item = session.query(Item).all()
>>>>>>> major-changes
    if 'username' in login_session:
<<<<<<< HEAD
        return render_template('luthiers.html', items=items)
||||||| merged common ancestors
        return render_template('luthiers.html', luthiers=luthiers)
=======
        return render_template('items.html', item=items)
>>>>>>> major-changes
    else:
<<<<<<< HEAD
        return render_template('publicluthiers.html',  items=items)
||||||| merged common ancestors
        return render_template('publicluthiers.html', luthiers=luthiers)
=======
        return render_template('publicitems.html', item=items)




>>>>>>> major-changes


# Show a Luthier's Cellos

@app.route('/item/<int:item_id>/')
@app.route('/item/<int:item_id>/cello')
def showitems(item_id):
    items = session.query(celloItem).filter_by(item_id=item.id).all()
    return render_template('cello.html', items=items, item=item)
 


@app.route('/item/')
def showitems():
    items = session.query(Item).first()
    return "This page will show all of the items"
    return render_template('items.html', items=items)
    items = session.query(Item).filter_by(item_id
    	=item.id)

    output += '</br>'
    return output
'''

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
    if request.method == 'POST':
        newitem = Item(model=request.form['model'],
                             id=request.form['id'],
                             
        )
        session.add(newitem)
        session.commit()
        flash("Is this even working new items?")
        return redirect(url_for('showitems'))
    else:
        return render_template('newitem.html')
    # return "This page will be for adding a new item"
    
    

@app.route('/edit/')    
def edititem():
    return render_template('edititem.html')



@app.route('/items/<int:item_id>/<int:item_id>/edit',
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
        return render_template('editcelloitem.html', item=item, item_id=item.id)
    else:
        return render_template(
            'editcelloitem.html', item=item, item_id=item.id)



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
    
    return items
        return render_template('cellos.html', items=Item.id, items=items)
'''


@app.route('/item/<int:item_id>/items/')
def show_cellos(item_id):
    items = session.query(Item).filter_by(id=item_id).all()
    if 'username' in login_session:
        return render_template('celloitems.html', items=items)
    else:
        return render_template('publiccelloitems.html', items=items)



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
    if not user:
        abort(400)
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
