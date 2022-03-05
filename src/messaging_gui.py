#Importing tkinter GUI library
import tkinter as tk
from tkinter import *
#Importing datetime for message timing
from datetime import datetime

#Main tk display with specific window size
root = Tk()
root.geometry('500x350')

#Messages frame creation and display
messFrame = tk.Frame(root, bg="white")
messFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.05)
#Menu frame creation and display
menuFrame = tk.Frame(root, bg="white")
menuFrame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.7)

#Function to return current date and time
def dati():
    datiFull = datetime.now()
    datiForm = datiFull.strftime("%d/%m/%Y %H:%M:%S")
    return datiForm

#Recieved message label creation and display
def displayMessage(sender, rMess):

    whoSent = Label(messFrame, text=sender)
    receivedMessage = Label(messFrame, text=rMess, fg="white", bg="lightblue", wraplength=260)
    timeRec = Label(messFrame, text=dati())
    space = Label(messFrame, text="                   ", bg="white")
    whoSent.pack()
    receivedMessage.pack()
    timeRec.pack()
    space.pack()

#Test example function call for received message
displayMessage("Them","This is a pretty long message. This is a pretty long message. This is a pretty long message. This is a pretty long message.")

#Function to display a sent message to the screen
def sendMessage():
    sentMessage = Label(messFrame, text=e.get(), fg="white", bg="lightgreen", wraplength=260)
    timeSent = Label(messFrame, text=dati())
    space = Label(messFrame, text="                   ", bg="white")
    sentMessage.pack()
    timeSent.pack()
    space.pack()

#Message input field
e = Entry(menuFrame)
e.pack()

#Send button functionality
def send():
    alertBox['text']=""
    sendMessage()
    alertBox['text']="Message sent successfully."
    alertBox.pack()

#Send button creation and display
sendButton = Button(menuFrame, text="Send", fg="white", bg="green", command=send)
sendButton.pack()

#Program feedback will be shown in this label
alertBox = Label(menuFrame, text="", fg="white", bg="grey")

#Run command
root.mainloop()