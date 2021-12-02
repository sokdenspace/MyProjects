# pip install tk-tools

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("800x600")
window.title("GUI")

# set icon to application
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")

# keep window open
window.mainloop()