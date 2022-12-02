from flask_sqlalchemy import SQLAlchemy

# Cria a database
database = SQLAlchemy()
DB_NAME = "database.db"


def configue_database(app):
    # Configura qual datanase será usada
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # Seta a database
    database.init_app(app)


def create_database(app):
    with app.app_context():
        database.create_all()
