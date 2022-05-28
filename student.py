from cgitb import text
from logging import exception
from msilib.schema import ComboBox
from operator import mul
from sqlite3 import Cursor, Row
from tkinter import*
import tkinter as tk
from tkinter.messagebox import showinfo                   
from tkinter import ttk
from turtle import bgcolor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re

conn = mysql.connector.connect(username='root', password='aarya',host='localhost',database='face_recognition',port=3306)
my_cursor = conn.cursor()
my_cursor.execute("show databases")
data = my_cursor.fetchall()
print(data)
conn.close()

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")


        # variables

        self.var_dep=StringVar()
        self.var_semester=StringVar()
        self.var_name=StringVar()
        self.var_ID=StringVar()
        self.var_rollno=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_photo=StringVar()

        #bg image
        img=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\img3.jfif")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=1530,height=790)

        title_1b1=Label(f_1b1,text="STUDENT MANAGEMENT SYSTEM",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)


        main_frame=Frame(f_1b1,bd=2)
        main_frame.place(x=20,y=100,width=1490,height=660)


        #left lable frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("sans-serif",18,"bold"),fg="#21478a")
        left_frame.place(x=20,y=20,width=660,height=620)

        
       
       
        #Student Name
        student_name=Label(left_frame,text="Student Name:",font=("sans-serif",15,"bold"),fg="#21478a")
        student_name.grid(row=0,column=0,padx=10,sticky=W)

        student_name=Entry(left_frame,textvariable=self.var_name,width=20,font=("sans-serif",15),fg="black")
        student_name.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        #StudentID_no
        ID_no=Label(left_frame,text="Student ID No:",font=("sans-serif",15,"bold"),fg="#21478a")
        ID_no.grid(row=1,column=0,padx=10,sticky=W)

        ID_no=Entry(left_frame,textvariable=self.var_ID,width=20,font=("sans-serif",15),fg="black")
        ID_no.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        #Roll No
        roll_no=Label(left_frame,text="Roll No:",font=("sans-serif",15,"bold"),fg="#21478a")
        roll_no.grid(row=2,column=0,padx=10,sticky=W)

        roll_no=Entry(left_frame,textvariable=self.var_rollno,width=20,font=("sans-serif",15),fg="black")
        roll_no.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Departmant
        dep_name=Label(left_frame,text="Department:",font=("sans-serif",15,"bold"),fg="#21478a")
        dep_name.grid(row=3,column=0,padx=10,sticky=W)

        dep_name=Entry(left_frame,textvariable=self.var_dep,width=20,font=("sans-serif",15),fg="black")
        dep_name.grid(row=3,column=1,padx=10,pady=15,sticky=W)

       # dep_com=ComboBox(left_frame,font=("sans-serif",12,"bold"),fg="#21478a", width=20,state="read only")
       # dep_com["values"]=("Select Department","Computer Science","IT","Civil","Mechnical","Electronics")
       # dep_com.current(0)
       # dep_com.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Semester
        sem=Label(left_frame,text="Semester:",font=("sans-serif",15,"bold"),fg="#21478a")
        sem.grid(row=4,column=0,padx=10,sticky=W)

        sem=Entry(left_frame,textvariable=self.var_semester,width=20,font=("sans-serif",15),fg="black")
        sem.grid(row=4,column=1,padx=10,pady=15,sticky=W)

        
        #Gender
    #    gender=Label(left_frame,text="Gender:",font=("sans-serif",15,"bold"),fg="#21478a")
     #   gender.grid(row=5,column=0,padx=10,sticky=W)

    #    gender=Entry(left_frame,textvariable=self.var_gender,width=20,font=("sans-serif",15,"bold"),fg="#21478a")
     #   gender.grid(row=5,column=1,padx=10,pady=15,sticky=W)

        #Email_ID
        Email_ID=Label(left_frame,text="Email ID:",font=("sans-serif",15,"bold"),fg="#21478a")
        Email_ID.grid(row=5,column=0,padx=10,sticky=W)

        Email_ID=Entry(left_frame,textvariable=self.var_email,width=20,font=("sans-serif",15),fg="black")
        Email_ID.grid(row=5,column=1,padx=10,pady=15,sticky=W)


        #Phone No
        phone_no=Label(left_frame,text="Phone Number:",font=("sans-serif",15,"bold"),fg="#21478a")
        phone_no.grid(row=6,column=0,padx=10,sticky=W)

        phone_no=Entry(left_frame,textvariable=self.var_phone,width=20,font=("sans-serif",15),fg="black")
        phone_no.grid(row=6,column=1,padx=10,pady=15,sticky=W)


        #radio button
        self.var_radio1=StringVar()
        Radiobutton1=Radiobutton(left_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=8,column=0)

        self.var_radio2=StringVar()
        Radiobutton2=Radiobutton(left_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=8,column=1)

        #button frame 1
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=500,width=619,height=45)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        reset_btn.grid(row=0,column=4)

        
        #button frame 2
        btn_frame1=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=12,y=545,width=612,height=45)

        photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=25,font=("sans-serif",15,"bold"),fg="#21478a")
        photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset,width=24,font=("sans-serif",15,"bold"),fg="#21478a")
        update_photo_btn.grid(row=1,column=1)


        #right lable frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendace Information",font=("sans-serif",18,"bold"),fg="#21478a")
        right_frame.place(x=680,y=20,width=775,height=620)



        #================Search System================#

       # search_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white",text="Search System")
       # search_frame.place(x=10,y=500,width=619,height=45)

     #   search_lable=Label(right_frame,text="Search By:",font=("sans-serif",15,"bold"),fg="#21478a")
     #   search_lable.grid(row=0,column=0,padx=10,pady=15,sticky=W)

     #   search_com=ttk.Combobox(right_frame,font=("sans-serif",12,"bold"),fg="#21478a", width=20,state="readonly")
      #  search_com["values"]=("Select ","Roll No","Phone no","Mechnical","Electronics")
       # search_com.current(0)
        #search_com.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        scroll_x=ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(right_frame,column=("Dep","name","roll no","gender","semester","emailID","IDNo","Gender"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)




        self.student_table.heading('0',text='Department')
        self.student_table.heading('1',text='Semester')
        self.student_table.heading('2',text='Student Name')
        self.student_table.heading('3',text='Roll No')
        self.student_table.heading('4',text='Student ID')
        self.student_table.heading('5',text='Phone No')
        self.student_table.heading('6',text='Email ID')
     #   self.student_table.heading(column="7",text="Gender")
        self.student_table.heading('7',text='Photo Sample Status')
        self.student_table["show"]="headings"


        





        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get()=="" or self.var_name.get()=="" or self.var_rollno.get()=="" or self.var_ID.get()==""or self.var_semester.get()=="" or self.var_phone.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aarya",database="face_recognition",port=3306)
                my_cursor= conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_rollno.get(),
                                                                                        self.var_ID.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_radio1.get()




                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                        
                messagebox.showinfo("Success","Data Successfully Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    ## fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="aarya",database="face_recognition",port=3306)
        my_cursor= conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

            
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_semester.set(data[1])
        self.var_name.set(data[2])
        self.var_rollno.set(data[3])
        self.var_ID.set(data[4])
        self.var_phone.set(data[5])
        self.var_email.set(data[6])
      #  self.var_gender.set(data[7])
        self.var_radio1.set(data[7])

    #update function
    def update_data(self):
        if self.var_dep.get()=="" or self.var_name.get()=="" or self.var_rollno.get()=="" or self.var_semester.get()==""  or self.var_ID.get()=="" or self.var_phone.get()=="" or self.var_email.get()=="" or self.var_radio1=="" :
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                Update1=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if (Update1> 0):
                    conn=mysql.connector.connect(host="localhost",username="root",password="aarya",database="face_recognition")
                    my_cursor= conn.cursor()
                    my_cursor.execute("update student set dep=%s,semester=%s,name=%s,roll_no=%s,phone=%s,email=%s,photosample=%s where Student_ID=%s",(
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_radio1.get(),
                    self.var_ID.get()
 
                     ))
                else:
                    if not Update1:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
               
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #delete 
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data",parent=self.root)
                if (delete>=0):
                    conn=mysql.connector.connect(host="localhost",username="root",password="aarya",database="face_recognition")
                    my_cursor= conn.cursor()
                    sql="delete from student where Student_ID=%s",self.var_ID.get()
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

  #reset
    def reset_data(self):
        self.var_dep.set("")
        self.var_semester.set("")
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_photo.set("")
        self.var_ID.set("")
        self.var_gender.set("")

# Generate data set or take photo sample

    def generate_dataset(self):
        if self.var_dep.get()=="" or self.var_name.get()=="" or self.var_rollno.get()=="" or self.var_ID.get()==""  or self.var_phone.get()==""or self.var_phone.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aarya",database="face_recognition")
                my_cursor= conn.cursor()    
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,semester=%s,name=%s,roll_no=%s,phone=%s,email=%s,photosample=%s where Student_ID=%s",(
                                                                                                                                    self.var_dep.get(),
                                                                                                                                    self.var_semester.get(),
                                                                                                                                    self.var_name.get(),
                                                                                                                                    self.var_rollno.get(),
                                                                                                                                    self.var_phone.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_radio1.get(),
                                                                                                                                    self.var_ID.get()==id+1
 
                                                                                                                                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

              #  ============load predefined data on face frontal from opencv=======================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)  
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=("data/user."+str(id)+"."+str(img_id)+".jpg")
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data sets completed!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)








        











if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop() 