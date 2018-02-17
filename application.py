from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Luthier, Base, CelloItem

app = Flask(__name__)

engine = create_engine('sqlite:///cellocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show a Luthier's Cellos

@app.route('/luthier/<int:luthier_id>/')
@app.route('/luthier/<int:luthier_id>/cello')
def showCellos(luthier_id):
    luthier = session.query(Luthier).filter_by(id=luthier_id).one()
    items = session.query(CelloItem).filter_by(luthier_id=luthier.id).all()
    return render_template('cello.html', items=items, restaurant=restaurant)
     

@app.route('/cello/')
def main():
    return render_template('celloitem.html')

@app.route('/luthier/')
def showLuthiers():
    luthiers = session.query(Luthier).first()
    return "This page will show all of the luthiers"
    return render_template('luthiers.html', luthiers=luthiers)
    items = session.query(Luthier).filter_by(luthier_id
    	=luthier.id)

    output += '</br>'
    return output

@app.route('/')  
@app.route('/deletecelloitem/')    
def deleteCello():
    return render_template('deletecelloitem.html')

@app.route('/')  
@app.route('/deleteluthier/')    
def deleteLuthier():
    return render_template('deleteluthier.html')

@app.route('/')  
@app.route('/editcelloitem/')    
def editCello():
    return render_template('editcelloitem.html')

@app.route('/')  
@app.route('/editluthier/')    
def editLuthier():
    return render_template('editluthier.html')

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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)





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