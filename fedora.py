import os


def installinstok(text):
	os.system("lxterminal -e 'dnf install "+ text +"'")

def searchtok(text):
	os.system("lxterminal -e 'dnf search " + str(text) + " && read'")
	
def removetok(text):
	os.system("lxterminal -e 'dnf remove " + str(text) + "'")
	
def update():
	os.system("lxterminal -e 'dnf update'")

