from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import mysql.connector
import tkinter
from main import Face_dedection_system

def main():
    win=Tk()
    app=loginwindow(win)
    win.mainloop()

class loginwindow:
    def __init__(self,shrey):
        self.shrey=shrey
        self.shrey.title("Face Attendance system")
        self.shrey.geometry("1530x820+0+0")
        
        
        self.var_email=StringVar()
        self.var_passw=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"S:\faceattendancesystem\images\145.png")
        labl_bg=Label(self.shrey,image=self.bg)
        labl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frmaa=Frame(self.shrey,bg="#e6e6e6")
        frmaa.place(x=615,y=170,width=340,height=450)
        
        
        #user images
        img1=Image.open(r"S:\faceattendancesystem\images\user1.png")
        img1=img1.resize((100,100),Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl1img1=Label(image=self.photoimage1,bg="#e6e6e6",borderwidth=0)
        lbl1img1.place(x=730,y=175,width=100,height=100)
        
        #Get let start
        get=Label(frmaa,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="#e6e6e6")
        get.place(x=95,y=100)

        #username
        creat1=Label(frmaa,text="Username or Email",font=("times new roman",15,"bold"),fg="black",bg="#e6e6e6")
        creat1.place(x=65,y=155)
        
        self.txtuser=ttk.Entry(frmaa,textvariable=self.var_email, font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        creat2=Label(frmaa,text="Password",font=("times new roman",15,"bold"),fg="black",bg="#e6e6e6")
        creat2.place(x=65,y=235)
        
        self.txtpass=ttk.Entry(frmaa,show='*',textvariable=self.var_passw,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)
        
        
        # user or mail icons
        img3=Image.open(r"S:\faceattendancesystem\images\user1.png")
        img3=img3.resize((25,23),Image.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl1img3=Label(image=self.photoimage3,bg="#e6e6e6",borderwidth=0)
        lbl1img3.place(x=653,y=328,width=25,height=23)
        
        #user password icon
        img6=Image.open(r"S:\faceattendancesystem\images\password-180.png")
        img6=img6.resize((25,20),Image.BILINEAR)
        self.photoimage6=ImageTk.PhotoImage(img6)
        lbl1img6=Label(image=self.photoimage6,bg="#e6e6e6",borderwidth=0)
        lbl1img6.place(x=653,y=408,width=25,height=20)
        
        
        btn1=Button(frmaa,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        btn1.place(x=110,y=300,width=120,height=35)
        
        #btn2 forget
        btn2=Button(frmaa,text="Forgot password?",font=("times new roman",13,"bold"),borderwidth=0,fg="black",bg="#e6e6e6",activebackground="#e6e6e6",activeforeground="black")
        btn2.place(x=90,y=340,width=160)
        
        #btnregister
        #btn2
        btn3=Button(frmaa,text="New Registration",font=("times new roman",13,"bold"),command=self.register_window,bd=2,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        btn3.place(x=40,y=380,width=260)
  
  
    def register_window(self):
        self.new_window=Toplevel(self.shrey)
        self.app=Register(self.new_window)
             
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.txtuser.get()=="amit" and self.txtpass.get()=="amit12345":
            messagebox.showinfo("Success","Welcome to Management System !")
        else:
            conn=mysql.connector.connect(
					host="localhost",
					username="Amit Kumar",
					password="",
					database="face_system"
					)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
               self.var_email.get(),
               self.var_passw.get()
            ))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.shrey)
                    self.app=Face_dedection_system(self.new_window) #add project
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()
            
    def clear(self):
        self.txtuser.delete(0, tk.END)
        self.txtpass.delete(0, tk.END)




class Register:
    def __init__(self, shrey):
        self.shrey = shrey
        self.shrey.geometry("1530x820+0+0")
        
        #========Get data from the Entery field========
        
       
        self.var_lname=tk.StringVar()
        self.var_contact=tk.StringVar()
        self.var_email=tk.StringVar()
        self.security_question_var = tk.StringVar()
        self.var_answer=tk.StringVar()
        self.var_passw=tk.StringVar()
        self.var_cpass=tk.StringVar()
        
        
        
        # Load and set background image
        self.bg_image = Image.open(r"S:\faceattendancesystem\images\attende.jpg")  # Replace with your image path
        self.bg_image = self.bg_image.resize((1530, 820), Image.BILINEAR)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.shrey, image=self.bg_photo)
        self.bg_label.place(x=0, y=0)

        # Create a frame for the registration form
        self.frame = tk.Frame(self.shrey, bg='white', bd=5)
        self.frame.place(relx=0.5, rely=0.5, width=450, height=600, anchor='center')

        # Define font styles
        title_font = ("Times New Roman", 16, "bold")
        font_style = ("Times New Roman", 12, "bold")

        # Add main heading
        fname=tk.Label(self.frame, text="Registration Form", font=title_font, bg='white')
        fname.grid(row=0, columnspan=6, padx=10, pady=10)

        # Create labels and entries for the registration form
        lname=tk.Label(self.frame, text="Full Name", font=font_style)
        lname.grid(row=1, column=0, padx=10, pady=10)
        self.first_name_entry = tk.Entry(self.frame,textvariable=self.var_lname,width=30)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)


        contact=tk.Label(self.frame, text="Contact No", font=font_style)
        contact.grid(row=2, column=0, padx=10, pady=10)
        self.contact_entry = tk.Entry(self.frame,textvariable=self.var_contact, width=30)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=10)

        email=tk.Label(self.frame, text="Email", font=font_style)
        email.grid(row=3, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.frame,textvariable=self.var_email, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)

        question=tk.Label(self.frame, text="Security Question", font=font_style)
        question.grid(row=4, column=0, padx=10, pady=10)
        
        self.security_question_combobox = ttk.Combobox(self.frame, textvariable=self.security_question_var, width=27)
        self.security_question_combobox['values'] = [
            "What is your pet's name?",
            "What is your mother's maiden name?",
            "What city were you born in?"
        ]
        self.security_question_combobox.grid(row=4, column=1, padx=10, pady=10)

        answer=tk.Label(self.frame, text="Security Answer", font=font_style)
        answer.grid(row=5, column=0, padx=10, pady=10)
        self.security_answer_entry = tk.Entry(self.frame,textvariable=self.var_answer, width=30)
        self.security_answer_entry.grid(row=5, column=1, padx=10, pady=10)

        passw=tk.Label(self.frame,text="Password", font=font_style)
        passw.grid(row=6, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.frame,textvariable=self.var_passw,show='*', width=30)
        self.password_entry.grid(row=6, column=1, padx=10, pady=10)

        cpass=tk.Label(self.frame, text="Confirm Password", font=font_style)
        cpass.grid(row=7, column=0, padx=10, pady=10)
        self.confirm_password_entry = tk.Entry(self.frame,textvariable=self.var_cpass, show='*', width=30)
        self.confirm_password_entry.grid(row=7, column=1, padx=10, pady=10)

        # Random capture feature
        cap=tk.Label(self.frame, text="Capture:", font=font_style)
        cap.grid(row=8, column=0, padx=10, pady=10)
        self.capture_value = random.randint(1000, 9999)
        self.capture_label = tk.Label(self.frame, text=str(self.capture_value), font=font_style)
        self.capture_label.grid(row=8, column=1, padx=10, pady=10)

        self.capture_entry = tk.Entry(self.frame, width=30)
        self.capture_entry.grid(row=9, column=1, padx=10, pady=10)

        self.terms_var = tk.IntVar()
        self.terms_check = tk.Checkbutton(self.frame, text="Agree to Terms and Conditions", variable=self.terms_var, font=font_style)
        self.terms_check.grid(row=10, columnspan=2, padx=10, pady=10)

        btn1=tk.Button(self.frame, text="Register Now", command=self.submit, font=font_style,fg="#02e355",width="12")
        btn1.place(x=80, y=520)

        btn2=tk.Button(self.frame, text="Login", font=font_style, fg="Blue",width="12")
        btn2.place(x=250, y=520)

    def submit(self):
        # Validate form inputs
        if not self.first_name_entry.get() or not self.contact_entry.get() or not self.email_entry.get() or not self.security_answer_entry.get() or not self.password_entry.get() or not self.confirm_password_entry.get():
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        elif not self.terms_var.get():
            messagebox.showerror("Error", "You must agree to the terms and conditions!")
            return
        
        elif self.capture_entry.get() != str(self.capture_value):
            messagebox.showerror("Error", "Incorrect capture value!")
            return
        else:
            conn=mysql.connector.connect(
					host="localhost",
					username="Amit Kumar",
					password="",
					database="face_system"
					)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exist, Please try another email ")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.security_question_var.get(),
                    self.var_answer.get(),
                    self.var_passw.get()
                    ))
            
            conn.commit()
            conn.close()
            
        # Registration successful
        messagebox.showinfo("Registration", "Your registration is successful!")
        self.reset_form()
        

    def reset_form(self):
        self.first_name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.security_answer_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.capture_entry.delete(0, tk.END)
        self.terms_var.set(0)
        self.capture_value = random.randint(1000, 9999)
        self.capture_label.config(text=str(self.capture_value))







if __name__== "__main__":
    main()