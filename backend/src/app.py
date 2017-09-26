from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db import set_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
api = Api(app)
db.init_app(app)

db.create_all()

set_db(db)

from resources.trip import TripResource

api.add_resource(TripResource, '/trip/<int:trip_id>')

if __name__ == '__main__':
  app.run(debug=True)
