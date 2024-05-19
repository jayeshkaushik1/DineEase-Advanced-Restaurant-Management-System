from tkinter import*
import tkinter.messagebox
root1 = Tk()
root1.geometry("720x720+0+0")
root1.title("Login Page")

name=StringVar()
password=StringVar()
captcha=StringVar()

j=chr(random.randint(45,99))
k=chr(random.randint(45,99))
i=chr(random.randint(45,99))
CAPTCHA=str(random.randint(10,99))+i+k+str(random.randint(1,9))+j
def enter():
	if name.get() == "LUCIFER_3311" and password.get() == "JAYESH":
    if CAPTCHA==captcha.get():
      root1.destroy()
      import Restaurantbilling
    else:
      tkinter.messagebox.showinfo('Error','Authentication Failed')
      name.set("")
      password.set("")
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		name.set("")
		password.set("")	

def destroy():
	root1.destroy()	


label = Label(root1, font = ('arial',30,'bold'), text ="Login Page", fg = "steel blue", bd = 10)
label.grid(row = 0)

label1 = Label(root1, text="Name",)
label2 = Label(root1,text="Password")
label3=Label(root1,text="CAPTCHA:")
label4 = Label(root1,text=CAPTCHA)
label5 = Label(root1,text="ENTER CAPTCHA:")
	
entry1 = Entry(root1,textvariable=name)
entry2 = Entry(root1,textvariable=password)
entry5=Entry(root1,textvariable=captcha)

label1.grid(row=1, column=1)        
label2.grid(row=2,column=1)
label3.grid(row=3,column=1)
label4.grid(row=3,column=2)
label5.grid(row=4,column=1)

entry1.grid(row=1,column=2)
entry2.grid(row=2,column=2)
entry5.grid(row=4,column=2)

enterbtn = Button(root1, text="Enter", command= enter)
enterbtn.grid(row=3, column=1)

exitbtn = Button(root1, padx= 12, text="Exit", command= destroy)
exitbtn.grid(row=3,column=2)

root1.mainloop()
