from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.modules.create_user.app.create_user_controller import CreateUserController

from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.modules.delete_user.app.delete_user_controller import DeleteUserController

from src.modules.get_all_users.app.get_all_users_usecase import GetAllUsersUsecase
from src.modules.get_all_users.app.get_all_users_controller import GetAllUsersController

from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.modules.get_user.app.get_user_controller import GetUserController

from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.modules.update_user.app.update_user_controller import UpdateUserController

from src.shared.environments import Environment
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse

app = Flask(__name__)
CORS(app)
load_dotenv()

repos = Environment().get_repositories()
user_repository = repos["user_repo"]

@app.route('/', methods=['GET'])
def alive():
    return f'My CRUD'

@app.route('/', methods=['POST'])
def hello_world():
    request_json = request.get_json(silent=True)
    name = request_json.get('name') if request_json else 'World'
    return f'Hello, {name}!'

@app.route('/user', methods=['POST'])
def create_user():
    usecase = CreateUserUsecase(user_repository)
    controller = CreateUserController(usecase)

    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    return FlaskHttpResponse(response).to_flask_response()

@app.route('/user', methods=['DELETE'])
def delete_user():
    usecase = DeleteUserUsecase(user_repository)
    controller = DeleteUserController(usecase)

    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    return FlaskHttpResponse(response).to_flask_response()

@app.route('/users', methods=['GET'])
def get_all_users():
    usecase = GetAllUsersUsecase(user_repository)
    controller = GetAllUsersController(usecase)

    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    return FlaskHttpResponse(response).to_flask_response()

@app.route('/user', methods=['GET'])
def get_user():
    usecase = GetUserUsecase(user_repository)
    controller = GetUserController(usecase)

    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    return FlaskHttpResponse(response).to_flask_response()

@app.route('/user', methods=['PUT'])
def update_user():
    usecase = UpdateUserUsecase(user_repository)
    controller = UpdateUserController(usecase)

    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    return FlaskHttpResponse(response).to_flask_response()


def my_crud(request):
    with app.request_context(request.environ):
        try:
            rv = app.preprocess_request()
            if rv is None:
                rv = app.dispatch_request()
        except Exception as e:
            rv = app.handle_user_exception(e)
        response = app.make_response(rv)
        return app.process_response(response)

if os.getenv('ENV') == 'dev':
    if __name__ == '__main__':
        print('Running in dev mode')
        app.run(debug=True)
