from cgitb import text
from email import message
from fileinput import filename
import secrets
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from urllib import robotparser

from PIL import Image, ImageTk
import os
from numpy import blackman
from stegano import lsb  # pip install stegano

root = Tk()
root.title("Steganography")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#23395d")


def openImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetype=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"),
                                                     ("All file", "*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def saveImage():
    secret.save("image.png")

def hideData():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def showData():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

# frame1
frame1 = Frame(root, bd=3, bg="black", width=330, height=280, relief=GROOVE)
frame1.place(x=10, y=100)

lbl=Label(frame1,bg="black")
lbl.place(x=40,y=10)

# frame2
frame2 = Frame(root, bd=3, bg="white", width=330, height=280, relief=GROOVE)
frame2.place(x=360, y=100)

# text
text1 = Text(frame2, font="Robot 11", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=310, height=280)

# scrollbar
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=310, y=0, height=280, width=20)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# frame3
frame3 = Frame(root, bd=3, bg="#23395d", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=385)

Label(frame3, text="Image", width=5, height=1, bg="#23395d",
      fg="yellow", font="arial 12 bold").place(x=0, y=0)
Button(frame3, text="Open Image", width=12, height=2,
       font="arial 12 bold", command=openImage).place(x=20, y=30)
Button(frame3, text="Save Image", width=12, height=2,
       font="arial 12 bold", command=saveImage).place(x=175, y=30)

# frame4
frame4 = Frame(root, bd=3, bg="#23395d", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=385)

Label(frame4, text="Data", width=5, height=1, bg="#23395d",
      fg="yellow", font="arial 12 bold").place(x=0, y=0)
Button(frame4, text="Hide Data", width=12, height=2,
       font="arial 12 bold", command=hideData).place(x=20, y=30)
Button(frame4, text="Show Data", width=12, height=2,
       font="arial 12 bold", command=showData).place(x=175, y=30)


root.mainloop()
