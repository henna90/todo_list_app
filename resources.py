from flask_restful import Resource, reqparse
from run import UserModel, RevokedTokenModel, TaskModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask import jsonify, redirect, make_response
import json

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = False)
parser.add_argument('password', help = 'This field cannot be blank', required = False)
parser.add_argument('name', help = 'This field cannot be blank', required = False)
parser.add_argument('task', help = 'This field cannot be blank', required = False)
parser.add_argument('description', help = 'This field cannot be blank', required = False)
parser.add_argument('task_id', help = 'This field cannot be blank', required = False)

# def tail(input_list):
#     """Return all elements of the input list except the first.

#     For example:

#         >>> tail(['Jan', 'Feb', 'Mar'])
#         ['Feb', 'Mar']
#     """

#     return input_list[1:]

def does_user_exist(username, password):
    """ if user exists in database returns an error message.
    >>> does_user_exist('Bubski', 'password')
    {'message': 'User Bubski already exists'}
    """
  
    if UserModel.find_by_username(username):
        response = {'message': 'User {} already exists'. format(username)}
        return response

def create_new_user(username, password):
    new_user = UserModel(
            username = username,
            password = UserModel.generate_hash(password)
        )
    return new_user    


class UserRegistration(Resource):
    def post(self):
        print("post request to registration page")

        data = parser.parse_args()
        username = data['username']
        password = data['password']

        does_user_exist(username, password)    
         
        new_user = create_new_user(username, password)

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = username)
            refresh_token = create_refresh_token(identity = username)
            return jsonify({
                'message': 'User {} was created'.format( username),
                'access_token' : access_token,
                'refresh_token': refresh_token
            })


            
        except:
            return jsonify({'message': 'Something went wrong'}), 500



class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['username']
        
        current_user = UserModel.find_by_username(username)
        print(data['password'],"================", current_user.password )
        if not current_user:
            print("user not found")
            
            return jsonify({'message': 'User {} doesn\'t exist'.format(username)})
        
        if UserModel.verify_hash(data['password'], current_user.password):
            
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])

            print("found the person ++++++++++++++++++++++++++++++++++++++++", current_user.username)



            # response.header = {"Content-Type: text/turtle", "Content-Location: mydata.ttl"
            #  "Access-Control-Allow-Origin: *"}

            return jsonify({'message': 'Logged in as {}'.format(current_user.username),
                     'access_token': access_token,
                     'refresh_token': refresh_token})

           
            
            
        else:
            print("worng creds============")
            return jsonify({'message': 'Wrong credentials'})
      
      
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
      
      
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
      
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_indentity()
        acces_token = create_access_token(identity = current_user)
        return {'access_token': 'access_token'}
      
      
class AllUsers(Resource):
    def get(self):
        all_users = UserModel.return_all()
        print(all_users)


        # return jsonify([user.to_json() for user in all_users])
        return UserModel.return_all()
    
    def delete(self):
        return UserModel.delete_all()

class AllTasks(Resource):
    def get(self):
        return TaskModel.return_all()
    
    def delete(self):
        return TaskModel.delete_all()   

      
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }

def current_user(username):
    """returns current users object.
    >>> current_user("Bubski")
    <UserModel 1>

    """
    return UserModel.find_by_username(username= username)    

def get_all_task_for_user(user_id):
    return TaskModel.query.filter_by(user_id = user_id).all()


class Todos(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = UserModel.find_by_username(username= current_user)   
        # user = current_user(current_user)
        user_id = user.id
        
        tasks = get_all_task_for_user(user_id)
        
        return jsonify([task.to_json() for task in tasks])
        # return jsonify({"hello": 55})
        # print(username)
        
        # UserModel.find_by_username(current_user)


def find_user(current_user):
    return UserModel.find_by_username(username = current_user)


def add_new_task_to_db(user_id,task,description):
   
    
    return  TaskModel(
                        user_id= user_id, 
                        task=task, 
                        description=description)
 
class AddTask(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user = find_user(current_user)
        user_id = user.id

        data = parser.parse_args()
        task = data['task']
        description=data['description']

        new_task = add_new_task_to_db(user_id,task,description)

        try:
            new_task.save_to_db()
            return {'message': "your task has been added"} 

        except:    
            return {'message': 'Something went wrong'}, 500        

def get_current_user():
    return get_jwt_identity()
class DeleteTask(Resource):
    @jwt_required
    def post(self):
        # print("hit delete task")
        # current_user = get_jwt_identity()
        current_user = get_current_user()
        print("current user", current_user)
        data = parser.parse_args()
        task_id = data['task_id']
        task = data['task']
        print(task)
        print(task_id)

        current_task = TaskModel.query.filter_by(task_id = task_id).one()

        if not current_task:
            return {'message': 'Something went wrong'}, 500

        print(current_task, "<<<<<<<<=========")
        print("current task", current_task.task)
        try:
            current_task.delete()
            return jsonify({ 'task_id': task_id,
                            'task':task })               
        except:    
            return {'message': 'Something went wrong'}, 500

        
        # # current_user = get_jwt_identity()
        # #query db for user id based on username

        # print("WORKING==================")
        # print(data['task'])

        # return {
        #     'working': 123
        # }

        # print(data['task'], data['description'])


        #add to task table in db 


class Test(Resource):
    def get(self):
        user  = {'Henna': "sent a request"}
        return jsonify(user)