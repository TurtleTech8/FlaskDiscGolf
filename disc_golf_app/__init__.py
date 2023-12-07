import flask
from disc_golf_app.extensions import mdb
app = flask.Flask(__name__)
mdb.init_app()