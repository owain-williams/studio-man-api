from flask import Flask
from flask_restful import Resource, Api
import json
from engineers import Engineer, getallengineers, getengineerbyid
from client import Client, getallclients

app = Flask(__name__)
api = Api(app)

class ClientResource(Resource):
    def get(self):
        return json.dumps(getallclients())

class EngineerResource(Resource):
    def get(self):
        return json.dumps(getallengineers())

api.add_resource(ClientResource, '/clients')
api.add_resource(EngineerResource, '/engineers')

if __name__ == '__main__':
    app.run(debug=True)