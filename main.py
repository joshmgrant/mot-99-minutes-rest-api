from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sauce_logs")
def index():
    return "Sauce Logs - Logging your hot sauces"

# keeping data in memory, aka The Very Bad, No Good Idea
entries = []

# v2 - create POST (add entry) and GET (list all entries) endpoints
@app.route("/entry", methods=['POST'])
def add_log():
    entry = request.form
    entries.append(entry)
    return jsonify({'added new sauce log': 'ok'})

@app.route("/entries", methods=['GET'])
def get_log():
    return jsonify({"entries": entries})
