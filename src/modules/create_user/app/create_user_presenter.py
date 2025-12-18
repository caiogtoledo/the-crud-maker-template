from .create_user_controller import CreateUserController
from .create_user_usecase import CreateUserUsecase
from src.shared.environments import Environment
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse

def flask_handler(request):
    repos = Environment().get_repositories()
    user_repository = repos["user_repo"]
    usecase = CreateUserUsecase(user_repository)
    controller = CreateUserController(usecase)
    
    httpRequest = FlaskHttpRequest(request)
    response = controller(httpRequest)
    httpResponse = FlaskHttpResponse(response)
    
    return httpResponse.to_flask_response()

def lambda_handler(event, context):
    repos = Environment().get_repositories()
    user_repository = repos["user_repo"]
    usecase = CreateUserUsecase(user_repository)
    controller = CreateUserController(usecase)
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
