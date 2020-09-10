"""
program: PyTextEditor.py
This program is a very simple text editor written entirely in python using
built-in librarys. This program uses tkinkter for the graphical interfacing
"""

############################COMMAND DEFINITIONS###########################
def NEW(): #Create New Text
    textbox_text.delete("1.0",tk.END)
def OPEN(): #Open Text File
    f = open("TextFile.txt", "r")
    text = f.read()
    textbox_text.insert("1.0",text)
def SAVE(): #Save Text File
    text = textbox_text.get("1.0",tk.END)
    f = open("TextFile.txt","w")
    f.write(text)
    f.close()
def EXIT(): #Exit Application
    window.destroy()
##########################################################################

#import classes
import tkinter as tk

#Create Window
window = tk.Tk()
window.title("PyTextEditor") #set title of window

#Create Frame for Toolbar
frame_toolbar = tk.Frame()
frame_buttonbar = tk.Frame()

#Create buttons for Toolbar
buttonNew = tk.Button(master=frame_buttonbar, text="New", relief=tk.RAISED, command=NEW)
buttonOpen = tk.Button(master=frame_buttonbar, text="Open", relief = tk.RAISED, command=OPEN)
buttonSave = tk.Button(master=frame_buttonbar, text="Save", relief=tk.RAISED, command=SAVE)
buttonExit = tk.Button(master=frame_buttonbar, text="Exit", relief=tk.RAISED, command=EXIT)


#add buttons to toolbar
buttonNew.pack(side=tk.LEFT,padx=3,pady=1)
buttonSave.pack(side=tk.LEFT,padx=3,pady=1)
buttonOpen.pack(side=tk.LEFT,padx=3,pady=1)
buttonExit.pack(side=tk.LEFT,padx=3,pady=1)

#Create Frame for Text Field
frame_text = tk.Frame()
textbox_text = tk.Text(master=frame_text)
textbox_text.pack(fill=tk.BOTH,expand=True)


#Display Frames
frame_toolbar.pack(side=tk.TOP)
frame_buttonbar.pack(anchor="nw")
frame_text.pack(fill=tk.BOTH,expand=True)



#Run Process
window.mainloop()
