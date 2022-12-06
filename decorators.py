from config import app
from flask import request, abort
import jwt
from models import ChatUser as User
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "auth_key" in request.headers:
            token = request.headers["auth_key"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data=jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user= User.objects.filter(email=data['email']).first()
            if not(current_user):
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
            if not current_user.is_login:
                abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
