from App.models import TokenModel, UserModel
from flask_jwt_extended import get_jwt
from flask_restful import abort


def jwt_is_blacklist(func):
    def wrapper(*args, **kwargs):

        access_token = get_jwt()["jti"]
        token : TokenModel = TokenModel.query.filter_by(token=access_token).first()

        if token:
            abort(401, message="Token is blacklisted")

        return func(*args, **kwargs)
    
    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):

        user_id = kwargs.get("user_id")
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User does not exists")

        return func(*args, **kwargs)
    
    return wrapper