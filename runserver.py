from Website.website import create_app


def start():
    # Cria o webserver
    app = create_app()

    # Inicia o webserver
    app.run()


if __name__ == "__main__":
    start()
