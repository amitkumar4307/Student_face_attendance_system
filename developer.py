from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class developer:
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

        writee=Label(self.shrey,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="#660033")
        writee.place(x=0, y=0,width=1530,height=45)

        Left_course=Frame(photo1,)
        Left_course.place(x=900,y=100,width=600,height=650)

        img2=Image.open(r"images\amit.jpg")
        img2=img2.resize((225, 250), Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        photo2=Label(Left_course,image=self.photoimg2)
        photo2.place(x=372,y=10,width=225,height=250)


        labl1=Label(Left_course, text="Name - Amit Kumar", font=("times new roman",20,"bold"))
        labl1.place(x=5,y=10)
        labl2=Label(Left_course, text="Position - Full Stack developer", font=("times new roman",20,"bold"))
        labl2.place(x=5,y=50)
        labl3=Label(Left_course, text="Skills - Python(TKinter)", font=("times new roman",20,"bold"))
        labl3.place(x=5,y=90)
        labl4=Label(Left_course, text="Contact - 7380894307", font=("times new roman",20,"bold"))
        labl4.place(x=5,y=130)
        labl5=Label(Left_course, text="Location - Lucknow", font=("times new roman",20,"bold"))
        labl5.place(x=5,y=170)
        
        
        
        
        
if __name__== "__main__":

    shrey=Tk()
    obj=developer(shrey)
    shrey.mainloop()