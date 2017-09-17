from bson import json_util
from flask import Blueprint, request

from tutorialsharing.db.users_connection import UsersConnection


users_api = Blueprint('users_api', __name__)


db_host = 'localhost'
db_port = 27017
users_connection = UsersConnection(db_host, db_port)


@users_api.route('/users', methods=['POST'])
def create_user():
    json_request_object = request.get_json()

    # required
    userid = json_request_object['userid']

    # optional
    username = json_request_object.get('username')
    name = json_request_object.get('name')
    avatar_url = json_request_object.get('avatar_url')
    years_of_development = json_request_object.get('years_of_development')

    if years_of_development:
        years_of_development = int(years_of_development)

    results = users_connection.save_user(userid,
                                         username=username,
                                         name=name,
                                         avatar_url=avatar_url,
                                         years_of_development=years_of_development)
    return json_util.dumps(results)


@users_api.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    return json_util.dumps({'user': users_connection.get_user(userid)})


@users_api.route('/users', methods=['GET'])
def get_users():
    return json_util.dumps({'users': users_connection.get_users()})


@users_api.route('/users', methods=['PUT'])
def update_user():
    pass
