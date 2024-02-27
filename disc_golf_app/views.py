from flask import render_template
from flask import request
from flask import session
from . import app
import disc_golf_app.disc_data as disc_data
import disc_golf_app.cart as cart

app.secret_key = "SUPER_SECRET_KEY"

def checkSession():
    if 'uid' not in session:
            session['uid'] = 3

@app.route("/")
def home():
    checkSession()
    return render_template(
        "main.html",
        brands=disc_data.getAllBrands(),
        discs=disc_data.getAllDiscs()
    )

@app.route("/search")
def search():
    checkSession()

    print(session['cart'])
    return render_template(
        "search.html",
        brands=disc_data.getAllBrands(),
        discs=disc_data.getSearchDiscs()
    )

@app.route("/shoppingCart")
def shoppingCart():
    checkSession()

    print(session['uid'])
    return render_template(
        "cart.html"
    )

@app.route("/addToCart")
def addToCart():
     return cart.addDisc()

@app.route("/getDisc")
def getDisc():
    return disc_data.getDisc(request.args.get('name'))

@app.route("/getRelatedDiscs")
def getRelatedDiscs():
    return disc_data.getRelatedDiscs(request.args.get('name'))