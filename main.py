from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

from src.modules.create_user.app import create_user_presenter
from src.modules.delete_user.app import delete_user_presenter
from src.modules.get_all_users.app import get_all_users_presenter
from src.modules.get_user.app import get_user_presenter
from src.modules.update_user.app import update_user_presenter

app = Flask(__name__)
CORS(app)
load_dotenv()

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
    return create_user_presenter.flask_handler(request)

@app.route('/user', methods=['DELETE'])
def delete_user():
    return delete_user_presenter.flask_handler(request)

@app.route('/users', methods=['GET'])
def get_all_users():
    return get_all_users_presenter.flask_handler(request)

@app.route('/user', methods=['GET'])
def get_user():
    return get_user_presenter.flask_handler(request)

@app.route('/user', methods=['PUT'])
def update_user():
    return update_user_presenter.flask_handler(request)


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
