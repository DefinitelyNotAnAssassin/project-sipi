from flask import Flask
from .library.routes import library
from .chat.routes import chat
from .extensions import db,  bcrypt, login, socketio
from .api.library_api import library_api
from .api.chat_api import chat_api
from .models.chat import user
from .user.routes import user_route
from .api.login_api import login_api
from .api.socket_api import socket_api
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "dakflksd foi!5aweoB"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_BINDS"] = {
        'chat': "sqlite:///chat.sqlite3",
        "library": "sqlite:///library.sqlite3"
    }
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)
    socketio.init_app(app)
    login.blueprint_login_views = {
        'chat': '/login',
        'library': '/login'
    }

    with app.app_context():
        db.create_all()
    app.register_blueprint(library)
    app.register_blueprint(chat)
    app.register_blueprint(library_api)
    app.register_blueprint(chat_api)
    app.register_blueprint(user_route)
    app.register_blueprint(login_api)
    app.register_blueprint(socket_api)
    return app