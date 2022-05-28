#from cProfile import label
#from heapq import heappush
#from logging import root
#from termios import B75
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import shape
from PIL import Image,ImageTk
from cv2 import BORDER_DEFAULT
from setuptools import Command
from student import student
from chatbot import chatbot
from attendance import attendance
from train import train
from tkinter import messagebox
from face_recognition import face_recognition
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
from register import register
from main import Face_Recognition_System



def main():
    win=Tk()
    app=Login(win)
    win.mainloop()


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        #bg image
        img=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\img3.jfif")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        
        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=1530,height=790)

        title_1b1=Label(f_1b1,text="WELCOME TO FACE RECOGNITION ATTENDANCE SYSTEM",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)

       

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)


      #  img1=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\login.jpg")
      #  img1=img1.resize((100,100),Image.ANTIALIAS)
      #  self.photoimg=ImageTk.PhotoImage(img1)
      #  lbling=Label(image=self.photoimg,bg="#002B53",borderwidth=0)
      #  lbling.place(x=750,y=175,width=100,height=1000)


        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forgot?",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='aarya',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpwd.get()
                                                                                        ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='aarya',host='localhost',database='face_recognition',port=3306)
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and ssq=%s and sa=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='aarya',host='localhost',database='face_recognition',port=3306)
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forgot Password?",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)

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
 #   root=Tk()
 #   app=Login(root)
 #   root.mainloop()
    main()