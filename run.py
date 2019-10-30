from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_jwt_extended import JWTManager
from passlib.hash import pbkdf2_sha256 as sha256
from flask_cors import CORS


db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
api = Api(app)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()  

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'} 

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)  

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)



class TaskModel(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
    task = db.Column(db.String(120), unique = True, nullable = False)
    description = db.Column(db.String(200), nullable = False)
    # user = db.relationship("User", backref=db.backref("ratings", order_by=rating_id))

    user = db.relationship("UserModel", backref=db.backref("tasks", order_by=task_id))
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  


    def to_json(self):
        return{'taskId':self.task_id,
                'userId': self.user_id,
                'task':self.task,
                'description':self.description} 

    def delete(self):
        db.session.delete(self)
        db.session.commit()            

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'task': x.task,
                'description': x.description
            }
        return {'tasks': list(map(lambda x: to_json(x), TaskModel.query.all()))}     

# app = Flask(__name__)
# api = Api(app)

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///thingstodo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'some-secret-string'

    db.app = app
    db.init_app(app)

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
    return RevokedTokenModel.is_jti_blacklisted(jti)

# import views, models, resources
import views, resources


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
api.add_resource(resources.DeleteTask, '/deletetask')
api.add_resource(resources.Test,'/test')







# app = Flask(__name__)

connect_to_db(app)

# FLASK_APP=run.py FLASK_DEBUG=1 flask run


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    # DebugToolbarExtension(app)
    app.run()