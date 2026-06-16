import os, sys
from flask import Flask, render_template

# Point template folder to the project root templates/
tmpl = os.path.join(os.path.dirname(__file__), '..', 'templates')
app = Flask(__name__, template_folder=tmpl)

@app.route("/")
def index():
    return render_template("game.html")
