import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector

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

if __name__ == "__main__":
    shrey = tk.Tk()
    app = Register(shrey)
    shrey.mainloop()
