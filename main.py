from flask import Flask
from flask_restful import Api
from db import db

from resources.user import UserResource, UsersList
from resources.covid_data import CovidData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserResource, '/signup', methods=["POST"])
api.add_resource(UsersList, '/users', methods=['GET']) # Total number of users
api.add_resource(CovidData, '/covid-data-and-sending-mail', methods=['POST'])

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
