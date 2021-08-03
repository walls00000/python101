# cipherUI.py
########################################################
## TODO:
## Add transposition cipher
## Add Reverse cipher
## Add editor capability to plaintext files
## Add bulk encrypt/decrypte functionality

import PySimpleGUI as sg
import os.path

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabetLength = alphabet.__len__()
defaultFont = "Courier 14"

################### Helper Functions ###################
def contents(filename):
    contents = ""
    with open(filename) as f:
        for line in f:
            contents += line
    return contents

def binaryEncode(ascii_string):
    binary = bin(int.from_bytes(ascii_string.encode(), 'big'))
    return binary

def binaryDecode(binary):
    n = int(binary, 2)
    decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return decoded

def writeFile(newfilename, contents):
    newfile = open(newfilename, "w")
    newfile.write(contents)
    newfile.close()

def encryptFile(arguments):
    newfilename = "{}.enc".format(arguments["file"])
    encrypted = ""
    with open(arguments["file"]) as f:
        contents = f.read()
        if(arguments["bin"] == "DECODE"):
            encrypted = binaryDecode(contents)
        else:
            encrypted = contents
        encrypted = caesar_cipher(encrypted, arguments["key"])
        if(arguments["bin"] == "ENCODE"):
            encrypted = binaryEncode(encrypted)
    return encrypted;

def caesar_cipher(clearText, shiftAmount):
    """ caesar_cipher: Use the caesar cipher to encrypt clearText
    using shiftAmount

    Parameters
    ----------
    clearText: the text string to encrypt
    shiftAmount: the integer shift amount

    Return:
    the encrypted string
    """
    encryptedString = ""

    for currentCharacter in clearText:
        position = alphabet.find(currentCharacter)
        newPosition = (position + shiftAmount) % alphabetLength
        if currentCharacter in alphabet:
            encryptedString = encryptedString + alphabet[newPosition]
        else:
            encryptedString = encryptedString + currentCharacter
    return encryptedString

def setValues(dictionary):
    filename = os.path.join(
        values["-FOLDER-"], values["-FILE LIST-"][0]
    )
    dictionary["file"] = filename
    dictionary["key"] = int(values["-SLIDER-"])
    dictionary["write"] = False
    if values["-BIN_OFF-"]:
        dictionary["bin"] = "OFF"
    elif values["-BIN_ENCODE-"]:
        dictionary["bin"] = "ENCODE"
    elif values["-BIN_DECODE-"]:
        dictionary["bin"] = "DECODE"
    else:
        dictionary["bin"] = "OFF"

################### UI ###################
# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Encrypted Files Folder"),
        sg.In(
            size=(25, 1),
            enable_events=True,
            font=defaultFont,
            text_color="yellow",
            background_color="black",
            key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Refresh", key="-REFRESH-")
    ],
    [
        sg.Listbox(
            values=[],
            enable_events=True,
            size=(50,20),
            text_color="white",
            background_color="black",
            font=defaultFont,
            key="-FILE LIST-"
        )
    ],
    [sg.HSeparator()],
    [sg.Button("Plain Text", key="-PLAIN_TEXT-"),
     sg.Button("Encrypt/Decrypt", key="-ENCRYPT-")],
    [sg.Text("Write Contents To File: "),
     sg.In(
         size=(25, 1),
         enable_events=True,
         text_color="yellow",
         background_color="black",
         font=defaultFont,
         key="-NEW_FILE_NAME-"
     ),
     sg.Button("Write File", key="-WRITE_FILE-")],
    [sg.Text("caesar cipher key")],
    [sg.Slider(
        range=(0-alphabetLength, alphabetLength),
        default_value=0,
        orientation='h',
        size=(50,20),
        key="-SLIDER-"
    )],
    [sg.Radio("binary off", group_id=1, default=True, key="-BIN_OFF-")],
    [sg.Radio("binary encode", group_id=1, key="-BIN_ENCODE-")],
    [sg.Radio("binary decode", group_id=1, key="-BIN_DECODE-")],
]


# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text(
        "Choose a file from list on left:",
        text_color="yellow",
        font=defaultFont,
        key="-CHOSEN_FILENAME-"
    )],
    [sg.Text(size=(60, 2), key="-TOUT-")],
    [sg.HSeparator()],
    [sg.Output(size=(60,40), text_color="white",background_color="black", font=defaultFont, key="-CONTENTS-")],
]

# ------- Full layout -------
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("CipherUI", layout)


## Refresh the folder contents
def refreshFolder():
    folder = values["-FOLDER-"]
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
        file_list.sort()
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
    ]
    window["-FILE LIST-"].update(fnames)



# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        refreshFolder()
    elif event == "-PLAIN_TEXT-":
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        window["-CONTENTS-"].update(contents(filename))
    elif event == "-ENCRYPT-":
        myArgs = {};
        setValues(myArgs)
        encrypted = encryptFile(myArgs)
        window["-TOUT-"].update("{}".format(myArgs))
        window["-CONTENTS-"].update(encrypted)
    elif event == "-WRITE_FILE-":
        myArgs = {};
        setValues(myArgs)
        myArgs["write"] = True
        encrypted = encryptFile(myArgs)
        newfilename = values["-NEW_FILE_NAME-"]
        window["-TOUT-"].update("{}".format(myArgs))
        window["-CONTENTS-"].update(encrypted)
        writeFile(newfilename, encrypted);
        refreshFolder()
    elif event == "-REFRESH-":
        refreshFolder()
    elif event == "-FILE LIST-": # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            newfilename = ""
            if (filename.endswith(".enc")):
                newfilename = os.path.splitext(filename)[0]+'.txt'
            else:
                newfilename = "{}.enc".format(filename)
            window["-NEW_FILE_NAME-"].update(newfilename)
            slider_value = values["-SLIDER-"]
            myArgs = {}
            setValues(myArgs)
            window["-TOUT-"].update("{}".format(myArgs))
            window["-CHOSEN_FILENAME-"].update(filename)
            window["-CONTENTS-"].update(contents(filename))
        except:
            pass

window.close()