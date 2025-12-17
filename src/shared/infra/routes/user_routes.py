from flask import Blueprint, request

from src.modules.create_user.app import create_user_presenter
from src.modules.delete_user.app import delete_user_presenter
from src.modules.get_all_users.app import get_all_users_presenter
from src.modules.get_user.app import get_user_presenter
from src.modules.update_user.app import update_user_presenter

user_routes = Blueprint('user_routes', __name__, url_prefix='/users')

@user_routes.route('/', methods=['POST'])
def create_user():
    return create_user_presenter.flask_handler(request)

@user_routes.route('/', methods=['GET'])
def get_all_users():
    return get_all_users_presenter.flask_handler(request)

@user_routes.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_presenter.flask_handler(request)

@user_routes.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    return update_user_presenter.flask_handler(request)

@user_routes.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_presenter.flask_handler(request)
