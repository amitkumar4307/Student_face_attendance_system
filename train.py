from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
	def __init__(self,shrey):
		self.shrey=shrey
		self.shrey.title("Face Attendance system")
		self.shrey.geometry("1530x820+0+0")
		
		#Images bar

		img=Image.open(r"images\train.jpg")
		img=img.resize((1530, 820), Image.BILINEAR)
		self.photoimg=ImageTk.PhotoImage(img)

		photo1=Label(self.shrey,image=self.photoimg)
		photo1.place(x=0,y=0,width=1530,height=820)
		
		
		
		writee=Label(self.shrey, text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="#660033")
		writee.place(x=0, y=0,width=1530,height=45)

		btn1=Button(photo1, text="TRAIN DATA SET",command=self.train_classifier,font=("times new roman",20,"bold"),bg="#3D1386",fg="#660033")
		btn1.place(x=600, y=600)



	def train_classifier(self):
		data_dir=("data")
		path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]	
		
		faces=[]
		ids=[]
		for image in path:
			img=Image.open(image).convert('L')
			imageNp=np.array(img,"uint8")
			id=int(os.path.split(image)[1].split('.')[1])
			
			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Training",imageNp)
			cv2.waitKey(1)==13
			
		ids=np.array(ids)
		
		#train the classifier and save
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces,ids)
		clf.write("classifier.xml")
		cv.destroyAllWindows()
		messagebox.showinfo("Result","Training datasets completed !")



if __name__== "__main__":

	shrey=Tk()
	obj=Train(shrey)
	shrey.mainloop()