from flask import Flask


app = Flask(__name__)

# v1 - just an endpoint
@app.route("/sauce_logs")
def index():
    return "Sauce Logs - Logging your hot sauces"