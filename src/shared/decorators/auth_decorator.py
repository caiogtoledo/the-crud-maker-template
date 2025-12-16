import jwt
from functools import wraps
from flask import request, jsonify
import os


def authenticate(secret_key=None):
    """
    Decorator to protect protected routes
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({'message': 'Authorization header is missing'}), 401
            
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Invalid token format'}), 401
            
            key = secret_key or os.getenv('JWT_SECRET', 'jwt_secret')
            
            try:
                payload = jwt.decode(token, key, algorithms=['HS256'])
                request.user = payload
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator