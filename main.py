from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'message': 'okey!'}


class Users(Resource):
    def get(self):
        data = [{"id": 1, "name": "bob"}, {"id": 1, "name": "bob"}, {"id": 1, "name": "bob"}]
        return data


api.add_resource(Home, "/")
api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run(debug=True)
