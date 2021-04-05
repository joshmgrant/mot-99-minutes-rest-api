from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


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
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))
    heat_level = db.Column(db.String(10))

    def __repr__(self):
        return '<Entry {}>'.format(self.title)


class EntrySchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "heat_level")


entry_schema = EntrySchema()
entries_schema = EntrySchema(many=True)
# - v4

class EntriesResource(Resource):
    def get(self):
        entries = Entry.query.all()
        return entries_schema.dump(entries)

    def post(self):
        new_entry = Entry(
            title = request.json['title'],
            description = request.json['description'],
            heat_level = request.json['heat_level']
        )
        db.session.add(new_entry)
        db.session.commit()
        return entry_schema.dump(new_entry)


class EntryResource(Resource):
    def get(self, post_id):
        entry = Entry.query.get_or_404(post_id)
        return entry_schema.dump(entry)

    def patch(self, post_id):
        entry = Entry.query.get_or_404(post_id)

        if 'title' in request.json:
            entry.title = request.json['title']
        if 'description' in request.json:
            entry.description = request.json['description']
        if 'heat_level' in request.json:
            entry.heat_level = request.json['heat_level']

        db.session.commit()
        return entry_schema.dump(entry)

    def delete(self, post_id):
        entry = Entry.query.get_or_404(post_id)
        db.session.delete(entry)
        db.session.commit()
        return '', 204


api.add_resource(EntriesResource, '/entries')
api.add_resource(EntryResource, '/entry/<int:post_id>')

# to run using flask development server, 
# FLASK_APP=main.py flask run
# to run using gunicorn
# gunicorn --bind 0.0.0.0:5000 main:app