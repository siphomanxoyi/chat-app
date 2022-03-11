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


#Recieved message display
def display_message(rMess):
    tex.insert("end", (dated_message(rMess) + "\n"), "rec")
    tex.pack(side=TOP, fill=X)

#Label to tell you who you are
cuLabel = Label(root, text = "YOU ARE: " + tempUser)
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
        if (client.send_text_message(messBody, tempChatUser) == True):
            alert("Message sent successfully.")
            #Sent message display
            tex.insert("end", dated_message(messBody) + "\n", "sent") #Displaying sent message to screen
            tex.pack(side=TOP, fill=X)
        else:
            alert("Message could not be sent")
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
    client.disconnect_from_server()
    from home_gui import log_out_all
    log_out_all()
    global root
    root.destroy()

#Send button creation and display
logoutButton = Button(menuFrame, text="Log Out", fg="white", bg="green", command=log_out)
logoutButton.pack()

#Program feedback will be shown in this label
alertBox = Label(menuFrame, text="", fg="white", bg="grey")

#Constantly checking for new messages
def check_messages():

    while(True): #[0] is the sender and [2] is the message
        messageArr = client.get_next_text_message()
        rMess = messageArr[0] + " | " + messageArr[2]
        if(rMess != ""):
            display_message(rMess)
    

#Main functionality function, starts the program
def driveM():
    incMessThread = threading.Thread(target=check_messages)
    incMessThread.start()
    #Run command
    global root
    root.mainloop()