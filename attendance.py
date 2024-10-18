from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector  # Connect database with python
import os
import cv2
import csv
from tkinter import filedialog



mydata=[]
class attendance:
	def __init__(self,shrey):
		self.shrey=shrey
		self.shrey.title("Face Attendance system")
		self.shrey.geometry("1530x820+0+0")

		#maked variable perform action
  
		self.var_atend_id=StringVar()
		self.var_atend_roll=StringVar()
		self.var_atend_name=StringVar()
		self.var_atend_dep=StringVar()
		self.var_atend_time=StringVar()
		self.var_atend_date=StringVar()
		self.var_atend_attendance=StringVar()
	

		#Images bar

		img=Image.open(r"S:\faceattendancesystem\images\attende.jpg")
		img=img.resize((765, 300), Image.BILINEAR)
		self.photoimg=ImageTk.PhotoImage(img)

		photo1=Label(self.shrey,image=self.photoimg)
		photo1.place(x=0,y=0,width=765,height=164)
		
		img1=Image.open(r"S:\faceattendancesystem\images\attendance3.jpg")
		img1=img1.resize((765, 300), Image.BILINEAR)
		self.photoimg1=ImageTk.PhotoImage(img1)

		photo2=Label(self.shrey,image=self.photoimg1)
		photo2.place(x=765,y=0,width=765,height=164)
		
		
		
		# background images
		img4=Image.open(r"S:\faceattendancesystem\images\12.jpg")
		img4=img4.resize((1530, 650), Image.BILINEAR)
		self.photoimg4=ImageTk.PhotoImage(img4)

		photo4=Label(self.shrey,image=self.photoimg4)
		photo4.place(x=2,y=160,width=1520,height=650)
		
		writee=Label(photo4, text="Attendance Managment of Student",font=("times new roman",35,"bold"),bg="white",fg="#660033")
		writee.place(x=0, y=0,width=1530,height=45)
		
		#write frame 
		frame1=Frame(photo4, width=1500,)
		frame1.place(x=10,y=48,height=580)
		
		#Left frmae 
		Left_frame=LabelFrame(frame1, text="Student details",font=("times new roman",12,"bold"),bd=2,fg="#660033",width=710)
		Left_frame.place(x=30,y=10,height=565)
		
		#Left frame images
		img_left=Image.open(r"S:\faceattendancesystem\images\face3.jpg")
		img_left=img_left.resize((695,200), Image.BILINEAR)
		self.photoimg_left=ImageTk.PhotoImage(img_left)

		photo4=Label(Left_frame,image=self.photoimg_left)
		photo4.place(x=5,y=0,width=695,height=200)
		
		#CLASS STUDENT INFORMATION
		studentinfo=LabelFrame(Left_frame,relief=RIDGE, text="Student Information",font=("times new roman",12,"bold"))
		studentinfo.place(x=2,y=205,width=700,height=335)
	
		#Attendance ID
		att_id=Label(studentinfo,text="Attendance ID:",font=("times new roman",12,"bold"))
		att_id.grid(row=0,column=0,padx=2,pady=10,sticky=W)
		att_entry=ttk.Entry(studentinfo, width='20' ,textvariable=self.var_atend_id,font=("times new roman",12,"bold"))
		att_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		#roll Number
		roll_id=Label(studentinfo,text="Roll No:",font=("times new roman",12,"bold"))
		roll_id.grid(row=0,column=2,padx=2,pady=10,sticky=W)
		roll_id=ttk.Entry(studentinfo, width='20',textvariable=self.var_atend_roll,font=("times new roman",12,"bold"))
		roll_id.grid(row=0,column=3,padx=2,pady=10,sticky=W)
  
		#Name
		name_stu=Label(studentinfo,text="Name :",font=("times new roman",12,"bold"))
		name_stu.grid(row=1,column=0,padx=2,pady=10,sticky=W)
		name_stu=ttk.Entry(studentinfo, width='20' ,textvariable=self.var_atend_name,font=("times new roman",12,"bold"))
		name_stu.grid(row=1,column=1,padx=2,pady=10,sticky=W)
  
		#Department
		Department=Label(studentinfo,text="Department :",font=("times new roman",12,"bold"))
		Department.grid(row=1,column=2,padx=2,pady=10,sticky=W)
		Department_entry=ttk.Entry(studentinfo, width='20' ,textvariable=self.var_atend_dep,font=("times new roman",12,"bold"))
		Department_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
  
		#Time
		time=Label(studentinfo,text="Time:",font=("times new roman",12,"bold"))
		time.grid(row=2,column=0,padx=2,pady=10,sticky=W)
		time_entry=ttk.Entry(studentinfo, width='20' ,textvariable=self.var_atend_time,font=("times new roman",12,"bold"))
		time_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)
  
		#Date
		Dete=Label(studentinfo,text="Date:",font=("times new roman",12,"bold"))
		Dete.grid(row=2,column=2,padx=2,pady=10,sticky=W)
		Dete_entry=ttk.Entry(studentinfo, width='20' ,textvariable=self.var_atend_date,font=("times new roman",12,"bold"))
		Dete_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
  
		#Attendance status
		attend=Label(studentinfo,text="Attendance Status:",font=("times new roman",12,"bold"))
		attend.grid(row=3,column=0,padx=2,pady=10,sticky=W)
		attend_entry=ttk.Combobox(studentinfo, width='18' ,textvariable=self.var_atend_attendance,font=("times new roman",12,"bold"))
		sty=["Status","Present","Absent"]
		attend_entry["values"]=sty
		attend_entry.current(0)
		attend_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

  
		#button
		botton_frame=Frame(studentinfo,bd=2,bg="white")
		botton_frame.place(x=7,y=260,width=680,height=35)
		
		#Save
		savebtn2=Button(botton_frame,text="Import csv",command=self.importCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		savebtn2.grid(row=0,column=0)

		#Update
		updatebtn2=Button(botton_frame,text="Export csv",command=self.ExportCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		updatebtn2.grid(row=0,column=1)

		#delete
		deletebtn2=Button(botton_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
		deletebtn2.grid(row=0,column=3)

		#rest
		rest=Button(botton_frame,text="Reset",command=self.reseat, width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		rest.grid(row=0,column=4)
  
  
  
		#right frmae 
		Right_frame=LabelFrame(frame1, text="Attendance Details", font=("times new roman",12,"bold"),bd=2,fg="#660033")
		Right_frame.place(x=750,y=10,width=710,height=565)
		
		table_scroll=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
		table_scroll.place(x=5,y=1,width=695,height=540)
  
  
		#Scroll Triger
		scroll_x=ttk.Scrollbar(table_scroll,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_scroll,orient=VERTICAL)
  
		self.AttendanceReportTable=ttk.Treeview(table_scroll,column=("id","roll","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
  
		scroll_x.config(command=self.AttendanceReportTable.xview)
		scroll_y.config(command=self.AttendanceReportTable.yview)
  
		#heading for the tables 
		self.AttendanceReportTable.heading("id",text="Attendance ID")
		self.AttendanceReportTable.heading("roll",text="Roll Number")
		self.AttendanceReportTable.heading("department",text="Department")
		self.AttendanceReportTable.heading("time",text="Time")
		self.AttendanceReportTable.heading("date",text="Date")
		self.AttendanceReportTable.heading("attendance",text="Attendance")
  
		self.AttendanceReportTable["show"]="headings"

		#set width of the
		self.AttendanceReportTable.column("id",width=120)
		self.AttendanceReportTable.column("roll",width=120)
		self.AttendanceReportTable.column("department",width=120)
		self.AttendanceReportTable.column("time",width=120)
		self.AttendanceReportTable.column("date",width=120)
		self.AttendanceReportTable.column("attendance",width=120)
		
		
  
		self.AttendanceReportTable.pack(fill=BOTH,expand=1)
  
		self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
  
	def fetchdata(self,rows):
		self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
		for i in rows:
			self.AttendanceReportTable.insert("",END,values=i)
	def importCSV(self):
		global mydata
		fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.shrey)
		with open(fln) as myfile:
			csvread=csv.reader(myfile,delimiter=",")
			for i in csvread:
				mydata.append(i)
			self.fetchdata(mydata)
   
	#export csv
	def ExportCSV(self):
		try:
			if len(mydata)<1:
				messagebox.showerror("No Data","No Data Found to export",parent=self.shrey)
				return False
			fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.shrey)
			with open(fln,mode="w",newline="") as myfile:
				exp_write=csv.writer(myfile,delimiter=",")
				for i in mydata:
					exp_write.writerow(i)
				messagebox.showinfo("Data Export","Your data  exported to"+os.path.basename(fln)+"Successfully")
		except Exception as es:
			messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.shrey)

	def get_cursor(self,event=""):
		cursor_row=self.AttendanceReportTable.focus()
		content=self.AttendanceReportTable.item(cursor_row)
		rows=content['values']
		self.var_atend_id.set(rows[0])
		self.var_atend_roll.set(rows[1])
		self.var_atend_name.set(rows[2])
		self.var_atend_dep.set(rows[3])
		self.var_atend_time.set(rows[4])
		self.var_atend_date.set(rows[5])
		self.var_atend_attendance.set(rows[6])
  
  
	def reseat(self):
		self.var_atend_id.set("")
		self.var_atend_roll.set("")
		self.var_atend_name.set("")
		self.var_atend_dep.set("")
		self.var_atend_time.set("")
		self.var_atend_date.set("")
		self.var_atend_attendance.set("")
   
   
   
   
  
if __name__== "__main__":
	shrey=Tk()
	obj=attendance(shrey)
	shrey.mainloop()


