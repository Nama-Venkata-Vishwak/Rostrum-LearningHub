from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
root = Tk()
root.title("Rostrum")
width = 640
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
def Database():
   global conn, cursor
   conn = sqlite3.connect("db_member.db")
   cursor = conn.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
def LoginForm():
   global LoginFrame, lbl_result1
   LoginFrame = Frame(root)
   LoginFrame.pack(side=TOP, pady=80)
   Upper_right = Label(LoginFrame,text ='Rostrum Login Page',font=('arial', 20))
   Upper_right.place(y=0,x=210)
   lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
   lbl_username.grid(row=2)
   lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
   lbl_password.grid(row=3)
   lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
   lbl_result1.grid(row=4, columnspan=2)
   lbl = Label(LoginFrame, text="", font=('arial', 18))
   lbl.grid(row=0, column=3)
   username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
   username.grid(row=2, column=1)
   password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
   password.grid(row=3, column=1)
   btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
   btn_login.grid(row=5, columnspan=2, pady=20)
   lbl_register = Label(LoginFrame, text="New to Rostrum? Click Here to Create New Account", fg="Blue", font=('arial', 12))
   lbl_register.grid(row=6, sticky=W)
   lbl_register.bind('<Button-1>', ToggleToRegister)
   USERNAME.set("")
   PASSWORD.set("")
   ##############################################################################################################        Upload Page
Liturature = StringVar()
def Database2():
   global conn2, cursor2, Liturature, UName
   conn = sqlite3.connect("db_member.db")
   cursor = conn.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS `feed2` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, Liturature TEXT, likes INTRGER)")
def Upload(Lit):
   Database2()
   if UName.get() == "":
      lbl_result3.config(text="Name is Empty!!! ", fg="orange")
   else:
         cursor.execute("INSERT INTO `feed2` (username, Liturature, likes) VALUES(?, ?, 0)", (str(UName.get()), str(Lit)))
         conn.commit()
         lbl_result3.config(text="Liturature Successfully Uploaded!", fg="black")
         
UName= StringVar()
def UploadPage():
   Database2()
   global UploadFrame, lbl_result3, USERNAME, Liturature,content,UName
   UploadFrame = Frame(root)
   UploadFrame.pack(side=TOP, pady=20)
   Upper_right = Label(UploadFrame,text ='Rostrum Upload Page',font=('arial', 20))
   Upper_right.grid(row=0, column=0)
   Uname= Entry(UploadFrame,textvariable=UName ,font=('arial', 15) , width=25)
   Uname.grid(row=0, column=1)
   lbl_content = Label(UploadFrame, text="Literature:", font=('arial', 25), bd=18)
   lbl_content.grid(row=1, column=0)
   lbl_result3 = Label(UploadFrame, text="", font=('arial', 18))
   lbl_result3.grid(row=2, columnspan=2)
   content = Text(UploadFrame, font=('arial', 15),height=12 , width=25)
   content.grid(row=1, column=1)
   btn_upload = Button(UploadFrame, text="Upload", font=('arial', 18), width=15,  command=lambda :Upload(content.get("1.0",END)))
   btn_upload.grid(row=3,column=0)
   btn_view = Button(UploadFrame, text="Open Feed Page", font=('arial', 18), width=15,  command=ToggleToView)
   btn_view.grid(row=3,column=1)
   lbl_Logout = Button(UploadFrame, text="Log Out", fg="Blue", font=('arial', 12),command=ToggleToLogout)
   lbl_Logout.grid(row=6, sticky=W)
 
def ToggleToLogout(event=None):
   cursor.close()
   conn.close()
   UploadFrame.destroy()
   LoginForm()
 
def ToggleToUpload(event=None):
   LoginFrame.destroy()
   UploadPage()
##################################################################################################################     View Page
 
Liturature = StringVar()
i=-1
def View():
         global i,val
         i=-1
         cursor.execute("Select Liturature,username,likes,mem_id from `feed2` order by mem_id DESC" )
         val=cursor.fetchall()
         conn.commit()
         Next()
 
def Like():
    global lbl_like,btn_like
    lbl_like['text']='Likes: ' + str(int(val[i][2]+1))
    cursor.execute("Update `feed2` set likes=likes+1 where mem_id=(?)",(str(val[i][3])))
    conn.commit()
    btn_like['state']=DISABLED
    return 0
def Next():
        global i,val,lbl_like,btn_like
        i=i+1
        if(len(val)<=i):
            result2 = tkMessageBox.showinfo('Information', 'No More Lituratures are available')
        else:
         cont.config(text=val[i][0],fg='black')
         uname.config(text=val[i][1],fg='black')
         lbl_like.config(text='Likes: '+str(val[i][2]),fg='black')
         btn_like['state']=NORMAL
        
def ViewPage():
   global ViewFrame, feed, USERNAME, Liturature, cont,uname,lbl_like,btn_like
   ViewFrame = Frame(root)
   ViewFrame.pack(side=TOP, pady=20)
   Upper_right = Label(ViewFrame,text ='Rostrum View Page',font=('arial', 20))
   Upper_right.grid(row=0, column=0)
   uname= Label(ViewFrame,text="", width=10)
   uname.grid(row=0,column=1)
   cont= Label(ViewFrame,text="", font=('arial', 15),wraplength=250,height=12 , width=25)
   cont.grid(row=1,column=0)
   btn_Next = Button(ViewFrame, text="Next Feed", font=('arial', 18), width=15,  command=Next)
   btn_Next.grid(row=2, column=0)
   lbl_like = Label(ViewFrame,text="Likes : 0",font=('arial', 18),width=15)
   lbl_like.grid(row=1,column=1)
   btn_like = Button(ViewFrame,text="Like Feed ", font=('arial', 18), width=15,  command=Like)
   btn_like.grid(row=2, column=1)
   lbl_Logout = Button(ViewFrame, text="Log Out", fg="Blue", font=('arial', 12),command=ToggleToLogout2)
   lbl_Logout.grid(row=3, column=0)
   lbl_upload = Button(ViewFrame, text="Open Upload page", fg="Blue", font=('arial', 12),command=ToggleToUpload2)
   lbl_upload.grid(row=3, column=1)
   View()
def ToggleToLogout2(event=None):
   cursor.close()
   conn.close()
   ViewFrame.destroy()
   LoginForm()
def ToggleToView(event=None):
   UploadFrame.destroy()
   ViewPage()
def ToggleToUpload2(event=None):
   #cursor.close()
   #conn.close()
   ViewFrame.destroy()
   UploadPage()
#################################################################################################################
def RegisterForm():
   global RegisterFrame, lbl_result2
   RegisterFrame = Frame(root)
   RegisterFrame.pack(side=TOP, pady=40)
   Upper_right = Label(RegisterFrame,text ='Rostrum Account Creation Page',font=('arial', 20))
   Upper_right.place(y=0,x=80)
   lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
   lbl_username.grid(row=1)
   lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
   lbl_password.grid(row=2)
   lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
   lbl_firstname.grid(row=3)
   lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
   lbl_lastname.grid(row=4)
   lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
   lbl_result2.grid(row=5, columnspan=2)
   lbl = Label(RegisterFrame, text="", font=('arial', 18))
   lbl.grid(row=0, column=3)
   username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
   username.grid(row=1, column=1)
   password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
   password.grid(row=2, column=1)
   firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
   firstname.grid(row=3, column=1)
   lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
   lastname.grid(row=4, column=1)
   btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
   btn_login.grid(row=6, columnspan=2, pady=20)
   lbl_login = Label(RegisterFrame, text="Already Have an Account? Click here to Login", fg="Blue", font=('arial', 12))
   lbl_login.grid(row=7, sticky=W)
   lbl_login.bind('<Button-1>', ToggleToLogin)
def Exit():
   result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
   if result == 'yes':
      root.destroy()
      exit()
 
def ToggleToLogin(event=None):
   RegisterFrame.destroy()
   LoginForm()
 
 
 
def ToggleToRegister(event=None):
   LoginFrame.destroy()
   RegisterForm()
 
def Register():
   Database()
   if USERNAME.get() == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "":
      lbl_result2.config(text="Please complete the required field!", fg="orange")
   else:
      cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
      if cursor.fetchone() is not None:
         lbl_result2.config(text="Username is already taken", fg="red")
      else:
         cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
         conn.commit()
         USERNAME.set("")
         PASSWORD.set("")
         FIRSTNAME.set("")
         LASTNAME.set("")
         lbl_result2.config(text="Successfully Created!", fg="black")
         #cursor.close()
         #conn.close()
def Login():
   Database()
   if USERNAME.get == "" or PASSWORD.get() == "":
      lbl_result1.config(text="Please complete the required field!", fg="orange")
   else:
      cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
      if cursor.fetchone() is not None:
 
 
         lbl_result1.config(text="You Successfully Login", fg="blue")
         ToggleToUpload()
      else:
         lbl_result1.config(text="Invalid Username or password", fg="red")
LoginForm()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
if __name__ == '__main__':
   root.mainloop()
