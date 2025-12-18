import json
from flask import Flask
from src.modules.delete_user.app.delete_user_presenter import flask_handler, lambda_handler
from src.shared.infra.repositories.mock.user_repository_mock import UserRepositoryMock


class MockMultiDict:
    def to_dict(self, flat=True):
        return {}

class MockRequest:
    def __init__(self, json: dict, headers: dict, method: str = 'POST', path: str = '/delete_user'):
        self._json = json
        self.headers = headers
        self.method = method
        self.path = path
        self.args = {}
        self.view_args = {}
        self.files = MockMultiDict()
        self.form = MockMultiDict()

    def get_json(self, silent=False):
        return self._json

class Test_DeleteUserPresenter:

    def setup_method(self, method):
        UserRepositoryMock._initialized = False

    def test_delete_user_flask(self):
        app = Flask(__name__)
        with app.app_context():
            request = MockRequest(
                json={
                    "user_id": "2"
                },
                headers={
                    "Content-Type": "application/json"
                }
            )

            response = flask_handler(request)

            expected = {'user_id': "2",
                        'name': 'Vitor Brancas',
                        'email': 'brancas@brancas.com',
                        'state': 'REJECTED',
                        'message': 'the user was deleted successfully'}

            assert json.loads(response.data) == expected
            assert response.status_code == 200

    def test_delete_user_lambda(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "2"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                    }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"user_id": "2"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        expected = {'user_id': "2",
                     'name': 'Vitor Brancas',
                     'email': 'brancas@brancas.com',
                     'state': 'REJECTED',
                     'message': 'the user was deleted successfully'}

        assert json.loads(response["body"]) == expected
        assert response["statusCode"] == 200
