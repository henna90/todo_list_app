
from run import app
from flask import jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')