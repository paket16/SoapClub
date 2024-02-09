from flask import Flask, render_template, request, redirect, url_for
from database import Database


app = Flask(__name__)

@app.route('/')
def index():
    db = Database('database.db')
    db.createTestPost()
    goods = db.database.execute('SELECT * FROM goods').fetchall()
    
    del db

    return render_template("index.html", goods = goods)

#TODO:
# @app.route('/buy')
# def buy(goodId):


# @app.route('/card')
# def card(goodId):
#     db = Database('database.db')
#     good = db.database.execute('SELECT * FROM goods WHERE id = ?', (goodId,)).fetchall()
#     del db
#     return render_template('good.html', good = good)