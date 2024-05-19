from tkinter import*
import random
import time

root = Tk()

root.geometry("1500x800+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,width =1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 1600,height=700)
f1.pack()

#TIME
localtime=time.asctime()
#INFO TOP
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)


def Ref():
    x=random.randint(12980, 50876)
    randomRef ="Ind"+str(x)
    rand.set(randomRef)
    if Fries.get()=="":
        costoffries=0
    else:
        costoffries=float(Fries.get())*80
    if Lunchmeal.get()=="":
        costofLunchmeal=0
    else:
        costofLunchmeal =float(Lunchmeal.get())*140
    if Burger.get()=="":
        costofburger=0
    else:
        costofburger = float(Burger.get())*90
    if Filet.get()=="":
        costoffilet=0   
    else:
        costoffilet = float(Filet.get())*190
    if Chinesemeal.get()=="":
        costofchinesemeal=0
    else:
        costofchinesemeal = float(Chinesemeal.get())*160
    if Coke.get()=="":
        costofcoke=0
    else:
        costofcoke = float(Coke.get())*70

    costofmeal = "Rs.",str(costoffries +  costofLunchmeal + costofburger + costoffilet + costofchinesemeal + costofcoke)
    PayTax=((costoffries +  costofLunchmeal + costofburger + costoffilet +  costofchinesemeal + costofcoke)*0.25)
    Totalcost=(costoffries +  costofLunchmeal + costofburger + costoffilet  + costofchinesemeal + costofcoke)
    Ser_Charge=((costoffries +  costofLunchmeal + costofburger + costoffilet + costofchinesemeal + costofcoke)/98)
    Service="Rs.",str(round(Ser_Charge))
    OverAllCost="Rs.",str( round(PayTax + Totalcost + Ser_Charge))
    PaidTax="Rs.",str(PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def sexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Lunchmeal.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Coke.set("")
    Tax.set("")
    cost.set("")
    Chinesemeal.set("")





rand = StringVar()
Fries = StringVar()
Lunchmeal = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Coke = StringVar()
Tax = StringVar()
cost = StringVar()
Chinesemeal = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLunchmeal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
lblLunchmeal.grid(row=2,column=0)
txtLunchmeal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lunchmeal , bd=6,bg="powder blue" ,justify='right')
txtLunchmeal.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)

lblChineseMeal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Chinese Meal",fg="steel blue",bd=10,anchor='w')
lblChineseMeal.grid(row=5,column=0)
txtChineseMeal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Chinesemeal , bd=6,bg="powder blue" ,justify='right')
txtChineseMeal.grid(row=5,column=1)

lblCoke = Label(f1, font=( 'aria' ,16, 'bold' ),text="Coke",fg="steel blue",bd=10,anchor='w')
lblCoke.grid(row=0,column=2)
txtCoke= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Coke , bd=6,bg="powder blue" ,justify='right')
txtCoke.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,bg="dodger blue" ,justify='right')
txtTotal.grid(row=5,column=3)

#buttons
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=sexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="140", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="190", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chinese Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="160", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 10, 'bold'), text="Coke", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()
def calci():
    import Calculator

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)
btncalci=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="CALCULATOR", bg="powder blue",command=calci)
btncalci.grid(row=7, column=4)

root.mainloop()
