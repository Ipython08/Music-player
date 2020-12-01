from tkinter import *
from tkinter import ttk
import os
import pygame
from tinytag import TinyTag, TinyTagException

temp = TinyTag.get("Unforgettable lyrics - clean.mp3")

win = Tk()
win.title("Music Player")
win["bg"] = "white"
win.geometry("1250x900")
win.resizable(width=False, height=False)
win.iconbitmap(r"favicon.ico")

pygame.mixer.init()

q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")
o = PhotoImage(file="Forward.png")
r = PhotoImage(file="Rewind.png")

def buttonpress(n):
    if n==1:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=575, y=700)# Pause button
        # play/pause with pyaudio will come here
        pygame.mixer.init()
        pygame.mixer.music.load('Unforgettable lyrics - clean.mp3')
        pygame.mixer.music.play(loops=0)

    if n==2:
        Button(win, image=q, borderwidth=0, command=lambda: buttonpress(3)).place(x=575, y=700)
        pygame.mixer.music.pause()
    if n==3:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=575, y=700)
        pygame.mixer.music.unpause()

def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


scale = Scale( from_=100, to=0, orient=VERTICAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.place(x=725,y=655)


Button(win, image=q, borderwidth=0, command=lambda: buttonpress(1)).place(x=575, y=700)# Play button
Button(win, image=o, borderwidth=0).place(x=634, y=700)
Button(win, image=r, borderwidth=0, command=lambda: buttonpress(1)).place(x=516, y=700)


win.mainloop()
#random
