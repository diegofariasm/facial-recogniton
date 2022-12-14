from ..models.MPicture import MPicture
from ..dao.DPicture import DPicture
class CPicture:
    
    @staticmethod
    def save_photo(file_name, file_data, student_id):
        picture = MPicture(file_name=file_name, file_data=file_data, student_id=student_id)
        DPicture.save_photo(picture)
        
        