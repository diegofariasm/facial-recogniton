from flask import Flask

def create_app():
    # Muda a pasta onde estão as 'views' de template para views e inicia o aplicativo.
    app = Flask(__name__,
    template_folder='views',
    static_folder='static'
    )
    # Chave secreta do website
    app.config['SECRET_KEY'] = 'reallystrongkey'

    # Registra as rotas que foram definidas em controllers/routes.py.
    from .controllers.routes import routes
    app.register_blueprint(routes)

    return app