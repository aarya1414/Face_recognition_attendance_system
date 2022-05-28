from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

        #bg image
        img=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\t.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_1b1=Label(self.root,image=self.photoimg)
        f_1b1.place(x=0,y=0,width=1530,height=790)

     


        title_1b1=Label(self.root,text="TRAIN DATASET",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)


        #button
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_clf,font=("Franklin Gothic Demi",20,"bold"),fg="#3d3737",bg="#ededed")
        b1_1.place(x=580,y=730,width=400,height=40)


    def train_clf(self):
        data_dir=(r"C:\Users\Lenovo\Desktop\face recognition\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

            #===========train clf===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\Lenovo\Desktop\face recognition\classifier.xml")
        messagebox.showinfo("Result","Training dataset Completed",parent=self.root)
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset Completed",parent=self.root)
        
  



if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()  