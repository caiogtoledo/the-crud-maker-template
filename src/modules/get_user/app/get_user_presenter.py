from .get_user_controller import GetUserController
from .get_user_usecase import GetUserUsecase
from src.shared.environments import Environment
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse


repos = Environment().get_repositories()
user_repository = repos["user_repo"]

usecase = GetUserUsecase(user_repository)
controller = GetUserController(usecase)

def flask_handler(request):
    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    httpResponse = FlaskHttpResponse(response)
    
    return httpResponse.to_flask_response()

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

