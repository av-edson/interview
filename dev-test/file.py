

class Files:
    def __init__(self) -> None:
        self.file_values = []
        self.processed_files=[]
        self.not_aplicable_files=[]
        self.path = ""
        self.sav_path=""

    def set_files(self,files):
        self.file_values = files
    
    def clean_files(self):
        self.file_values=[]
        self.processed_files=[]
        self.not_aplicable_files=[]
    
    def set_path(self,path):
        self.path = path
    def set_save_path(self,path):
        self.sav_path = path
    def get_save_path(self):
        return self.sav_path  
    def get_path(self):
        return self.path  

    def get_files(self):
        return self.file_values

    def insert_processed(self,file):
        self.processed_files.append(str(file))

    def insert_not_supported(self,file):
        self.not_aplicable_files.append(str(file))