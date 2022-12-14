from Website.website import create_app
from Recognition.recognition import FaceRecognition
import threading
def start():
    # Cria o reconhecedor
    fr = FaceRecognition()
    # Cria o webserver
    
    # Inicia o webserver
    app = create_app()
    threading.Thread(
                target=app.run()
            ).start()
    
    # Inicia o reconhecedor
    threading.Thread(
                target=fr.run_recognition()
            ).join()
    

if __name__ == "__main__":
    start()
