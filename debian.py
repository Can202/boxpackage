import os


def installinstok(text):
	os.system("lxterminal -e 'apt update && apt install -y "+ text +" && read'")

def searchtok(text):
	os.system("lxterminal -e 'apt update && apt search " + str(text) + " && read'")
	
def removetok(text):
	os.system("lxterminal -e 'apt remove " + str(text) + "'")
	
def showtok(text):
	os.system("lxterminal -e 'apt show " + str(text) + " && read'")
	
def update():
	os.system("lxterminal -e 'apt update && apt upgrade'")

