# from flask import Flask, render_template, redirect, request
# from model import Task, connect_to_db, db
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy

# import model,resources


# app = Flask(__name__, static_folder="build/static", template_folder="build")
# api=Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'some-secret-string'

# db = SQLAlchemy(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# api.add_resource(resources.UserRegistration, '/registration')
# api.add_resource(resources.UserLogin, '/login')
# api.add_resource(resources.UserLogoutAccess, '/logout/access')
# api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
# api.add_resource(resources.TokenRefresh, '/token/refresh')
# api.add_resource(resources.AllUsers, '/users')
# api.add_resource(resources.SecretResource, '/secret')



# @app.route("/")
# def homepage():
#     return render_template('index.html')
# print('Starting Flask!')

# @app.route("/addtask",methods=["POST"])
# def addtask():
   
#     task = request.form['text']
#     priority = request.form['priority']
#     #add to db
#     new_task = Task(task=task, priority=priority)
#     db.session.add(new_task)
#     db.session.commit()

#     #return a jsonified json object 

#     return "to do added...."



# if __name__ == "__main__":
#     app.debug=True
#     connect_to_db(app)
#     app.run(port=3000)
   
#     print('connected to server')

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
# import psycopg2-binary

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///thingstodo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

import views, models, resources

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')


api.add_resource(resources.AllTasks, '/all_tasks')
api.add_resource(resources.SecretResource, '/secret')
api.add_resource(resources.Todos,'/todos')
api.add_resource(resources.AddTask, '/addtask')