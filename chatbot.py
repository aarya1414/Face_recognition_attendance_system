from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class chatbot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("730x630+0+0")
        self.root.title("Face Recoginition System")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=1500)
        main_frame.pack()

        img_chat=Image.open(r"C:\Users\Lenovo\Desktop\face recognition\Images\bot.png")
        img_chat=img_chat.resize((160,80),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT WITH ME',font=("Franklin Gothic Demi",30,"bold"),bg="white",fg="#4c8aed")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=("sans-serif",14,"bold"),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='powder blue',width=1500)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("sans-serif",15,"bold"),bg="white",fg="black")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=("sans-serif",14,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=("sans-serif",14,"bold"),width=5)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=("sans-serif",14,"bold"),width=5)
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=("sans-serif",15,"bold"),bg="white",fg="black")
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)


    #==============function declaration====================

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')



    def send(self):
        send='\t\t\t'+ 'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg="Please enter some input!"
            self.label_11.config(text=self.msg,fg="black")

        else:
            self.msg=""
            self.label_11.config(text=self.msg,fg="black")

        if(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+ 'Bot: Hi')
        
        elif(self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+ 'Bot: Hello')

        
        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+ 'Bot: I am Good.\n What about you?')

        
        elif(self.entry.get()=='I am good. Thank you.'):
            self.text.insert(END,'\n\n'+ 'Bot: Nice to hear that.')

        
        elif(self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+ 'Bot: Aarya did!')

        
        elif(self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+ 'Bot: My name is Astor!')

        
        elif(self.entry.get()=='What is face recognition?'):
            self.text.insert(END,'\n\n'+ 'Bot: Face recognition is a technology \ncapable of identifying or verifying \na subject through an image, video \nor any audiovisual element of \nhuman face.')

        elif(self.entry.get()=='What is chatbot?'):
            self.text.insert(END,'\n\n'+ 'Bot: A computer program designed to simulate\n conversation with human users,\n especially over the internet.')

        elif(self.entry.get()=='How does face recognition work step by step?'):
            self.text.insert(END,'\n\n'+ 'Bot: Step 1: Face detection. The camera detects\n and locates the image of a face,\n either alone or in a crowd. ...\nStep 2: Face analysis. Next, an image of the\n face is captured and analyzed. ..\nStep 3: Converting the image to data. ...\nStep 4: Finding a match.') 

        elif(self.entry.get()=='What is python programming language'):
            self.text.insert(END,'\n\n'+ 'Bot: Python is an interpreted, object-oriented,\n high-level programming language with dynamic\n semantics')

        elif(self.entry.get()=='How many languages can you speak?'):
            self.text.insert(END,'\n\n'+ 'Bot: I can only speak english.')

        elif(self.entry.get()=='Flip a coin'):
            self.text.insert(END,'\n\n'+ 'Bot: It is heads!')

        elif(self.entry.get()=='Thank you'):
            self.text.insert(END,'\n\n'+ 'Bot: Welcome!')

        elif(self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+ 'Bot: Bye!\n It was great talking to you!')

        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didnt get it!")



        










if __name__ == "__main__":
    root=Tk()
    obj=chatbot(root)
    root.mainloop()        