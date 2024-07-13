from .extensions import os

class Path:
    def __init__(self):
        self.file_uploads = os.path.join(os.getcwd(), "temp")
        
    def set_file_uploads(self, new_path):
        self.file_uploads =  os.path.join(os.getcwd(), new_path)