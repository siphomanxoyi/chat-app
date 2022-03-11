# called by driverM to have a chatroom for a client-client or client-server chat

#Importing tkinter GUI library
import tkinter as tk
from tkinter import *
#Importing threading features to allow constant checking for new messages
import threading
#Importing client/server file methods
import client

from log_util import dated_message
from ip_util import ip
from message_util import create_ping_message
from protocol_util import send_message
from protocol_util import sort_messages_in

#Importing variables for client usernames
from home_gui import tempUser
from home_gui import tempChatUser

#Main tk display with specific window size
root = Tk()
root.geometry('500x600')

#Messages frame creation and display
messFrame = tk.Frame(root, bg="white")
messFrame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.05)
#Menu frame creation and display
menuFrame = tk.Frame(root, bg="white")
menuFrame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.7)


#Scrollbar for message frame
v = Scrollbar(messFrame)
v.pack(side=RIGHT, fill=Y)
#Text box to hold messages
tex = Text(messFrame, width=480, height=580, wrap=WORD, yscrollcommand=v.set, fg="black")
v.config(command=tex.yview) #Final scrollbar configuration
tex.tag_config("rec", background="lightblue") #Text box message colors' control
tex.tag_config("sent", background="lightgreen", justify="right")

#Testing receiving messages display:
##Recieved message display
#def display_message(rMess):
#    tex.insert("end", (dated_message(rMess) + "\n"), "rec")
#    tex.pack(side=TOP, fill=X)
#
##Test example function call for received message
#display_message("This is a pretty long message. This is a pretty long message. This is a pretty long message. This is a pretty long message.")

#Label to tell you who you are talking to
cuLabel = Label(root, text = "Chatting to: " + tempChatUser)
cuLabel.pack()

#Message input field
e = Entry(menuFrame)
e.pack()

#Function to display a sent message to the screen
def send_a_message():
    global e
    messBody = e.get()
    if(messBody==""):
        alert("Please input a message.")
    else:
        #Sending message from client
        newMessage = create_ping_message(tempUser, tempChatUser)
        send_message(newMessage)
        #Sent message display
        tex.insert("end", dated_message(messBody) + "\n", "sent") #Displaying sent message to screen
        tex.pack(side=TOP, fill=X)
        e.delete(0,END) #Clearing input field
        e.pack()

#Function to display an alert
def alert(message):
    global alertBox
    alertBox['text']="" #Clearing alert label
    alertBox['text']=message #Showing message status alert
    alertBox.pack()

#Send button creation and display
sendButton = Button(menuFrame, text="Send", fg="white", bg="green", command=send_a_message)
sendButton.pack()

#Disconnecting and ending the session
def log_out():
    #disCon = create_disconnect_message(tempUser,tempChatUser)
    global root
    root.destroy()

#Send button creation and display
logoutButton = Button(menuFrame, text="Log Out", fg="white", bg="green", command=log_out)
logoutButton.pack()

#Program feedback will be shown in this label
alertBox = Label(menuFrame, text="", fg="white", bg="grey")

#Main functionality function, starts the program
def driveM():
    #Run command
    global root
    root.mainloop()