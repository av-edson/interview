from genericpath import isfile
from importlib.resources import path
from ntpath import join
import os
import PySimpleGUI as sg
from file import Files
from reader import Reader


sg.theme('SystemDefault1')   
# first column
firstLayout = [  [sg.Text('Welcome to Edson\'s Dev Test')],
            [sg.Text('Enter Source path'), 
                sg.In(size=(25,1),enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(),
                ],
            # [sg.Text(key="-OUTTEXT-")],
            [sg.Button('Run'), sg.Button('Close')],
            [sg.Text('Everyting is ok',key="-msg-")] ]
# second column
secondLayout = [[sg.Text('Files Found')],
                    [sg.Listbox(values=[],enable_events=True,size=(30,10),key="-FILE LIST-")]]
# all layout
layout = [[sg.Column(firstLayout),sg.VerticalSeparator(),sg.Column(secondLayout)]]
# Create the Window

class Window:
    def __init__(self) -> None:
        pass
    def start(self):
        window = sg.Window('Edson\'s dev test', layout)
        current_window = Files()
        reader = Reader(current_window)
        reader.check_folders()
        while True:
            event, values = window.read()
            # close button
            if event == sg.WIN_CLOSED or event == 'Close': 
                break
            if event == "-FOLDER-":
                current_window.clean_files()
                folder = values["-FOLDER-"]
                current_window.set_path(str(folder))
                try:
                    files = os.listdir(folder)
                except:
                    print("An error ocurred")
                    files = []
                file_names = [
                    f
                    for f in files
                    if os.path.isfile(os.path.join(folder, f))
                ]
                current_window.set_files(file_names)
                window["-FILE LIST-"].update(file_names)
                window['-msg-'].update("Files loaded")
            if event=="Run":
                reader.evaluate_files()
                window['-msg-'].update(reader.msg)

        window.close()