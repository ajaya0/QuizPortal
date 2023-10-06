# Type on xampp sql : mysql -u root -p
# or type  mysql.exe -u root --password
# or open cmd and goto xampp -> mysql ->bin
#database sujit_sir
#table quiz
from tkinter import *
import pymysql
from tkinter import ttk, messagebox
import json
import mailbox as mb

def Login ():
	user = Luser.get ()
	password =  Lpwd.get ()
	print ("user id", user,  "password=", password)
	conobj = pymysql.connect(host='localhost', user='root', password= '')
	curobj= conobj.cursor()
	curobj.execute('use sujit_sir;')
	test = f'select * from quiz where uid = "{user}" and pass= "{password}";'
	curobj.execute(test) 
	record = curobj.fetchall () 
	if len (record) : 
		#print ("welcome to home page ")
		messagebox.showinfo ( "Title", "Welcome to home page")
		win.destroy()
		from mcq import myQuiz
		quiz = myQuiz()
	else : 
		#print ("try again")
		messagebox.showinfo ( "my message ", "Try Again")
		win.destroy() 

	curobj.close()
	conobj.close()

def Exit():
    win.destroy()   
def Newuser():
    win1=Tk()
    win1.title("Sign Up page")
    win1.maxsize(500,600)
    win1.minsize(500,600)

    Label(win1,text="Plese Sign Up",font=("Bell Mt",20),fg='black',width="50",height="3").place(x=-160,y=30)

    Label(win1,text="FirstName",font=("Bell Mt",15),fg='black',width="15",height="1").place(x=20,y=150)
    FName=Entry(win1,font=("Bell MT",15),bg="white",fg="black",width=20)
    FName.place(x=230,y=150)

    Label(win1,text="LastName",font=("Bell Mt",15),fg='black',width="15",height="1").place(x=15,y=200)
    LName=Entry(win1,font=("Bell MT",15),bg="white",fg="black",width=20)
    LName.place(x=230,y=200)

    Label(win1,text="UserId",font=("Bell Mt",15),fg='black',width="15",height="1").place(x=0,y=250)
    UId=Entry(win1,font=("Bell MT",15),bg="white",fg="black",width=20)
    UId.place(x=230,y=250)

    Label(win1,text="Gender",font=("Bell Mt",15),fg='black',width="15",height="1").place(x=0,y=300)
    Gender=Entry(win1,font=("Bell MT",15),bg="white",fg="black",width=20)
    Gender.place(x=230,y=300)

    Label(win1,text="Password",font=("Bell Mt",15),fg='black',width="15",height="1").place(x=10,y=350)
    Pass=Entry(win1,font=("Bell MT",15),bg="white",fg="black",width=20)
    Pass.place(x=230,y=350) 

    def submit():
        a=FName.get()
        b=LName.get()
        c=UId.get()
        d=Gender.get()
        e=Pass.get()

        con=pymysql.connect(host="localhost",user="root",password="",database="sujit_sir")
        cur=con.cursor()
        
        insert='insert into quiz values("{fname}","{lname}","{uid}","{gender}","{password}");'
        insert2=insert.format(fname=a,lname=b,uid=c,gender=d,password=e)
        cur.execute(insert2)

        con.commit()
        cur.close()
        con.close() #close the interface
        clear() #clear the input box
        switch() #destroy the signup page
                    
    def switch():
        win1.destroy()


#Function clear all the input box
    def clear():
        FName.delete(0,END)
        LName.delete(0,END)
        UId.delete(0,END)
        Gender.delete(0,END)
        Pass.delete(0,END)

    Button(win1,text="Submit",font=("Bell MT",10),bg="white",fg="black",width="10",height="0",command=submit).place(x=75,y=430)

    Button(win1,text="Clear",font=("Bell MT",10),bg="white",fg="black",width="10",height="0",command=clear).place(x=240,y=430)
    
    Button(win1,text="Switch to login",font=("Bell MT",10),bg="white",fg="black",width="10",height="0",command=switch).place(x=380,y=10)


    win1.mainloop()

win=Tk()
win.title("Home page !!!")
win.geometry('900x400')
win.maxsize(500,600)
win.minsize(500,600)

Label(win,text="Plese Login Here",font=("Bell Mt",25),fg='black',width="50",height="2").place(x=-230,y=80)


Label(win,text="User Id",font=("Bell Mt",20),fg='black',width='10',height="1").place(x=60,y=200)
Luser=Entry(win,font=("Bell Mt",20),bg='white',fg='black')
Luser.place(x=250,y=200,width=200)

Label(win,text="Password",font=("Bell Mt",20),fg='black',width='10',height="1").place(x=70,y=250)
Lpwd=Entry(win,font=("Bell Mt",20),bg='white',fg='black')
Lpwd.place(x=250,y=250,width=200)

Button(win,text="Login",font=("Bell Mt",10),bg='white',fg='black',width='10',height='1',command=Login).place(x=100,y=320)

Button(win,text="Exit",font=("Bell Mt",10),bg='white',fg='black',width='10',height='1',command=Exit).place(x=240,y=320)

Button(win,text="Sign up",font=("Bell Mt",10),bg='white',fg='black',width='10',height='0',command=Newuser).place(x=380,y=10)
win.mainloop()
