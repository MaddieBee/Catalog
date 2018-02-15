from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Luthier, Base, CelloItem

app = Flask(__name__)

engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all Luthiers

@app.route('/')
def index():
    return 'Hier ist unsere Startseite>'

@app.route('/profile/')
def profile():
    return '<h2>This is the default start page for users.</h2>'

@app.route('/profile/<username>')
def profile(username):
    return"Was geht ab %s?" % username

@app.route('/main.html/')
def main():
    return render_template('main.html')

@app.route('/luthier/')
def showLuthiers():
    luthiers = session.query(Luthier).first()
    return "This page will show all my restaurants"
    return render_template('luthiers.html', luthiers=luthiers)
    items = session.query(Luthier).filter_by(luthier_id
    	=luthier.id)
    output = ''
    for i in items:
    	output += i.name 
    	output += '</br>'
    return output

    return "confusion"

# When using strings, no need to specify data type.  But for integers 
# you must specify the data type.

@app.route('/post/<int:post_id')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' post_id


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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)





'''
@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

@app.route('/')
def ():
    return

'''    


# Create route for new cello listing function

#@app.route('/luthier/<int:luthier_id/>/<int:ce')

