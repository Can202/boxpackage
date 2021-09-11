import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys

#distro
import fedora
import debian as distro


BUTTONHEIGHT='3'
#BUTTONWIDTH='44'
BUTTONWIDTH='39'
#TEXTWIDTH=20
TEXTWIDTH=18



def main():
	
	screen = tk.Tk()
	screen.title("BoxPackage")
	screen.geometry("400x400")
	screen.resizable(width = False, height = False)
	screen.grid_columnconfigure(1, weight=1)
	screen.eval('tk::PlaceWindow . center')
	buttoninstall = tk.Button(screen, command=install, text='install', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonsearch = tk.Button(screen, command=search, text='search', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonremove = tk.Button(screen, command=remove, text='remove', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonshow = tk.Button(screen, command=show, text='show details', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonupdate = tk.Button(screen, command=distro.update, text='update', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	
	buttoninstall.grid(row=0, column=1)
	buttonsearch.grid(row=1, column=1)
	buttonremove.grid(row=2, column=1)
	buttonshow.grid(row=3, column=1)
	buttonupdate.grid(row=4, column=1)
	
#	buttoninstall.pack(fill=tk.X)
#	buttonsearch.pack(fill=tk.X)
#	buttonremove.pack(fill=tk.X)
#	buttonshow.pack(fill=tk.X)
#	buttonupdate.pack(fill=tk.X)
	screen.mainloop()

def install():
	instscreen = tk.Tk()
	instscreen.geometry("200x100")
	instscreen.title("program to install?")
	instscreen.resizable(width = False, height = False)
	instscreen.eval('tk::PlaceWindow . center')
	
	entry = ttk.Entry(instscreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(instscreen, command=lambda: distro.installinstok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	instscreen.mainloop()
	
def pathinstall(text):
	
	instscreen = tk.Tk()
	instscreen.geometry("200x100")
	instscreen.title("program to install?")
	instscreen.resizable(width = False, height = False)
	instscreen.eval('tk::PlaceWindow . center')
	
	l = Label(instscreen, text = "Install this package?")
	l.config(font =("Courier", 8))
	l.pack()

	
	instok = tk.Button(instscreen, command=lambda: distro.installinstok(text), text='Install', height=1, width=3)
	instok.place(x=70, y=40)
	
	instscreen.mainloop()


def search():
	searchscreen = tk.Tk()
	searchscreen.geometry("200x100")
	searchscreen.title("program to search?")
	searchscreen.resizable(width = False, height = False)
	searchscreen.eval('tk::PlaceWindow . center')
	
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
	removescreen.eval('tk::PlaceWindow . center')
	
	entry = ttk.Entry(removescreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(removescreen, command=lambda: distro.removetok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	removescreen.mainloop()
def show():
	instscreen = tk.Tk()
	instscreen.geometry("200x100")
	instscreen.title("program to show details?")
	instscreen.resizable(width = False, height = False)
	instscreen.eval('tk::PlaceWindow . center')
	
	entry = ttk.Entry(instscreen, width=TEXTWIDTH)
	entry.place(x=15, y=10)
	
	instok = tk.Button(instscreen, command=lambda: distro.showtok(entry.get()), text='ok', height=1, width=3)
	instok.place(x=70, y=40)
	
	instscreen.mainloop()

if len(sys.argv) > 1:
	
	program = sys.argv[1]
	
	pathinstall(program)

main()



