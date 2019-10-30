
from run import app
from flask import jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')


    # def does_user_exist( username, password):
    # """ if user exists in database returns an error message."""
  
    # if UserModel.find_by_username(username):
    #     response = {'message': 'User {} already exists'. format(username)}
    #     return response