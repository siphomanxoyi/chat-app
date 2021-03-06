# user name choice and choosing who to chat with happen in this GUI
# thanks to https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
#  for showing how to move between pages

# importing GUI elements
import tkinter as tk
from tkinter import ttk
from tkinter import *
# importing client/server file methods
import client

# default host client and contacted client or server names
tempUser = "Default"
tempChatUser = "Server"

# a method to set tempUser to a new username
def newUser(user):
    global tempUser
    tempUser = user

# multi page setup
class home(tk.Tk):
     
    # __init__ function for class home
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        # configuring container size
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (signup, online):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # signup and online pages respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        # the frame to show when the program opens
        self.show_frame(signup)

        # program feedback will be shown in this label
        global alertBox
        alertBox = Label(self, text="", fg="white", bg="grey")
        alertBox.pack(side=BOTTOM)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# function to display an alert
def alert(message):
    global alertBox
    alertBox['text']="" #Clearing alert label
    alertBox['text']=message #Showing message status alert
    alertBox.pack()
  
# first window frame signup
  
class signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # heading label
        labelChoo = ttk.Label(self, text ="Choose a  username:")
        labelChoo.pack()

        # name input field
        ent = Entry(self)
        ent.pack()

        # function to add a new client to address book
        def new_client():
            usernameStored = ent.get()
            if usernameStored != "":
                labelConf['text'] = ("Welcome " + usernameStored.upper())
                newUser(usernameStored)
                ent.delete(0,END) #Clearing input field
                ent.pack()
                show_button()
                client.set_username(tempUser)
                client.setup()
                if (client.connect_to_server()):
                    alert("Connected to server successfully.")
                else:
                    alert("Failed to connect to server.")
            else:
                alert("Please input a username")

        # button to sign up to the address book as a client
        buttonSign = ttk.Button(self, text ="Sign Up",
        command = new_client)
        buttonSign.pack()

        # label to confirm temporary account created
        labelConf = ttk.Label(self, text ="")
        labelConf.pack_forget()

        # button to navigate to online list page
        buttonNav = ttk.Button(self, text ="Online",
        command = lambda : controller.show_frame(online))
        buttonNav.pack_forget()

        # showing online list page button and hiding regestration fields
        def show_button():
            labelConf.pack()
            buttonNav.pack()
            labelChoo.pack_forget()
            ent.pack_forget()
            buttonSign.pack_forget()

# second window frame online

class online(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # opens messaging_gui
        def open_messaging():
            exec(open("driverM.py").read())

        # clears users list when refreshing
        def clear(): 
            onlineUsers.delete('1.0',END)
            onlineUsers.pack()

        # heading label
        onLabel = ttk.Label(self, text ="Online List:")
        onLabel.pack()

        # adding a text field to hold online users with a scrollbar
        v = Scrollbar(self)
        v.pack(side=RIGHT, fill=Y)
        onlineUsers = Text(self,  yscrollcommand=v.set, state=DISABLED, width=30, height=20, wrap=WORD)
        v.config(command=onlineUsers.yview)
        onlineUsers.pack()

        # looping through online list to display a button for each
        def get_online():
            import address_book_util
            onlineUsers['state'] = NORMAL
            clear()
            if(client.fetch_users()):
                    for user in address_book_util.address_book:
                        if(user != tempUser.upper()):
                            onlineUsers.insert("end",">>" + user + "\n")
                    alert("Fetched online users successfully.")
            else:
                alert("Failed to fetch online users.")
            onlineUsers['state'] = DISABLED

        # input field for user to choose who to chat with
        chosenUser = Entry(self)
        chosenUser.pack()

        # opens messaging_gui for chosen user communication
        def choose_peer():
            chosen = chosenUser.get()
            if (chosen == ""):
                alert("Please pick a user.")
            elif(onlineUsers.search(">>" + chosen.upper(), "0.0") == ""):
                alert("Please pick a valid online user.")
            else:
                global tempChatUser
                tempChatUser = chosen
                open_messaging()

        # button to refresh online list
        buttonReturn = ttk.Button(self, text = "Refresh",
                        command = get_online)
        buttonReturn.pack(side=BOTTOM)

        # button to open messaging_gui
        messButton = ttk.Button(self, text = "Connect", command=choose_peer)
        messButton.pack(side=BOTTOM)

#Disconnecting and ending the session
def log_out_all():
    #disCon = create_disconnect_message(tempUser,tempChatUser)
    global app
    app.destroy()


def drive():
    # driver Code
    global app
    app = home()
    app.mainloop()