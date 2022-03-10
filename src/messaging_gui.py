# called by driverM to have a chatroom for a client-client or client-server chat

#Importing tkinter GUI library
import tkinter as tk
from tkinter import *
#Importing threading features to allow constant checking for new messages
import threading
#Importing client/server file methods
import client

from log_util import dated_message
from address_book_util import add_to_address_book
from ip_util import ip
from message_util import create_ping_message
from message_util import create_connect_message
from message_util import create_disconnect_message
from protocol_util import process_message_out
from protocol_util import process_message_in
from protocol_util import send_message
from protocol_util import receive_message

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

#Message input field
e = Entry(menuFrame)
e.pack()

#Function to constantly check for new incoming messages
def checkForNew():
    while True:
        recMess = receive_message()
        if recMess != "":
            #Received message display
            tex.insert("end", dated_message(recMess) + "\n", "sent") #Displaying received message to screen
            tex.pack(side=TOP, fill=X)

#function to connect to other client and call checkForNew
def connect():
    connectionMessage = create_connect_message(tempUser, tempChatUser)
    process_message_out(connectionMessage)
    send_message(connectionMessage)
    checkingThread = threading.Thread(target=checkForNew)
    checkingThread.start()

#Function to display a sent message to the screen
def send_a_message():
    global e
    messBody = e.get()
    if(messBody==""):
        alert("Please input a message.")
    else:
        #Sending message from client
        newMessage = create_ping_message(tempUser, tempChatUser)
        process_message_out(newMessage)
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
    #Create a client
    client.username = tempUser
    client.main()
    add_to_address_book(tempUser, ip)
    connect()
    #Run command
    global root
    root.mainloop()