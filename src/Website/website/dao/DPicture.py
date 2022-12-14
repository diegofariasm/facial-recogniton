from ..models.MPicture import MPicture
from .database import database

class DPicture():

    @staticmethod
    def save_photo(MPicture):
        database.session.add(MPicture)
        database.session.commit()
    def get_all_photos():
        images = MPicture.query.all()
        
        return images
                
    