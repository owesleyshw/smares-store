from flask_restful import Api

from app.resources import auth


def init_app(app):
    api = Api(app, prefix="/api")
    api.add_resource(auth.Login, "/auth/login")
    api.add_resource(auth.Register, "/auth/register")
    api.add_resource(auth.ForgetPassword, "/auth/forget-password")
