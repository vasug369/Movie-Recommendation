import serial
import time
from tkinter import *


def turn_on(sr):
	sr.write(b'o')

def turn_off(sr):
	sr.write(b'x')


def main(sr):
	root=Tk()
	root.geometry("350x350")
	root.title("control led ")
	b1=Button(root,text="turn on",font="chillar 12 bold",command=lambda:turn_on(sr))
	b1.place(x=0,y=0)

	b2=Button(root,text="turn off",font="chillar 12 bold",command=lambda:turn_off(sr))
	b2.place(x=0,y=50)

	root.mainloop()

if __name__=="__main__":
	sr=serial.Serial("COM3",baudrate=9600,timeout=1)

	time.sleep(3)
	main(sr)