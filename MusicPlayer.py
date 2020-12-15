from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame
from mutagen.mp3 import MP3

audio = MP3(
    "C:/1 Files and Folders/SHARAN/Python/SVE atom/Code/Music-player-main/Music player/Undertale - Megalovania.mp3")
# print(int(audio.info.length))
a = 0

x = 0
win = Tk()
win.title("Music Player")
win["bg"] = "white"
win.geometry("1250x900")
win.resizable(width=False, height=False)
win.iconbitmap("favicon.ico")

pygame.mixer.init()

menubar = Menu(win)
win.config(menu=menubar)


class Popup(Toplevel):
    def __init__(self, title='', message='', master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title(title)

        lbl = Label(self, text=message, font=('bold', 14))
        lbl.pack()
        btn = ttk.Button(self, text="OK", command=self.destroy)
        btn.pack()

        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)


def light():
    win["bg"] = "white"


def dark():
    win["bg"] = "#3E3D3D"


# Create the submenu

def about():
    Popup("About Music Player", "Powered By Python \n Version 1.1")


def openfile():
    global file
    file = filedialog.askopenfilename()
    List1.insert(END, file)


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=openfile)
subMenu.add_command(label="Exit", command=win.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Theme", menu=subMenu)
subMenu.add_command(label="Light", command=light)
subMenu.add_command(label="Dark", command=dark)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about)

List1 = Listbox(win, bg="dark grey", fg="black", width=60)  # Listbox creation here
List1.place(x=60, y=60)

q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")
o = PhotoImage(file="Forward.png")
r = PhotoImage(file="Rewind.png")


def buttonpress(n):
    if n == 1:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=575, y=700)  # Pause button
        # play/pause with pyaudio will come here
        current = List1.get(0)
        pygame.mixer.init()
        pygame.mixer.music.load(current)
        pygame.mixer.music.play(loops=0)
        Button(win, image=r, borderwidth=0, command=lambda: buttonpress(808)).place(x=516, y=700)
    if n == 2:
        Button(win, image=q, borderwidth=0, command=lambda: buttonpress(3)).place(x=575, y=700)
        pygame.mixer.music.pause()
    if n == 3:
        Button(win, image=t, borderwidth=0, command=lambda: buttonpress(2)).place(x=575, y=700)
        pygame.mixer.music.unpause()


def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


scale = Scale(from_=100, to=0, orient=VERTICAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.place(x=725, y=655)

Button(win, image=q, borderwidth=0, command=lambda: buttonpress(1)).place(x=575, y=700)  # Play button
Button(win, image=o, borderwidth=0, command=lambda: buttonpress(x + 4)).place(x=634, y=700)
Button(win, image=r, borderwidth=0, command=lambda: buttonpress(808)).place(x=516, y=700)

win.mainloop()
