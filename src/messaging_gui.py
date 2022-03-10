#Importing tkinter GUI library
import tkinter as tk
from tkinter import *

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

#Function to display a sent message to the screen
def send_message():
    if(e.get()==""):
        alert("Please input a message.")
    else:
        #Testing sent messages display:
        #tex.insert("end", dated_message(e.get()) + "\n", "sent") #Displaying sent message to screen
        #tex.pack(side=TOP, fill=X)
        e.delete(0,END) #Clearing input field
        e.pack()

#Function to display an alert
def alert(message):
    alertBox['text']="" #Clearing alert label
    alertBox['text']=message #Showing message status alert
    alertBox.pack()

#Send button creation and display
sendButton = Button(menuFrame, text="Send", fg="white", bg="green", command=send_message)
sendButton.pack()

#Program feedback will be shown in this label
alertBox = Label(menuFrame, text="", fg="white", bg="grey")

#Run command
root.mainloop()