from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image
from datetime import datetime
from time import strftime
import time
import tkinter
import os
from student import student_details
from train import Train
from face import Face
from attendance import attendance
from developer import developer 
from help import help



class Face_dedection_system:
	def __init__(self,shrey):
		self.shrey=shrey
		self.shrey.title("Face Attendance system")
		self.shrey.geometry("1530x820+0+0")
		
		#Images bar

		img=Image.open(r"images\college3.jpg")
		img=img.resize((525, 300), Image.BILINEAR)
		self.photoimg=ImageTk.PhotoImage(img)

		photo1=Label(self.shrey,image=self.photoimg)
		photo1.place(x=0,y=0,width=525,height=164)
		
		img1=Image.open(r"S:\faceattendancesystem\images\attendance.jpg")
		img1=img1.resize((525, 300), Image.BILINEAR)
		self.photoimg1=ImageTk.PhotoImage(img1)

		photo2=Label(self.shrey,image=self.photoimg1)
		photo2.place(x=500,y=0,width=525,height=164)
		
		img2=Image.open(r"images\college4.jpg")
		img2=img2.resize((525, 300), Image.BILINEAR)
		self.photoimg2=ImageTk.PhotoImage(img2)

		photo3=Label(self.shrey,image=self.photoimg2)
		photo3.place(x=1000,y=0,width=525,height=164)
		
		# background images
		img4=Image.open(r"images\4555.jpg")
		img4=img4.resize((1530, 650), Image.BILINEAR)
		self.photoimg4=ImageTk.PhotoImage(img4)

		photo4=Label(self.shrey,image=self.photoimg4)
		photo4.place(x=2,y=160,width=1520,height=650)
		
		writee=Label(photo4, text="Student Managment Face Attendance System Software",font=("times new roman",35,"bold"),bg="white",fg="#660033")
		writee.place(x=0, y=0,width=1530,height=45)
		
	
  		
    	#Student details button
		img5=Image.open(r"images\a.jpeg")
		img5=img5.resize((180, 180), Image.BILINEAR)
		self.photoimg5=ImageTk.PhotoImage(img5)
		
		#images convert the button
		d1=Button(photo4,image=self.photoimg5,command=self.Student,cursor="hand2")
		d1.place(x=200,y=100,width=180,height=180)
		
		d2=Button(photo4,text="Student Details",command=self.Student,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		d2.place(x=200,y=250,width=180,height=35)
		
		#face dedection 
		img6=Image.open(r"images\dedt.jpeg")
		img6=img6.resize((180, 180), Image.BILINEAR)
		self.photoimg6=ImageTk.PhotoImage(img6)
		
		#face convert the button
		f1=Button(photo4,image=self.photoimg6,command=self.face_data,cursor="hand2")
		f1.place(x=500,y=100,width=180,height=180)
		
		f2=Button(photo4,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		f2.place(x=500,y=250,width=180,height=35)

		#Attendance Detector
		img7=Image.open(r"images\attendance2.png")
		img7=img7.resize((180, 180), Image.BILINEAR)
		self.photoimg7=ImageTk.PhotoImage(img7)
		
		#Attendance convert the button
		A1=Button(photo4,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
		A1.place(x=800,y=100,width=180,height=180)
		
		A2=Button(photo4,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		A2.place(x=800,y=250,width=180,height=35)

		#Help desktop
		img8=Image.open(r"images\help1.jpg")
		img8=img8.resize((180, 180), Image.BILINEAR)
		self.photoimg8=ImageTk.PhotoImage(img8)
		
		#Help convert the button
		H1=Button(photo4,image=self.photoimg8,cursor="hand2",command=self.help_data)
		H1.place(x=1100,y=100,width=180,height=180)
		
		H2=Button(photo4,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		H2.place(x=1100,y=250,width=180,height=35)

		#trainData
		img9=Image.open(r"images\train.png")
		img9=img9.resize((180, 180), Image.BILINEAR)
		self.photoimg9=ImageTk.PhotoImage(img9)
		
		#Train Data convert the button
		T1=Button(photo4,image=self.photoimg9,command=self.train_data,cursor="hand2")
		T1.place(x=200,y=330,width=180,height=180)
		
		T2=Button(photo4,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		T2.place(x=200,y=475,width=180,height=35)

		#Photos
		img10=Image.open(r"images\gl.png")
		img10=img10.resize((180, 180), Image.BILINEAR)
		self.photoimg10=ImageTk.PhotoImage(img10)
		
		#Photo Data convert the button
		P1=Button(photo4,image=self.photoimg10,cursor="hand2",command=self.open_galary)
		P1.place(x=500,y=330,width=180,height=180)
		
		P2=Button(photo4,text="Photos",cursor="hand2",command=self.open_galary,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		P2.place(x=500,y=475,width=180,height=35)
		
		#Developer 
		img11=Image.open(r"images\dev.jpeg")
		img11=img11.resize((180, 180), Image.BILINEAR)
		self.photoimg11=ImageTk.PhotoImage(img11)
		
		#Developer Data convert the button
		D1=Button(photo4,image=self.photoimg11,cursor="hand2",command=self.developer_data)
		D1.place(x=800,y=330,width=180,height=180)
		
		D2=Button(photo4,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		D2.place(x=800,y=475,width=180,height=35)

		#Exit
		img12=Image.open(r"images\ex.png")
		img12=img12.resize((180, 180), Image.BILINEAR)
		self.photoimg12=ImageTk.PhotoImage(img12)
		
		#Exit Data convert the button
		E1=Button(photo4,image=self.photoimg12,cursor="hand2",command=self.Iexit)
		E1.place(x=1100,y=330,width=180,height=180)
		
		E2=Button(photo4,text="Exit",cursor="hand2",command=self.Iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
		E2.place(x=1100,y=475,width=180,height=35)
  
  
	#Time function
		def time():
			string=strftime('%H:%M:%S %p')
			lb1.config(text = string)
			lb1.after(1000,time)
	
		lb1=Label(photo4,font=("times new roman",14,"bold"),background="white",foreground='red')
		lb1.place(x=0,y=0,width=120,height=40)
		time()
  

	def open_galary(self): 
		os.startfile("data")

	def Student(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=student_details(self.new_tap)
		
	def train_data(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=Train(self.new_tap)
	
	def face_data(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=Face(self.new_tap)

	def attendance_data(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=attendance(self.new_tap)
  
	def developer_data(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=developer(self.new_tap)
  
	def help_data(self):
		self.new_tap=Toplevel(self.shrey)
		self.app=help(self.new_tap)
  
	def Iexit(self):
		self.Iexit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit this Project",parent=self.shrey)
		if self.Iexit >0:
			self.shrey.destroy()
		else:
			return 
  
  
 
if __name__== "__main__":
	
	shrey=Tk()
	obj=Face_dedection_system(shrey)
	shrey.mainloop()