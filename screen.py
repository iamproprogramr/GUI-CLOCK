from tkinter import *
from tkinter import messagebox
from time import strftime


screen= Tk()
screen.geometry("300x360")
screen.title("CLOCK BY MUHAMMAD YOUSAF")
screen.iconbitmap('icon.ico')
c=Canvas(screen,bg="#ADD8E6",height=200,width=200)
filename=PhotoImage(file="bg.png")
bg_label=Label(screen,image=filename)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

c.pack()

custom_font = ("Helvetica", 30, "bold")

time_label = Label(screen, font=custom_font,bg="white")
time_label.place(x=15,y=30)
time_label.pack()

def time():
    # Get the current time, day, and date
    time_string = strftime("%I:%M:%S %p")
    day_string = strftime("%A")
    date_string = strftime("%d, %m, %Y")
    
    # Update the labels
    time_label.config(text=time_string + "\n" + day_string + "\n" + date_string)
    time_label.after(1000, time)
    time_label.place(x=30,y=90)
time()


text_font=("arial",20,"bold")



screen.mainloop()
