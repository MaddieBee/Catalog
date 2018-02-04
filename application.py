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
@app.route('/luthier/')
def showLuthiers():
    luthiers = session.query(Luthier).first()
    # return "This page will show all my restaurants"
    #return render_template('luthiers.html', luthiers=luthiers)
    items = session.query(CelloItem).filter_by(luthier_id 
    	=luthier.id)
    output = ''
    for i in items:
    	output += i.name 
    	output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000) 