from flask import Flask, render_template, url_for, request
from flask import Flask, render_template, request, jsonify, make_response, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# localhost:5000/
@app.route("/")
def home():
    return render_template('math1.html')

app.run()
