from flask import render_template
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
        "search.html"
    )