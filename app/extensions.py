from dynaconf import FlaskDynaconf
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
jwt = JWTManager()


def init_app(app):
    FlaskDynaconf(app)
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    Migrate(app, db)
    CORS(app)

    from app.models import Category, Product, User, UserAdmin

    @app.shell_context_processor
    def context_processor():

        return dict(
            app=app,
            db=db,
            User=User,
            UserAdmin=UserAdmin,
            Product=Product,
            Category=Category,
        )
