from flask_restful import Resource, reqparse
from run import UserModel, RevokedTokenModel, TaskModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = False)
parser.add_argument('password', help = 'This field cannot be blank', required = False)
parser.add_argument('name', help = 'This field cannot be blank', required = False)
parser.add_argument('task', help = 'This field cannot be blank', required = False)
parser.add_argument('description', help = 'This field cannot be blank', required = False)

class UserRegistration(Resource):
    def post(self):
        print("post request to registration page")

        data = parser.parse_args()
        print(data['username'], data['password'])


        

        #query db to see if user exsists
        if UserModel.find_by_username(data['username']):
          return {'message': 'User {} already exists'. format(data['username'])}

         

        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data ['username'])
            return {
                'message': 'User {} was created'.format( data['username']),
                'access_token' : access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500



class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        print(data['password'],"================", current_user.password )
        if not current_user:
            
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if UserModel.verify_hash(data['password'], current_user.password):
            print("++++++++++++++++++++++++++++++++++++++++")
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {'message': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token}
        else:
            return {'message': 'Wrong credentials'}
      
      
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

class Todos(Resource):
#     @jwt_required
    def get(self):
#         current_user = get_jwt_identity()
#         print(current_user)
        return {"hello": 55}
        # print(username)
        
        # UserModel.find_by_username(current_user)






class AddTask(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        data = parser.parse_args()
        print(data)
        task = data['task']
        description=data['description']
        user = UserModel.find_by_username(username = current_user)
        user_id = user.id

        print("**************************",user_id)

        new_task = TaskModel(
                        user_id= user_id, 
                        task=task, 
                        description=description)

        try:
            new_task.save_to_db()
            return {'message': "your task has been added"} 

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


#install psycopg2 ... should fix tasks table issue 