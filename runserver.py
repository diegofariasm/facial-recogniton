from Website.website import create_app
from Recognition.recognition import FaceRecognition
import threading
def start():
    # Cria o reconhecedor
    fr = FaceRecognition()
    # Cria o webserver
    app = create_app()
    
    # Inicia o webserver
    app.run()
    
    # Inicia o reconhecedor
   
    

if __name__ == "__main__":
    start()
