from config import app
from flask import request
import jwt
from models import ChatUser as User

def login_required(f):
    def log_in(*args, **kwargs):
        auth = None
        try:
            auth = request.headers['auth_key']
        except Exception as e:
            return {"status": "auth key missing in the header"}, 401
        user_dec = jwt.decode( token, app.config['SECRET_KEY'], algorithms="HS256")
        user = User.objects.filter(username=user_dec['username']).first()
        if not(user):
            return {"status": "Authentication failed"}, 403
        f(*args, **kwargs)
    return log_in
