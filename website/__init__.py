from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    # Muda a pasta onde estão as 'views' de template para views e inicia o aplicativo.
    app = Flask(
        __name__,
        template_folder="views",
        static_folder="static",
    )

    # Chave secreta do website
    app.config["SECRET_KEY"] = "reallystrongkey"

    from .dao.database import configue_database, create_database

    configue_database(app)
    # É necessário importar os models para que a funcção create_database() saiba que eles existam
    from .models.MAluno import MAluno

    # Cria o arquivo da database
    create_database(app)

    # Registra as rotas que foram definidas em controllers/routes.py.
    from .controllers.routes import routes

    app.register_blueprint(routes)

    # Registra as rotas de autenticação
    from .controllers.auth_routes import auth_routes

    app.register_blueprint(auth_routes)

    # Configura o aplicativo como debug
    app.debug = True
    # Enable toolbar on debug mode
    toolbar = DebugToolbarExtension(app)

    return app
