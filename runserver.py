from Website.website import create_app

def start():
    # Cria o webserver
    app = create_app()
    # Para conseguir usar as funções fora do aplicativo
    app.app_context().push()
    # Inicia o webserver
    app.run()

if __name__ == "__main__":
    start()
