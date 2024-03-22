from msilib import RadioButtonGroup
from msilib.schema import RadioButton
from tkinter import *
from tkinter.ttk import LabeledScale
k=0
def vajuta():
    global k
    k+=1
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k) 
def tst_psse(event):
    t=textbox.get() 
    pealkiri.configure(text=t,width=len(t)) 
    textbox.delete(0,END)
def valik():
    arv=var.get()
    textbox.insert(END,arv)

aken=Tk() 
aken.geometry("400x600") 
aken.iconbitmap('love.ico') 
aken.title("Tkinteri kasutamine")
tekst="Pealkiri\n"
pealkiri=Label(aken,
               text=tekst,
               bg="#fadadd",
               fg="#e0ffff",
               font="Algerian 20",
               height=3,width=len(tekst), 
               cursor="watch") 
textbox=Entry(aken,
              bg="#133337",
              fg="#ff7373",
              font="Algerian 20",
              width=20,
              justify=CENTER) #show="*"
nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED,
            bg="darkred",            
            command=vajuta) #SUNKEN, GROOVE
f=Frame(aken)
var=IntVar() #StringVar() BooleanVar()
e=Radiobutton(f,text="Esimene",variable=var,value=1,font="Algerian 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Algerian 20",command=valik)
k_=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Algerian 20",command=valik)

nupp.bind("<Button-3>",vajuta_) #PKM
textbox.bind("<Return>",tst_psse) #ENTER

obj=[pealkiri, textbox, nupp, f]
for i in obj:
    i.pack()
obj2=[e, t, k_] 
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)
aken.mainloop()

