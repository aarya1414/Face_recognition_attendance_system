from cProfile import label
from heapq import heappush
from logging import root
#from termios import B75
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import shape
from PIL import Image,ImageTk
from student import student
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog



myData=[]
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")


        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()



        #bg image
        img=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\img3.jfif")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=1530,height=790)

        title_1b1=Label(f_1b1,text="ATTENDANCE RECORD",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)



        main_frame=Frame(f_1b1,bd=2)
        main_frame.place(x=15,y=100,width=1490,height=660)

        #left lable frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("sans-serif",18,"bold"),fg="#21478a")
        left_frame.place(x=20,y=20,width=660,height=620)

        #label and entry
        #Attendance ID
        attendanceID_label=Label(left_frame,text="Attendance ID:",font=("sans-serif",15,"bold"),fg="#21478a")
        attendanceID_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_label=Entry(left_frame,width=20,textvariable=self.var_id,font=("sans-serif",15),fg="black")
        attendanceID_label.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        #Student name
        student_name=Label(left_frame,text="Student Name:",font=("sans-serif",15,"bold"),fg="#21478a")
        student_name.grid(row=1,column=0,padx=10,sticky=W)

        student_name=Entry(left_frame,width=20,textvariable=self.var_name,font=("sans-serif",15),fg="black")
        student_name.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        #roll no
        roll_no=Label(left_frame,text="Roll No:",font=("sans-serif",15,"bold"),fg="#21478a")
        roll_no.grid(row=2,column=0,padx=10,sticky=W)

        roll_no=Entry(left_frame,width=20,textvariable=self.var_roll,font=("sans-serif",15),fg="black")
        roll_no.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #department
        dep_name=Label(left_frame,text="Department:",font=("sans-serif",15,"bold"),fg="#21478a")
        dep_name.grid(row=3,column=0,padx=10,sticky=W)

        dep_name=Entry(left_frame,width=20,textvariable=self.var_dep,font=("sans-serif",15),fg="black")
        dep_name.grid(row=3,column=1,padx=10,pady=15,sticky=W)

        #time 
        time_label=Label(left_frame,text="Time:",font=("sans-serif",15,"bold"),fg="#21478a")
        time_label.grid(row=4,column=0,padx=10,sticky=W)

        time_label=Entry(left_frame,width=20,textvariable=self.var_time,font=("sans-serif",15),fg="black")
        time_label.grid(row=4,column=1,padx=10,pady=15,sticky=W)

        #Date
        date_label=Label(left_frame,text="Date:",font=("sans-serif",15,"bold"),fg="#21478a")
        date_label.grid(row=5,column=0,padx=10,sticky=W)

        date_label=Entry(left_frame,width=20,textvariable=self.var_date,font=("sans-serif",15),fg="black")
        date_label.grid(row=5,column=1,padx=10,pady=15,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("sans-serif",15,"bold"),fg="#21478a")
        student_attend_label.grid(row=6,column=0,padx=7,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,width=23,textvariable=self.var_attend,font=("sans-serif",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=6,column=1,padx=5,pady=5,sticky=W)


        #button frame 1
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=450,width=619,height=45)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        update_btn.grid(row=0,column=2)

        delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("sans-serif",15,"bold"),fg="#21478a")
        reset_btn.grid(row=0,column=4)


         
        #right lable frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendace Information",font=("sans-serif",18,"bold"),fg="#21478a")
        right_frame.place(x=680,y=20,width=775,height=620)

        scroll_x=ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(right_frame,column=("ID","roll no","name","department","time","date","attendance"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("0",text="Std-ID")
        self.AttendanceReportTable.heading("1",text="Roll.No")
        self.AttendanceReportTable.heading("2",text="Std-Name")
        self.AttendanceReportTable.heading("3",text="Department")
        self.AttendanceReportTable.heading("4",text="Time")
        self.AttendanceReportTable.heading("5",text="Date")
        self.AttendanceReportTable.heading("6",text="Attend-status")
        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
       
       
        #===============fetch data=================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)



#==============import csv==============================
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
#=============export csv=====================
    def exportCsv(self):

        try:
            if len(myData)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","You data is exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attend.set(rows[6])

#=================update csv======================
    def update_data(self):
            if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
                messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(username='root', password='aarya',host='localhost',database='face_recognition',port=3306)
                        my_cursor = conn.cursor()
                        my_cursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                                                                                                                                                                        self.var_id.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_time.get(),
                                                                                                                                                                        self.var_date.get(),
                                                                                                                                                                        self.var_attend.get(),
                                                                                                                                                                        self.var_id.get()  
                                                                                                                                                                    ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                    conn.commit()
                    self.fetchData()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
 #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_dep.set("")
        self.var_attend.set("Status")




if __name__ == "__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop() 