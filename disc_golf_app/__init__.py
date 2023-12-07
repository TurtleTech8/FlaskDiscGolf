import flask
from extensions import mdb
app = flask.Flask(__name__)
mdb.init_app()