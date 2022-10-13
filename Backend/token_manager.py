from flask import request, jsonify
from jwt import decode
from functools import wraps, partial, WRAPPER_ASSIGNMENTS
from .extensions import SECRET_KEY
from .models import User

try:
    wraps(partial(wraps))(wraps)
except AttributeError:
    @wraps(wraps)
    def wraps(obj, attr_names=WRAPPER_ASSIGNMENTS, wraps=wraps):
        return wraps(obj, assigned=(name for name in attr_names if hasattr(obj, name))) 
    
# def encode_auth_token():
def token_required(func):
    @wraps
    def token_validator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = decode(token,SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})
    
        return func(current_user, *args, **kwargs)
    return token_validator