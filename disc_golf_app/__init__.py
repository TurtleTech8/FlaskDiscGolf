import flask
from disc_golf_app.extensions import mdb
app = flask.Flask(__name__)
print('http://localhost:5000')
mdb.init_app()