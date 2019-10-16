#!/usr/bin/python
from appJar import gui

# create a function called press which takes a button for input
# This function is called when an event happens
def press(button):
  if button == "Cancel":
    app.stop()
  else:
    usr = app.getEntry("Username")
    pwd = app.getEntry("Password")
    print("User:", usr, "Pass:", pwd)

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

app.go()
