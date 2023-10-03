from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb #pip install stegano


root=Tk()
root.title("steganography - Hide a secret text message in an Image")
root.geometry("900x1000")
root.resizable(False,False)
root.configure(bg="grey")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="select image file",
                                        filetype=(("PNG file","*.png"),
                                                           ("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    Ibl.configure(image=img,width=250,height=250)
    Ibl.image=img
    
def hide():
     global secret
     message=Text1.get(1.0,END)
     secret = Isb.hide(filename, message).save("hidden.png")
       
def show():
    clear_message=lsb.reveal(filename)
    Text1.delete(1.0,END)
    Text1.insert(END,clear_message)
          
def save():
    secret.save("hidden.png")
    
#icon
image_icon=PhotoImage(file="C:/Users/papu/Pictures/logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="C:/Users/papu/Pictures/logo.png1.png")
Label(root,image=logo,bg="grey").place(x=12,y=10)

Label(root,text="IMAGE STEGANOGRAPHY",bg="grey",fg="white",font="arial 20 bold").place(x=140,y=40)

#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=40,y=150)

Ibl=Label(f,bg="black")
Ibl.place(x=40,y=10)

#second frame
frame2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
frame2.place(x=500,y=150)

Text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
Text1.place(x=0,y=0,width=320,height=290)

Scrollbar1=Scrollbar(frame2)
Scrollbar1.place(x=320,y=0,height=300)

Scrollbar1.configure(command=Text1.yview)
Text1.configure(yscrollcommand=Scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="grey",width=340,height=100,relief=GROOVE)
frame3.place(x=40,y=500)

Button(frame3,text="open image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="save image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="picture, image, photo file",bg="grey",fg="yellow").place(x=15,y=5)

#fourth frame
frame4=Frame(root,bd=3,bg="grey",width=340,height=100,relief=GROOVE)
frame4.place(x=500,y=500)

Button(frame4,text="hide data",width=10,height=2,font="arial 14 bold",command=hide).place(x=20,y=30)
Button(frame4,text="show data",width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=30)
Label(frame4,text="picture, image, photo file",bg="grey",fg="yellow").place(x=15,y=5)

root.mainloop()

