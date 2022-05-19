from numpy import full
from file import Files
import pandas as pd
import shutil
import pathlib
import os

class Reader:
    def __init__(self,data:Files) -> None:
        self.data = data
        self.processed_path = pathlib.Path(__file__).parent.resolve().joinpath("processed")
        self.not_aplicable_path = pathlib.Path(__file__).parent.resolve().joinpath("notAplicable")
        self.this_path = pathlib.Path(__file__).parent.resolve().joinpath("concat")
        self.msg = ""
    
    def evaluate_files(self):
        output_file= pd.DataFrame()
        for f in self.data.get_files():
            print("reading file... ",f)
            full_path = self.data.get_path()+"/"+f
            if str(f).endswith((".xlsx",".xls",".xlsm")):
                self.data.insert_processed(full_path)
                try:
                    # copy file into dir
                    shutil.copy(full_path, self.processed_path)
                    print("File saved at ",self.processed_path)
                    # all datasheets from current file
                    # df = pd.read_excel(full_path, sheet_name=None)
                    # cdf = pd.concat(df.values())
                    conc = pd.concat(pd.read_excel(full_path, sheet_name=None), ignore_index=True)
                    output_file = pd.concat([output_file,conc],ignore_index=True)
                    # print(full_path)
                    # break
                except Exception as e:
                    self.msg = "An error ocurred"
                    print("error to save file: ",f)
                    print(str(e))
            else:
                self.data.insert_not_supported(full_path)
                try:
                    shutil.copy(full_path, self.not_aplicable_path)
                    print("File saved at ",self.not_aplicable_path)
                except:
                    self.msg = "An error ocurred"
                    print("error to save file: ",f)
        try:
            output_file.to_excel(str(self.this_path)+"/out.xlsx")
            print("File saved at ",self.this_path)
            self.msg = str("File saved at "+str(self.this_path))
        except Exception as e:
            self.msg = "An error ocurred"
            print("Error generating output file\n",e)

    def check_folders(self):
        CHECK_FOLDER = os.path.isdir(self.this_path)
        if not CHECK_FOLDER:
            os.makedirs(self.this_path)
        CHECK_FOLDER = os.path.isdir(self.processed_path)
        if not CHECK_FOLDER:
            os.makedirs(self.processed_path)
        CHECK_FOLDER = os.path.isdir(self.not_aplicable_path)
        if not CHECK_FOLDER:
            os.makedirs(self.not_aplicable_path)