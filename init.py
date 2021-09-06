import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

BUTTONHEIGHT='3'
BUTTONWIDTH='44'

screen = tk.Tk()
screen.title("dnf")
screen.geometry("400x300")

def install():
	os.system("xterm -e 'echo what do you want install? && read install && sudo dnf install $install'")

def search():
	os.system("xterm -e 'echo what do you want search? && read search && sudo dnf search $search && read'")

def remove():
	os.system("xterm -e 'echo what do you want remove? && read search && sudo dnf remove $remove'")

def update():
	os.system("xterm -e 'sudo dnf update'")

def main():
	
	buttoninstall = tk.Button(screen, command=install, text='install', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonsearch = tk.Button(screen, command=search, text='search', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonremove = tk.Button(screen, command=remove, text='remove', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	buttonupdate = tk.Button(screen, command=update, text='update', height=BUTTONHEIGHT, width=BUTTONWIDTH)
	
	buttoninstall.place(x='10', y='30')
	buttonsearch.place(x='10', y='95')
	buttonremove.place(x='10', y='160')
	buttonupdate.place(x='10', y='225')
	screen.mainloop()
main()
