from tkinter import *
import tkinter.messagebox as tmsg

def love():
    n=name1value.get()
    b=name2value.get()
    if n==0  or b==0 :
        tmsg.showinfo("ERROR","PLEASE ENTER VALUE")
    else:
        n=name1value.get()
        b=name2value.get()
        e=n/(b/100)**2
        a=round(e,2)
        name3entry.insert(0,a)
        if a>25:
            tmsg.showwarning("WARNING","YOU ARE OVER WEIGHT")
        elif a<18:
            tmsg.showwarning("WARNING","YOU ARE UNDER WEIGHT")        
        print(a)

root=Tk()
root.geometry("555x450")
root.title("BMI CAlCULATOR")
Label(root,text="BMI CALCULATOR",font=("Bold 20"),bg="yellow",pady=15,padx=15,relief="sunken").grid(row=0,column=2)

name1=Label(root,text="ENTER YOUR WEIGHT (in KG) :",font=("Bold 15"),pady=20,padx=30)
name2=Label(root,text="ENTER YOUR HEIGHT (in CM) :",font=("Bold 15"),pady=20,padx=30)
name3=Label(root,text="BMI:",pady=20,padx=30,font=("Bold 15"))

name1.grid(row=10,column=2)
name2.grid(row=20,column=2)
name3.grid(row=30,column=2)

name1value=IntVar()
name2value=IntVar()

name1entry=Entry(root,textvariable=name1value)
name2entry=Entry(root,textvariable=name2value)
name3entry=Entry(root)

name1entry.grid(row=10,column=3)
name2entry.grid(row=20,column=3)
name3entry.grid(row=30,column=3)

button=Button(root,text="GO",command=love,relief="sunken",padx=30,pady=5)
button.grid(row=60,column=2)

root.mainloop()
