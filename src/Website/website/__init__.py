from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

# Muda a pasta onde estão as 'views' de template para views e inicia o aplicativo.
app = Flask(
    __name__,
    template_folder="views",
    static_folder="static",
)

def create_app():

    # Chave secreta do website
    app.config["SECRET_KEY"] = "reallystrongkey"

    from .dao.database import configue_database, create_database
    configue_database(app)

    # É necessário importar os models para que a funcção create_database() saiba que eles existam
    from Website.website.models.MAttendance import MAttendance
    from Website.website.models.MStudent import MStudent
    from Website.website.models.MPicture import MPicture

    # Cria o arquivo da database
    create_database(app)

    # Registra as rotas que foram definidas em controllers/routes.py.
    from Website.website.controllers.routes import routes

    app.register_blueprint(routes)

    # Registra as rotas de autenticação
    from Website.website.controllers.auth_routes import auth_routes

    app.register_blueprint(auth_routes)

    login_manager = LoginManager()
    login_manager.login_view = "auth_routes.login"
    login_manager.login_message = "É necessário estar logado para acessar essa página."
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_student(id):
        return MStudent.query.get(int(id))

    # Configura o aplicativo como debug
    app.debug = True
    # Enable toolbar on debug mode
    toolbar = DebugToolbarExtension(app)
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    return app
