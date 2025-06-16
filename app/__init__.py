from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "user.login_page"

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register routes
    from app.routes.user_routes import user_bp
    from app.routes.admin_routes import admin_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()

    return app
