from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector  # Connect database with python



class student_details:
	def __init__(self,shrey):
		self.shrey=shrey
		self.shrey.title("Face Attendance system")
		self.shrey.geometry("1530x820+0+0")

		#Variable
		
		self.store_dep=StringVar()
		self.store_course=StringVar()
		self.store_year=StringVar()
		self.store_sem=StringVar()
		self.store_id=StringVar()
		self.store_name=StringVar()
		self.store_se=StringVar()
		self.store_roll=StringVar()
		self.store_mob=StringVar()
		self.store_dob=StringVar()
		self.store_gender=StringVar()
		self.store_email=StringVar()
		self.store_address=StringVar()
		

		#Images bar

		img=Image.open(r"S:\faceattendancesystem\images\face3.jpg")
		img=img.resize((525, 300), Image.BILINEAR)
		self.photoimg=ImageTk.PhotoImage(img)

		photo1=Label(self.shrey,image=self.photoimg)
		photo1.place(x=0,y=0,width=525,height=164)
		
		img1=Image.open(r"S:\faceattendancesystem\images\student2.jpeg")
		img1=img1.resize((525, 300), Image.BILINEAR)
		self.photoimg1=ImageTk.PhotoImage(img1)

		photo2=Label(self.shrey,image=self.photoimg1)
		photo2.place(x=500,y=0,width=525,height=164)
		
		img2=Image.open(r"S:\faceattendancesystem\images\face4.jpg")
		img2=img2.resize((525, 300), Image.BILINEAR)
		self.photoimg2=ImageTk.PhotoImage(img2)

		photo3=Label(self.shrey,image=self.photoimg2)
		photo3.place(x=1000,y=0,width=525,height=164)
		
		# background images
		img4=Image.open(r"S:\faceattendancesystem\images\12.jpg")
		img4=img4.resize((1530, 650), Image.BILINEAR)
		self.photoimg4=ImageTk.PhotoImage(img4)

		photo4=Label(self.shrey,image=self.photoimg4)
		photo4.place(x=2,y=160,width=1520,height=650)
		
		writee=Label(photo4, text="Student Details Managment Dashboard",font=("times new roman",35,"bold"),bg="white",fg="#660033")
		writee.place(x=0, y=0,width=1530,height=45)
		
		#write frame 
		frame1=Frame(photo4, width=1500,)
		frame1.place(x=10,y=48,height=580)
		
		#Left frmae 
		Left_frame=LabelFrame(frame1, text="Student details",font=("times new roman",12,"bold"),bd=2,fg="#660033",width=710)
		Left_frame.place(x=30,y=10,height=565)
		
		#Left frame images
		img_left=Image.open(r"S:\faceattendancesystem\images\st.jpg")
		img_left=img_left.resize((695,100), Image.BILINEAR)
		self.photoimg_left=ImageTk.PhotoImage(img_left)

		photo4=Label(Left_frame,image=self.photoimg_left)
		photo4.place(x=5,y=0,width=695,height=100)
		
		#Left student course frame
		Left_course=LabelFrame(Left_frame,relief=RIDGE, text="Course Information",font=("times new roman",12,"bold"))
		Left_course.place(x=2,y=100,width=700,height=110)
		
		#Left course current
		depart=Label(Left_course, text="Department :",font=("times new roman",12,"bold"))
		depart.grid(row=0,column=0)
		
		depart_entry=ttk.Combobox(Left_course,textvariable=self.store_dep,font=("times new roman",12,"bold"),width=17)
		departt=["Select Department","Computer Science","Information Technology","EN","EC","AIML","ME","D Pharma","B Pharma"]
		depart_entry["values"]=departt
		depart_entry.current(0)
		depart_entry.grid(row=0,column=1,padx=2,pady=10)
		
		#Course
		cu=Label(Left_course, text=" Course :",font=("times new roman",12,"bold"))
		cu.grid(row=0,column=2,sticky=W)
		
		cu_entry=ttk.Combobox(Left_course,textvariable=self.store_course, font=("times new roman",12,"bold"),width=17)
		cu=["Select Course","B.Tech","M.Tech","MCA","MBA","BBA","BCA","MA","Diploma","Pharma"]
		cu_entry["values"]=cu
		cu_entry.current(0)
		cu_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
		
		#Year
		Year=Label(Left_course, text=" Year :",font=("times new roman",12,"bold"))
		Year.grid(row=1,column=0,sticky=W)
		
		Year_entry=ttk.Combobox(Left_course,textvariable=self.store_year, font=("times new roman",12,"bold"),width=17)
		Year=["Select Year","2022-23","2023-24","2024-25","2025-26"]
		Year_entry["values"]=Year
		Year_entry.current(0)
		Year_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

		
		#Semester
		sem=Label(Left_course, text=" Semester :",font=("times new roman",12,"bold"))
		sem.grid(row=1,column=2,sticky=W)
		
		sem_entry=ttk.Combobox(Left_course,textvariable=self.store_sem, font=("times new roman",12,"bold"),width=17)
		sem=["Select Semester","1 semester","2 semester","3 semester","4 semester","5 semester","6 semester","7 semester","8 semester"]
		sem_entry["values"]=sem
		sem_entry.current(0)
		sem_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
		
		#CLASS STUDENT INFORMATION
		studentinfo=LabelFrame(Left_frame,relief=RIDGE, text="Student Information",font=("times new roman",12,"bold"))
		studentinfo.place(x=2,y=205,width=700,height=335)
		
		#StudentID
		student_id=Label(studentinfo,text="Student ID:",font=("times new roman",12,"bold"))
		student_id.grid(row=0,column=0,padx=2,pady=10,sticky=W)
		
		student_entry=ttk.Entry(studentinfo,textvariable=self.store_id,font=("times new roman",12,"bold"),width=20)
		student_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
		
		#Student Name
		student_name=Label(studentinfo,text="Student Name:",font=("times new roman",12,"bold"))
		student_name.grid(row=0,column=2,padx=2,pady=10,sticky=W)
		
		student1_entry=ttk.Entry(studentinfo,textvariable=self.store_name,font=("times new roman",12,"bold"),width=20)
		student1_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
		
		#Roll Number
		roll=Label(studentinfo,text="Roll No:",font=("times new roman",12,"bold"))
		roll.grid(row=1,column=0,padx=2,pady=10,sticky=W)
		
		roll=ttk.Entry(studentinfo,textvariable=self.store_roll,font=("times new roman",12,"bold"),width=20)
		roll.grid(row=1,column=1,padx=2,pady=10,sticky=W)
		
		#Section
		section=Label(studentinfo,text="Section :",font=("times new roman",12,"bold"))
		section.grid(row=0,column=4,padx=2,pady=10,sticky=W)
		
		section=ttk.Combobox(studentinfo,textvariable=self.store_se,font=("times new roman",12,"bold"),width=3)
		sect=["Select Section","A","B","C","D","E","F","G"]
		section["values"]=sect
		section.current(0)
		section.grid(row=0,column=5,padx=2,pady=10,sticky=W)
		
		#Select Date of birth
		dob=Label(studentinfo,text="Date Of Birth:",font=("times new roman",12,"bold"))
		dob.grid(row=2,column=0,padx=2,pady=10,sticky=W)
		
		dob_entry=ttk.Entry(studentinfo,textvariable=self.store_dob,font=("times new roman",12,"bold"),width=20)
		dob_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

		#GEnder
		gender=Label(studentinfo,text="Gender:",font=("times new roman",12,"bold"))
		gender.grid(row=2,column=2,padx=2,pady=5,sticky=W)
		
		gender=ttk.Combobox(studentinfo,textvariable=self.store_gender,font=("times new roman",12,"bold"),width=18)
		ge=["Select Gender","Male","Female","Other"]
		gender["values"]=ge
		gender.grid(row=2,column=3,padx=2,pady=5,sticky=W)
		
		#Email
		email=Label(studentinfo,text="Email:",font=("times new roman",12,"bold"))
		email.grid(row=3,column=0,padx=2,pady=5,sticky=W)
		
		email=ttk.Entry(studentinfo,textvariable=self.store_email,font=("times new roman",12,"bold"),width=20)
		email.grid(row=3,column=1,padx=2,pady=5,sticky=W)
		
		#Mobile Number
		mobile=Label(studentinfo,text="Mobile No:",font=("times new roman",12,"bold"))
		mobile.grid(row=1,column=2,padx=2,pady=5,sticky=W)
		
		mobile=ttk.Entry(studentinfo,textvariable=self.store_mob,font=("times new roman",12,"bold"),width=20)
		mobile.grid(row=1,column=3,padx=2,pady=5,sticky=W)
		
		#Address
		address=Label(studentinfo,text="Address:",font=("times new roman",12,"bold"))
		address.grid(row=3,column=2,padx=2,pady=5,sticky=W)
		
		address=ttk.Entry(studentinfo,textvariable=self.store_address,font=("times new roman",12,"bold"),width=20)
		address.grid(row=3,column=3,padx=2,pady=5,sticky=W)

		#Radio Button
		
		self.store_radio1=StringVar()
		radiobtn1=ttk.Radiobutton(studentinfo,variable=self.store_radio1,text="Take Photo Sample",value="Yes")
		radiobtn1.grid(row=4,column=0,padx=2,sticky=W)
		radiobtn2=ttk.Radiobutton(studentinfo,variable=self.store_radio1,text="No Photo Sample",value="No")
		radiobtn2.grid(row=4,column=1,padx=2,sticky=W)
		
		#Button Frmae
		botton_frame=Frame(studentinfo,bd=2,bg="white")
		botton_frame.place(x=10,y=210,width=680,height=35)
		
		#Save
		savebtn2=Button(botton_frame,text="Save",command=self.adddata,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		savebtn2.grid(row=0,column=0)

		#Update
		updatebtn2=Button(botton_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		updatebtn2.grid(row=0,column=1)

		#delete
		deletebtn2=Button(botton_frame,text="Delete",command=self.deletedata,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
		deletebtn2.grid(row=0,column=3)

		#rest
		rest=Button(botton_frame,text="Reset",command=self.reset,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
		rest.grid(row=0,column=4)
		
		botton_frame1=Frame(studentinfo,bd=2,bg="white")
		botton_frame1.place(x=10,y=250,width=680,height=35)
		
		take_photo_btn=Button(botton_frame1,text="Take Photo Sample",command=self.generatedata,width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
		take_photo_btn.grid(row=0,column=0)
		update_photo_btn=Button(botton_frame1,text="Update Photo",width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
		update_photo_btn.grid(row=0,column=1)
		
		#right frmae 
		Right_frame=LabelFrame(frame1, text="Student Database", font=("times new roman",12,"bold"),bd=2,fg="#660033")
		Right_frame.place(x=750,y=10,width=710,height=565)

		#Right 
		img_right=Image.open(r"S:\faceattendancesystem\images\st.jpg")
		img_right=img_right.resize((695,100), Image.BILINEAR)
		self.photoimg_right=ImageTk.PhotoImage(img_right)

		photo41=Label(Right_frame,image=self.photoimg_right)
		photo41.place(x=5,y=0,width=695,height=100)
		
		#Saerch system
		search_system=LabelFrame(Right_frame,relief=RIDGE, text="Search System",font=("times new roman",12,"bold"))
		search_system.place(x=2,y=100,width=697,height=50)

		system=Label(search_system,text="Search By:",font=("times new roman",12,"bold"))
		system.grid(row=0,column=0)
		
		system_entry=ttk.Combobox(search_system,width=18,font=("times new roman",12,"bold"))
		sty=["AFN No","Roll No","Name","Mobile No"]
		system_entry["values"]=sty
		system_entry.grid(row=0,column=1)
		
		entry_search=Entry(search_system,width=18,font=("times new roman",12,"bold"))
		entry_search.grid(row=0,column=2,padx=5)
	
		botton_f1=Button(search_system,text="Search",width=16,font=("times new roman",10,"bold"),fg="white" ,bg="blue")
		botton_f1.grid(row=0,column=3,padx=5)
		
		botton_f2=Button(search_system,text="Show ALL",width=16,font=("times new roman",10,"bold"),fg="white" ,bg="blue")
		botton_f2.grid(row=0,column=4,padx=5)

		#Table Frame
		table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
		table_frame.place(x=2,y=153,width=697,height=387)

		#Now maked ScrollBar
		
		scroll_x_bar=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y_bar=ttk.Scrollbar(table_frame,orient=VERTICAL)
		
		self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","se","roll","gender","dob","email","mob","address","photo"),xscrollcommand=scroll_x_bar.set,yscrollcommand=scroll_y_bar.set)
	
		scroll_x_bar.pack(side=BOTTOM,fill=X)
		scroll_y_bar.pack(side=RIGHT,fill=Y)
		scroll_x_bar.config(command=self.student_table.xview)
		scroll_y_bar.config(command=self.student_table.yview)
		
		self.student_table.heading("dep",text="Department")
		self.student_table.heading("course",text="Course")
		self.student_table.heading("year",text="Year")
		self.student_table.heading("sem",text="Semester")
		self.student_table.heading("id",text="Student ID")
		self.student_table.heading("name",text="Student Name")
		self.student_table.heading("se",text="Section")
		self.student_table.heading("roll",text="Roll No")
		self.student_table.heading("mob",text="Mobile No")
		self.student_table.heading("dob",text="Date Of Birth")
		self.student_table.heading("gender",text="Gender")
		self.student_table.heading("email",text="Email")
		self.student_table.heading("address",text="Address")
		self.student_table.heading("photo",text="TakePhotoSample")
		self.student_table["show"]="headings"
		

		
		self.student_table.column("dep",width=120)
		self.student_table.column("course",width=120)
		self.student_table.column("year",width=120)
		self.student_table.column("sem",width=120)
		self.student_table.column("id",width=120)
		self.student_table.column("name",width=120)
		self.student_table.column("se",width=120)
		self.student_table.column("roll",width=120)
		self.student_table.column("mob",width=120)
		self.student_table.column("dob",width=120)
		self.student_table.column("gender",width=120)
		self.student_table.column("email",width=120)
		self.student_table.column("address",width=120)
		self.student_table.column("photo",width=120)

		self.student_table.pack(fill=BOTH,expand=1)
		self.student_table.bind("<ButtonRelease>",self.cursor_work)
		self.fetch_data()
	
	def adddata(self):
		if self.store_dep.get()=="Select Department" or self.store_name.get()=="" or self.store_id.get()=="":
			messagebox.showerror("Error","All Fields are required",parent=self.shrey)
		else:
			try:
				conn=mysql.connector.connect(
					host="localhost",
					username="Amit Kumar",
					password="",
					database="face_system"
					)
				my_cursor=conn.cursor()
				my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
					self.store_dep.get(),
					self.store_course.get(),
					self.store_year.get(),
					self.store_sem.get(),
					self.store_id.get(),
					self.store_name.get(),
					self.store_se.get(),
					self.store_roll.get(),
					self.store_mob.get(),
					self.store_dob.get(),
					self.store_gender.get(),
					self.store_email.get(),
					self.store_address.get(),
					self.store_radio1.get()
					))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Success","Student details has been add successfully",parent=self.shrey)
			except Exception as es:
				messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.shrey)


	#fetch data from the data base 

	def fetch_data(self):
		conn=mysql.connector.connect(
			host="localhost",
			username="Amit Kumar",
			password="",
			database="face_system"
			)
		my_cursor=conn.cursor()
		my_cursor.execute("select * from student")
		data=my_cursor.fetchall()
		
		if len(data)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for i in data:
				self.student_table.insert("",END,values=i)
			conn.commit()
		conn.close()
	
	#fetch cursor data
	def cursor_work(self, srol=""):
		cursor_focus=self.student_table.focus()
		content=self.student_table.item(cursor_focus)
		data=content["values"]
		
		self.store_dep.set(data[0]),
		self.store_course.set(data[1]),
		self.store_year.set(data[2]),
		self.store_sem.set(data[3]),
		self.store_id.set(data[4]),
		self.store_name.set(data[5]),
		self.store_se.set(data[6]),
		self.store_roll.set(data[7]),
		self.store_mob.set(data[8]),
		self.store_dob.set(data[9]),
		self.store_gender.set(data[10]),
		self.store_email.set(data[11]),
		self.store_address.set(data[12]),
		self.store_radio1.set(data[13]),


	#update the data 
	def update_data(self):
		if self.store_dep.get()=="Select Department" or self.store_name.get()=="" or self.store_id.get()=="":
			messagebox.showerror("Error","All Fields are required",parent=self.shrey)
		else:
			try:
				update=messagebox.askyesno("update","Do you want to update student details ",parent=self.shrey)
				if update>0:
					conn=mysql.connector.connect(
						host="localhost",
						username="Amit Kumar",
						password="",
						database="face_system"
						)
					my_cursor=conn.cursor()

					my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,se=%s,roll=%s,mob=%s,dob=%s,gender=%s,email=%s,address=%s,Photosample=%s where id=%s",(
		self.store_dep.get(),
		self.store_course.get(),
		self.store_year.get(),
		self.store_sem.get(),
		self.store_name.get(),
		self.store_se.get(),
		self.store_roll.get(),
		self.store_mob.get(),
		self.store_dob.get(),
		self.store_gender.get(),
		self.store_email.get(),
		self.store_address.get(),
		self.store_radio1.get(),
		self.store_id.get()

		))
				else:
					if not update:
						return 
				messagebox.showinfo("Success","Student details successfully updateded.",parent=self.shrey)
				conn.commit()
				self.fetch_data()
				conn.close()
			except Exception as es:
				messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.shrey)
	# Implement delete functionality
	def deletedata(self):
		if self.store_id.get()=="":
			messagebox.showerror("Error","Student id must be required",parent=self.shrey)
		else:
			try:
				delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.shrey)
				if delete>0:
					conn=mysql.connector.connect(
						host="localhost",
						username="Amit Kumar",
						password="",
						database="face_system"
						)
					my_cursor=conn.cursor()
					sql="delete from student where id=%s"
					val=(self.store_id.get(),)
					my_cursor.execute(sql,val)
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.shrey)
			except Exception as es:	
				messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.shrey) 
			
	#Reset the data student

	def reset(self):
   	 # Reset all StringVar variables
    		self.store_dep.set("Select Department")
    		self.store_course.set("Select Course")
    		self.store_year.set("Select Year")
    		self.store_sem.set("Select Semester")
    		self.store_id.set("")
    		self.store_name.set("")
    		self.store_se.set("Select Section")
    		self.store_roll.set("")
    		self.store_mob.set("")
    		self.store_dob.set("")
    		self.store_gender.set("Select Gender")
    		self.store_email.set("")
    		self.store_address.set("")
    		self.store_radio1.set("")


	#Generate Dataset and Take photo set
	def generatedata(self):
		if self.store_dep.get()=="Select Department" or self.store_name.get()=="" or self.store_id.get()=="":
			messagebox.showerror("Error","All Fields are required",parent=self.shrey)
		else:
			try:
		
				conn=mysql.connector.connect(
					host="localhost",
					username="Amit Kumar",
					password="",
					database="face_system"
					)
				my_cursor=conn.cursor()
				my_cursor.execute("select * from student")
				myresult=my_cursor.fetchall()
				ID=1
				for x in myresult:
					ID+=1
					
				my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,se=%s,roll=%s,mob=%s,dob=%s,gender=%s,email=%s,address=%s,Photosample=%s where id=%s",(
		self.store_dep.get(),
		self.store_course.get(),
		self.store_year.get(),
		self.store_sem.get(),
		self.store_name.get(),
		self.store_se.get(),
		self.store_roll.get(),
		self.store_mob.get(),
		self.store_dob.get(),
		self.store_gender.get(),
		self.store_email.get(),
		self.store_address.get(),
		self.store_radio1.get(),
		self.store_id.get()==ID+1

		))
				conn.commit()
				self.fetch_data()
				self.reset()
				conn.close()

				#load face predeined data
				import cv2
				face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
				
				def face_load(img):
					gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
					faces=face_classifier.detectMultiScale(gray,1.3,5)
					for (x,y,w,h) in faces:
						face_load=img[y:y+h,x:x+w]
						return face_load
					
				cap=cv2.VideoCapture(0)
				img_id=0
				while True:
					ret, my_frame=cap.read()
					if face_load(my_frame) is not None:
						img_id+=1
						face=cv2.resize(face_load(my_frame),(550,550))
						#face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
						file_name_path="data/user."+str(ID)+"."+str(img_id)+".jpg"
						cv2.imwrite(file_name_path,face)
						cv2.putText(face,str(img_id),(10,10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
						cv2.imshow("Crooped Face",face)
					if cv2.waitKey(1)==13 or int(img_id)==50:
						break
				cap.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Result","Generating data sets complete !!")
			except Exception as es:
				messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.shrey)
		2345
		
		
if __name__== "__main__":
	shrey=Tk()
	obj=student_details(shrey)
	shrey.mainloop()


