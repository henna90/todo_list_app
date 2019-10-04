# import datetime
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt import JWT, jwt_required, current_identity
# from werkzeug.security import safe_str_cmp


# db = SQLAlchemy()

# ##############################################################################
# # Model definitions

# class User(db.Model):
#     """User of todo website."""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     email = db.Column(db.String(64), nullable=True)
#     password = db.Column(db.String(64), nullable=True)

#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()
    
#     def __repr__(self):
#         return(f"<User user_id={self.user_id} email={self.email}>")




# class Task(db.Model):

#     __tablename__ = "tasks"
#     task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     task = db.Column(db.String, nullable=False)
#     priority = db.Column(db.String, nullable=True)
#     # due_date = db.Column(db.DateTime, nullable=False, default=datetime.now)



#     # user = db.relationship("User", backref=db.backref("tasks", order_by=task_id))

# #############################################################################
# # def authenticate(email,password):
# #     user =     

from run import db
from passlib.hash import pbkdf2_sha256 as sha256




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
    user_id = db.Column(db.Integer, nullable = False)
    task = db.Column(db.String(120), unique = True, nullable = False)
    description = db.Column(db.String(200), nullable = False)

    # user = db.relationship("UserModel", backref=db.backref("tasks", order_by=task_id))
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()    
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'task': x.task,
                'description': x.description
            }
        return {'users': list(map(lambda x: to_json(x), TaskModel.query.all()))}     





   



# ##############################################################################
# # Helper functions

# # def connect_to_db(app):
# #     """Connect the database to our Flask app."""

# #     # Configure to use our PstgreSQL database
# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todo'
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #     db.app = app
# #     db.init_app(app)

#     # @app.before_first_request
#     # def create_tables():
#     #     db.create_all()


# if __name__ == "__main__":
#     # As a convenience, if we run this module interactively, it will leave
#     # you in a state of being able to work with the database directly.

#     from serve import app
#     connect_to_db(app)
#     print("Connected to DB.")

