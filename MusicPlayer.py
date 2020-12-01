from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
import os
import tkinter
import pygame
from tinytag import TinyTag, TinyTagException

a=0

win = Tk()
win.title("Music Player")
win["bg"] = "white"
win.geometry("1250x900")
win.resizable(width=False, height=False)
win.iconbitmap(r"favicon.ico")

pygame.mixer.init()

menubar = Menu(win)
win.config(menu=menubar)

def light():
    win["bg"] = "white"

def dark():
    win["bg"] = "#696969"

# Create the submenu

def about():
    tkinter.messagebox.showinfo("About us","This is an unnamed music player that is still in development made by Ishanth Rajesh and Sharan Senthil")
def openfile():
    global file
    file = filedialog.askopenfilename()
    
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open",command=openfile)
subMenu.add_command(label="Exit",command=win.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Modes", menu=subMenu)
subMenu.add_command(label="Light",command=light)
subMenu.add_command(label="Dark",command=dark)


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us",command=about)

q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")
o = PhotoImage(file="Forward.png")
r = PhotoImage(file="Rewind.png")
m=PhotoImage(file="Resume.png")

def buttonpress(n):
    
    if n==1:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=515.5, y=641)# Pause button
        # play/pause with pyaudio will come here
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loops=0)

    if n==2:
                    
        Button(win, image=m, borderwidth=0, command=lambda: buttonpress(3)).place(x=515.5, y=641)
        pygame.mixer.music.pause()
    if n==3:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=515.5, y=641)
        pygame.mixer.music.unpause()

def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


scale = Scale( from_=100, to=0, orient=VERTICAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.place(x=725,y=655)


Button(win, image=m, borderwidth=0, command=lambda: buttonpress(1)).place(x=515.5, y=641)# Play button
Button(win, image=o, borderwidth=0).place(x=574.5, y=700)
Button(win, image=q, borderwidth=0, command=lambda: buttonpress(1)).place(x=574.5, y=641)
Button(win, image=r, borderwidth=0).place(x=516, y=700)


win.mainloop()
