from flask import Flask
from flask import render_template
from datetime import datetime
from . import app
import disc_data



@app.route("/")
def home():
    return render_template(
        "main.html",
        brands=disc_data.getAllBrands(),
        discs=disc_data.getAllDiscs()
    )

@app.route("/getDiscs")
def getDiscs():
    return disc_data.getAllDiscs()


@app.route("/brands")
def brands():
    return disc_data.getAllBrands()