from .extensions import db, SECRET_KEY
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta


class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    
    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=500),
                'iat': datetime.utcnow(),
                'id': user_id
                }
            return encode(payload,SECRET_KEY,algorithm='HS256')
        except Exception as e:
            return e
        
    @staticmethod        
    def decode_auth_token(auth_token):
        try:
            payload = decode(auth_token, SECRET_KEY)
            return payload['id']
        except ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except InvalidTokenError:
            return 'Invalid token. Please log in again.'