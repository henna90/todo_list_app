# import unittest

from run import UserModel, TaskModel


# class DescribeTests(unittest.TestCase):
#     """TestCase skeleton."""

#     def test_does_user_exist(self):
#         """test does user exist function """

#         self.assertEqual(resources.does_user_exist('Bubski','password'),{'message': 'User Bubski already exists'})

def create_new_user(username, password):
    """ create a new user object.
    >>> create_new_user("John123", "password")
    <UserModel (transient 4372842384)>

    """
    new_user = UserModel(
            username = username,
            password = UserModel.generate_hash(password)
        )
    return new_user 


def does_user_exist(username, password):
    """ if user exists in database returns an error message.
    >>> does_user_exist('Bubski', 'password')
    {'message': 'User Bubski already exists'}
    """
  
    if UserModel.find_by_username(username):
        response = {'message': 'User {} already exists'. format(username)}
        return response    


def current_user(username):
    """returns current users object.
    >>> current_user("Bubski")
    <UserModel 1>

    """
    return UserModel.find_by_username(username= username)


def get_all_task_for_user(user_id):
    """ returns all tasks for user.
    >>> get_all_task_for_user(1)
    [<TaskModel 51>]
    """
    return TaskModel.query.filter_by(user_id = user_id).all()    

# def all_users ():
#     return returnUserModel.return_all()        


# to run doctests : python3 -m doctest -v test.py