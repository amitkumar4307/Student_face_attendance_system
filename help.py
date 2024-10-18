from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class help:
    def __init__(self,shrey):
        self.shrey=shrey
        self.shrey.title("Face Attendance system")
        self.shrey.geometry("1530x820+0+0")

        #Images bar

        img=Image.open(r"images\222.jpg")
        img=img.resize((1530, 820), Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        photo1=Label(self.shrey,image=self.photoimg)
        photo1.place(x=0,y=0,width=1530,height=820)

        writee=Label(self.shrey,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="#660033")
        writee.place(x=0, y=0,width=1530,height=45)

        Left_course=Frame(photo1,)
        Left_course.place(x=500,y=500,width=500,height=100)
        
        labl1=Label(Left_course,text="Email :AV305764@GMAIL.COM",font=("times new roman",20,"bold"))
        labl1.place(x=50,y=10)
        
        labl2=Label(Left_course,text="Contact : +91 73-8089-4307",font=("times new roman",20,"bold"))
        labl2.place(x=50,y=50)
        
        
        
        
if __name__== "__main__":
    shrey=Tk()
    obj=help(shrey)
    shrey.mainloop()