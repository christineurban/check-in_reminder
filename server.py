from flask import Flask, render_template, redirect, flash, session

import jinja2

import os

app = Flask(__name__)

app.secret_key = FLASK_SECRET_KEY

app.jinja_env.undefined = jinja2.StrictUndefined


################################################################################

@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")

################################################################################

if __name__ == "__main__":
    
    app.debug = True # for DebugToolbarExtension
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    app.run(port=5000, host='0.0.0.0')

