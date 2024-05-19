from tkinter import *
from time import strftime
from tkcalendar import *



screen= Tk()
screen.geometry('350x600')
screen.title('CLOCK')
c=Canvas(screen,bg="#ADD8E6",height=200,width=200)
filename=PhotoImage(file="BOG.png")
bg_label=Label(screen,image=filename)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


label = Label(screen, font=("arial", 40),bg='#FFD580')
label.place(x=20,y=30)

def time():
    
    time1 = strftime("%I:%M:%S %p \n %A \n %d,%m,%Y")  
    label.config(text=time1,)
    label.after(1000, time)  

time()  
cal=Calendar(screen,setmode='day',date_pattern='d/m/yy')
cal.pack(padx=20,pady=220)

c.pack()

screen.mainloop()
