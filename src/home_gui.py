#Thanks to https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
#  for showing how to move between pages.

import tkinter as tk
from tkinter import ttk
from tkinter import Entry

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
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame signup
  
class signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # heading label
        label = ttk.Label(self, text ="Choose a nickname:")
        label.pack()

        # name input field
        e = Entry(self)
        e.pack()

        # button to navigate to online list page
        button = ttk.Button(self, text ="Online",
        command = lambda : controller.show_frame(online))
        button.pack()
  
          
  
  
# second window frame online
class online(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # heading label
        label = ttk.Label(self, text ="Online")
        label.pack()
  
        # storing list of people online in an array
        numOnline = ["John","James","Jessy","Jane"]
        
        #def chat(user):
            #exec(compile(open("messaging_gui.py").read(), "messaging_gui.py", 'exec'))
            # a function to be built in messaging_gui to take in client ip & port
            #setClient(user)

        # looping through online list to display a button for each
        for user in numOnline:
            button = ttk.Button(self, text =user)#,
            #                command = chat(user))
            button.pack()

        # blank label to add space
        label = ttk.Label(self, text ="")
        label.pack()

        # button to return to signup page
        button = ttk.Button(self, text = "Back to sign up",
                        command = lambda : controller.show_frame(signup))
        button.pack()
  


# driver Code
app = home()
app.mainloop()