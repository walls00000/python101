# cipherUI.py

import PySimpleGUI as sg
import os.path
################### Helper Functions
def contents(filename):
    contents = ""
    with open(filename) as f:
        for line in f:
            contents += line
    return contents

################### UI
# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Encrypted Files Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
        )
    ],
]

control_column = [
    [sg.Text("caesar cipher key")],
    [sg.Slider(range=(-26,26), default_value=0, orientation='v', size=(15,20), key="-SLIDER-")],
    [sg.Radio("binary off", group_id=1, default=True, key="-BIN_OFF-")],
    [sg.Radio("binary encode", group_id=1, key="-BIN_ENCODE-")],
    [sg.Radio("binary decode", group_id=1, key="-BIN_DECODE-")],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose a file from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text(size=(40,20), key="-CONTENTS-")],
]

# ------- Full layout -------
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(control_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("CipherUI", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-": # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            slider_value = values["-SLIDER-"]
            myArgs = {}
            if values["-BIN_OFF-"]:
                myArgs["bin"] = "OFF"
            elif values["-BIN_ENCODE-"]:
                myArgs["bin"] = "ENCODE"
            elif values["-BIN_DECODE-"]:
                myArgs["bin"] = "DECODE"
            else:
                myArgs["bin"] = "OFF"
            window["-TOUT-"].update("{} key={} bin={}".format(filename, slider_value, myArgs["bin"]))
            window["-CONTENTS-"].update(contents(filename))
        except:
            pass

window.close()