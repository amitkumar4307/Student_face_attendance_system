from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face:
    def __init__(self, shrey):
        self.shrey = shrey
        self.shrey.title("Face Attendance System")
        self.shrey.geometry("1530x820+0+0")

        # Images bar
        img = Image.open(r"images\f.jpg")
        img = img.resize((1530, 820), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        photo1 = Label(self.shrey, image=self.photoimg)
        photo1.place(x=0, y=50, width=1530, height=820)

        writee = Label(self.shrey, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="#660033")
        writee.place(x=0, y=0, width=1530, height=45)

        btn1 = Button(photo1, text="Face Detection Process", command=self.face_capture, font=("times new roman", 15, "bold"), bg="#0E182A", fg="white")
        btn1.place(x=820, y=650)

    # ====attendance save==============
    def attendance(self, i, n, r, d):
        with open("Shrey.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (d not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")

    # =========face recognition=========
    def face_capture(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gra_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gra_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                idn, predict = clf.predict(gra_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="Amit Kumar",
                    password="",
                    database="face_system"
                )
                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT name FROM student WHERE id ={str(idn)}")
                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"

                my_cursor.execute(f"SELECT roll FROM student WHERE id ={str(idn)}")
                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"

                my_cursor.execute(f"SELECT dep FROM student WHERE id ={str(idn)}")
                d = my_cursor.fetchone()
                d = str(d[0]) if d else "Unknown"

                my_cursor.execute(f"SELECT id FROM student WHERE id ={str(idn)}")
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.attendance(i, n, r, d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    shrey = Tk()
    obj = Face(shrey)
    shrey.mainloop()
