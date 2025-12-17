from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

from src.shared.infra.routes.user_routes import user_routes

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

app.register_blueprint(user_routes)

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
