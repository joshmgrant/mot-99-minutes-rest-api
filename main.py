from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
api = Api(app)

entries = []

# v1 - just an endpoint
@app.route("/sauce_logs")
def index():
    return "Sauce Logs - Logging your hot sauces"
# - v1

# v2 - create POST (add entry) and GET (list all entries) endpoints
# @app.route("/sauce_logs/entry", methods=['POST'])
# def add_log():
#     entry = request.form
#     entries.append(entry)
#     return jsonify({'added new sauce log': 'ok'})

# @app.route("/sauce_logs/entries", methods=['GET'])
# def get_log():
#     return jsonify({"entries": entries})
# -v2


# v4 - add database instead of using in-memory storage
# class Entry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     description = db.Column(db.String(255))
#     heat_level = db.Column(db.String(10))

#     def __repr__(self):
#         return '<Post {}>'.format(self.title)


# class EntrySchema(ma.Schema):
#     class Meta:
#         fields = ("id", "title", "description", "heat_level")


# entry_schema = EntrySchema()
# entries_schema = EntrySchema(many=True)
# - v4

class EntriesResource(Resource):
    def get(self):
        return entries

class EntryResource(Resource):
    def get(self, entry_id):
        try:
            return entries[entry_id]
        except ValueError:
            return 'Invalid entry index', 400

    def post(self):
        new_entry = {}
        new_entry['title'] = request.json['title']
        new_entry['description'] = request.json['description']
        new_entry['heat_level'] = request.json['heat_level']
        entries.append(new_entry)
        return 'added new sauce log entry', 200

api.add_resource(EntriesResource, '/entries')
api.add_resource(EntryResource, '/entry/<int:post_id>')



# v5 - install and use guicorn/uvicorn

