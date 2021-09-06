import os


def installinstok(text):
	os.system("lxterminal -e 'apt update && apt install "+ text +"'")

def searchtok(text):
	os.system("lxterminal -e 'apt update && apt search " + str(text) + " && read'")
	
def removetok(text):
	os.system("lxterminal -e 'apt remove " + str(text) + "'")
	
def update():
	os.system("lxterminal -e 'apt update && apt upgrade'")

