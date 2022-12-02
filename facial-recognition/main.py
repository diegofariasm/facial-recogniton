from website import create_app

if __name__ == '__main__':
    # Cria o webserver
    app = create_app()

    # Inicia o webserver
    app.run()
