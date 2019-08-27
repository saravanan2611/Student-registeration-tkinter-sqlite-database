from tkinter import *
import sqlite3
import datetime
from time import ctime

root = Tk() 
root.title("STUDENT REGISTRATION FORM")
root.geometry("750x750")

def database():
    name=NAME.get()
    rollno=ROLLNO.get()
    dob=DATE_OF_BIRTH.get()
    gender=var.get()
    subjects=var1.get()
    yos=var4.get()
    semester=var5.get()
    department=var6.get()
    time=ctime()
    conn = sqlite3.connect('mysrf.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS SRF (NAME TEXT, ROLLNO TEXT, DATE_OF_BIRTH TEXT, GENDER TEXT, SUBJECTS TEXT, YEAR_OF_STUDY TEXT, SEMESTER TEXT, DEPARTMENT TEXT,TIME TEXT)')
        cursor.execute('INSERT INTO SRF (NAME,ROLLNO,DATE_OF_BIRTH,GENDER,SUBJECTS,YEAR_OF_STUDY,SEMESTER,DEPARTMENT,TIME) VALUES(?,?,?,?,?,?,?,?,?)',(name,rollno,dob,gender,subjects,yos,semester,department,time,))

Label1 = Label(root, text = "STUDENT REGISTRATION FORM",font=('Helvetica', '20','bold'))
Label1.place(x=175,y=50)
#Label1.separator(root).place(x=0, y=26, relwidth=1)

NAME = StringVar()
L2 = Label(root,text="NAME", font=('arial','10','bold'), justify=LEFT)
L2.place(x=10,y=170)

E2 = Entry(root,bd=5,font=('arial','10'),textvar=NAME)
E2.place(x=150,y=170)

ROLLNO = StringVar()
L3 = Label(root,text="ROLLNO", font=('arial','10','bold'))
L3.place(x=10,y=220)

E3 = Entry(root,bd=5,font=('arial','10'),textvar=ROLLNO)
E3.place(x=150,y=220)

DATE_OF_BIRTH = StringVar()
L2 = Label(root,text="DATE_OF_BIRTH", font=('arial','10','bold'), justify=LEFT)
L2.place(x=10,y=270)

E2 = Entry(root,bd=5,font=('arial','10'),textvar=DATE_OF_BIRTH)
E2.place(x=150,y=270)


L4 = Label(root,text="GENDER", font=('arial','10','bold'))
L4.place(x=10,y=320)


var = IntVar()

Radiobutton(root, text = "Male", variable = var, value = 1).place(x=150,y=320)
Radiobutton(root, text = "Female", variable = var, value = 2).place(x=200,y=320)

L5 = Label(root,text="SUBJECTS", font=('arial','10','bold'))
L5.place(x=10,y=350)

var1 = IntVar()  
var2 = IntVar()  
var3 = IntVar()  
  
Checkbutton(root, text = "Python", variable = var1, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=150,y=350)  
Checkbutton(root, text = "Maths", variable = var2, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=150,y=390)  
Checkbutton(root, text = "Web", variable = var3, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=150,y=430)  

L6 = Label(root, text="YEAR OF STUDY", font=('arial','10','bold'))
L6.place(x=10,y=480)

var4 = StringVar(root)  
var4.set("Choose year")

OM1 = OptionMenu(root, var4, "1st year", "2nd year", "3rd year", "4th year")
OM1.place(x=150,y=486)

L7 = Label(root, text="SEMESTER", font=('arial','10','bold'))
L7.place(x=10,y=530)

var5 = StringVar(root)
var5.set("Choose Semester")

OM2 = OptionMenu(root, var5, "ODD", "EVEN")
OM2.place(x=150,y=530)

L8 = Label(root, text="DEPARTMENT", font=('arial','10','bold'))
L8.place(x=10,y=570)

var6 = StringVar(root)
var6.set("Choose Department")

OM3 = OptionMenu(root, var6, "CSE", "IT", "MECH", "ECE", "EEE", "EIE", "AERO", "CIVIL")
OM3.place(x=150,y=570)

#def dt():
    #dt = datetime.datetime.now()
    #database()
    
B1 = Button(root,text = "SUBMIT", font=('arial','10','bold'),command=database)  
B1.place(x=200,y=620)
  
root.mainloop()
#command = lambda x:func1() & func2()