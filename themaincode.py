from tkinter import *
import pyttsx3 as p
text_speech=p.init()
def texttospeech():
    
    text1=ew1.get()
    text_speech.say(text1)
    text_speech.runAndWait()
    string.set("")
    
    
def quit1():
    root.destroy()

root=Tk()
root.geometry("644x444")
root.title("Audible Text")
#root.wm_iconbitmap("icon1.ico")
root.configure(bg="#e5e5e5") 
Label(root,text="Synthesized Voice",  fg="#990100",bg="#e5e5e5" ,font=("Arial Rounded MT Bold",20)).pack()
string=StringVar()
ew1=Entry(root,textvariable=string,font=("Times New Roman",16),fg="#000000",bg="#ffffff")
ew1.pack(pady=140)
button1=Button(root, text="Speak",bg="#990100",fg="#f6f6f6",padx=10,pady=10,command=texttospeech)
button1.pack()
button2=Button(root, text="Quit", bg="#990100",fg="#f6f6f6",padx=10,pady=10, command=quit1)
button2.pack(side="bottom", anchor="se")
root.mainloop()
