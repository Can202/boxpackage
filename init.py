import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

#distro
import fedora
import debian as distro


BUTTONHEIGHT='3'
#BUTTONWIDTH='44'
BUTTONWIDTH='39'
#TEXTWIDTH=20
TEXTWIDTH=18

screen = tk.Tk()
screen.title("Install")
screen.geometry("400x300")
screen.resizable(width = False, height = False)

def install():
	instscreen = tk.Tk()
	instscreen.geometry("200x100")
	instscreen.title("program to install?")
	instscreen.resizable(width = False, height = False)
	
	entry = ttk.Entry(instscreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(instscreen, command=lambda: distro.installinstok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	instscreen.mainloop()


def search():
	searchscreen = tk.Tk()
	searchscreen.geometry("200x100")
	searchscreen.title("program to search?")
	searchscreen.resizable(width = False, height = False)
	
	entry = ttk.Entry(searchscreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(searchscreen, command=lambda: distro.searchtok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	searchscreen.mainloop()
	
def remove():
	removescreen = tk.Tk()
	removescreen.geometry("200x100")
	removescreen.title("program to remove?")
	removescreen.resizable(width = False, height = False)
	
	entry = ttk.Entry(removescreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(removescreen, command=lambda: distro.removetok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	removescreen.mainloop()
def main():
	
	buttoninstall = tk.Button(screen, command=install, text='install', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonsearch = tk.Button(screen, command=search, text='search', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonremove = tk.Button(screen, command=remove, text='remove', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonupdate = tk.Button(screen, command=distro.update, text='update', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	
	buttoninstall.place(x='10', y='30')
	buttonsearch.place(x='10', y='95')
	buttonremove.place(x='10', y='160')
	buttonupdate.place(x='10', y='225')
	screen.mainloop()
main()
