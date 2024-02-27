from disc_golf_app.extensions import mdb
from flask import session


def addDisc():
    session['cart'] = 'randomDisc'
    return session['cart']