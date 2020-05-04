import os 
from flask import Flask 

from web_app.models_data.models import db, migrate

from web_app.routes.rte_admin   import admin_routes
from web_app.routes.rte_general import general_routes

# Database URI
DATABASE_URI = os.environ.get('DATABASE_URI')
SECRET_KEY   = os.environ.get('FL_APP_SECRET_KEY')

def create_app():
    app = Flask(__name__)

    # Set secret key to encrypt client side data
    app.config["SECRET_KEY"] = SECRET_KEY

    # Configure database information
    app.config["SQLALCHEMY_DATABASE_URI"]        = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database and database migration objects
    db.init_app(app)
    migrate.init_app(app, db)

    # Register route handlers
    app.register_blueprint(admin_routes)
    app.register_blueprint(general_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
