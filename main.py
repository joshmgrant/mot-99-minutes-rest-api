from flask import Flask, request
from flask.json import jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
api = Api(app)


# v1 - just an endpoint
@app.route("/sauce_logs")
def index():
    return "Sauce Logs - Logging your hot sauces"

entries = []

class EntriesResource(Resource):
    def get(self):
        return jsonify({"entries": entries})


class EntryResource(Resource):
    def post(self):
        entry = request.form
        entries.append(entry)
        return jsonify({"added new sauce log", "ok"})


api.add_resource(EntriesResource, '/entries')
api.add_resource(EntryResource, '/entry')
