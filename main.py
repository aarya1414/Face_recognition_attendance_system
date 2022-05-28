from cProfile import label
from heapq import heappush
from logging import root
#from termios import B75
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from attendance import attendance
from student import student
from train import train
from face_recognition import face_recognition
from chatbot import chatbot
from help import help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

        #bg image
        img=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\img3.jfif")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=1530,height=790)




        title_1b1=Label(f_1b1,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)

        #student button
        img2=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\std1.jpg")
        img2=img2.resize((225,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(f_1b1,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=220,height=220)

        b1_1=Button(f_1b1,text="Student Details",command=self.student_details,cursor="hand2",font=("sans-serif",15,"bold"),fg="#21478a")
        b1_1.place(x=200,y=370,width=220,height=40)


        img3=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\det1.jpg")
        img3=img3.resize((225,230),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) 

        b2=Button(f_1b1,image=self.photoimg3,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=150,width=220,height=220)

        b2_1=Button(f_1b1,text="Face Recognition",cursor="hand2",command=self.face_data,font=("sans-serif",15,"bold"),fg="#21478a")
        b2_1.place(x=500,y=370,width=220,height=40)


        img4=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\att.jpg")
        img4=img4.resize((225,230),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(f_1b1,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=150,width=220,height=220)

        b3_1=Button(f_1b1,text="Attendance",cursor="hand2",command=self.attendance_data,font=("sans-serif",15,"bold"),fg="#21478a")
        b3_1.place(x=800,y=370,width=220,height=40)


        img5=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\tra1.jpg")
        img5=img5.resize((225,230),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4=Button(f_1b1,image=self.photoimg5,cursor="hand2",command=self.chatbot)
        b4.place(x=1100,y=150,width=220,height=220)

        b4_1=Button(f_1b1,text="Chatbot",cursor="hand2",command=self.chatbot,font=("sans-serif",15,"bold"),fg="#21478a")
        b4_1.place(x=1100,y=370,width=220,height=40)


        img6=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\dev.jpg")
        img6=img6.resize((225,230),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(f_1b1,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=450,width=220,height=220)

        b5_1=Button(f_1b1,text="Train Data",cursor="hand2",command=self.train_data,font=("sans-serif",15,"bold"),fg="#21478a")
        b5_1.place(x=200,y=668,width=220,height=40)


        img7=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\data.jpg")
        img7=img7.resize((225,230),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b6=Button(f_1b1,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=450,width=220,height=220)
        
        b6_1=Button(f_1b1,text="Dataset",cursor="hand2",command=self.open_img,font=("sans-serif",15,"bold"),fg="#21478a")
        b6_1.place(x=500,y=668,width=220,height=40)

        img8=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\hlp.jpg")
        img8=img8.resize((225,230),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b7=Button(f_1b1,image=self.photoimg8,cursor="hand2",command=self.help)
        b7.place(x=800,y=450,width=220,height=220)


        b7_1=Button(f_1b1,text="Help Desk",cursor="hand2",command=self.help,font=("sans-serif",15,"bold"),fg="#21478a")
        b7_1.place(x=800,y=668,width=220,height=40)


        img9=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\exi.jpg")
        img9=img9.resize((225,230),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b8=Button(f_1b1,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=450,width=220,height=220)

        b8_1=Button(f_1b1,text="Exit",command=self.iExit,cursor="hand2",font=("sans-serif",15,"bold"),fg="#21478a")
        b8_1.place(x=1100,y=668,width=220,height=40)

    def open_img(self):
        os.startfile("data")


 #==================Function Button===============================       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=chatbot(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure you want to exit?")
        if self.iExit >0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        