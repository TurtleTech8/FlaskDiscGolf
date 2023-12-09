from flask import render_template
from flask import request
from . import app
import disc_golf_app.disc_data as disc_data



@app.route("/")
def home():
    return render_template(
        "main.html",
        brands=disc_data.getAllBrands(),
        discs=disc_data.getAllDiscs()
    )

@app.route("/search")
def search():
    return render_template(
        "search.html",
        brands=disc_data.getAllBrands(),
        discs=disc_data.getSearchDiscs()
    )

@app.route("/getDisc")
def getDisc():
    return disc_data.getDisc(request.args.get('name'))

@app.route("/getRelatedDiscs")
def getRelatedDiscs():
    return disc_data.getRelatedDiscs(request.args.get('name'))