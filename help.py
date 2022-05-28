from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import webbrowser

class help:
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

        #title section
        title_1b1=Label(f_1b1,text="HELP DESK",font=("Franklin Gothic Demi",35,"bold"),fg="#21478a")
        title_1b1.place(x=0,y=50,width=1530,height=45)


         # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(f_1b1,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=275,y=200,width=180,height=180)

        std_b1_1 = Button(f_1b1,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#21478a")
        std_b1_1.place(x=275,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\fb.png")
        det_img_btn=det_img_btn.resize((170,170),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(f_1b1,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=525,y=200,width=180,height=180)

        det_b1_1 = Button(f_1b1,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#21478a")
        det_b1_1.place(x=525,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(f_1b1,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=775,y=200,width=180,height=180)

        att_b1_1 = Button(f_1b1,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#21478a")
        att_b1_1.place(x=775,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((170,170),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(f_1b1,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1025,y=200,width=180,height=180)

        hlp_b1_1 = Button(f_1b1,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#21478a")
        hlp_b1_1.place(x=1025,y=380,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://www.google.com/search?q=face+recognition+attendance+system"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)


if __name__ == "__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()  
