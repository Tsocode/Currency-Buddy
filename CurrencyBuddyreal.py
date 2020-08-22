from tkinter import Tk, StringVar, ttk
from tkinter import *
import time
import datetime
import tkinter.messagebox

root = Tk()
photo = PhotoImage(file="2020-08-20 (2).png")
label = Label(root, image=photo)
label.pack()
root.title("Currency Buddy")
root.geometry('800x400+0+0')
root.configure(background ="green")

LeftMF = Frame(root, width = 400, height = 200, bd=4,relief="raise")
LeftMF.pack(side=LEFT)
RightMF = Frame(root, width = 400, height = 100, bd=4,relief="raise")
RightMF.pack(side=RIGHT)

calc = Frame(root)
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

def ConCurrency():
    if value0.get() == 'USA':
        convert1 = float (convert.get() * 0.0026)
        convert2 = 'USD', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'England':
        convert1 = float (convert.get() * 0.0020)
        convert2 = 'GBP', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Rwanda':
        convert1 = float (convert.get() * 2.49)
        convert2 = 'RWF', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Uganda':
        convert1 = float (convert.get() * 9.500)
        convert2 = 'UGX', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Togo':
        convert1 = float (convert.get() * 1.43)
        convert2 = 'XOF', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Kenya':
        convert1 = float (convert.get() * 0.28)
        convert2 = 'KES', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Brazil':
        convert1 = float (convert.get() * 0.0014)
        convert2 = 'BLR', str('%.5f'%(convert1))
        currency.set(convert2)
    elif value0.get() == 'Canada':
        convert1 = float (convert.get() * 0.0034)
        convert2 = 'CAD', str('%.5f'%(convert1))
        currency.set(convert2)

def Ex():
    iEx = tkinter.messagebox.askyesno("Currency Buddy", "Confirm if you want to exit")
    if iEx > 0:
        root.destroy()
        return

def Reset():
    value0.set("")
    convert.set("0.00")
    currency.set("0.00")

Currency = Entry(LeftMF,font=('times',20,'bold'),textvariable=convert,relief='raise', bd=2,width=19,justify='center')
Currency.grid(row=0,column=1)

Naira = Label(LeftMF,font=('times',20,'bold'),text='Naira',padx=1,pady=1,bd=2,relief='raise',fg='black',width=13)
Naira.grid(row=0,column=2,sticky=W)

#combo box
countries = ttk.Combobox(LeftMF,textvariable = value0, state='readonly', font=('times',20,'bold'),width=13,justify= CENTER)
countries['values'] = ('','USA','Brazil','Canada','England','Togo','Uganda','Rwanda')
countries.current(0)
countries.grid(row=4, column=2)

Showcurrency= Label(LeftMF,font=('times',20,'bold'),textvariable=currency,bd=2,width=17,justify='center',
                   bg='white',pady=1,padx=1,relief='raise')
Showcurrency.grid(row=4,column=1)

#======================================================================================================================
menubar = Menu(calc)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label= "Conversion rates")
filemenu.add_command(label= "Update")
filemenu.add_separator()
filemenu.add_command(label= "Exit", command = Ex)


editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label= "Cut")
editmenu.add_command(label= "Copy")
editmenu.add_separator()
editmenu.add_command(label= "Paste")

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label= "View")

btnConvert = Button(RightMF, text='Convert',padx=0,pady=0,bd=1,fg='black',
                  font=('times',20,'bold'),width=6,height=1,command=ConCurrency,relief='raise').grid(row=1,column=0)

btnReset = Button(RightMF, text='Reset',padx=0,pady=0,bd=1,fg='black',
                  font=('times',20,'bold'),width=6, height=1,command=Reset,relief='raise').grid(row=2,column=0)

btnExit = Button(RightMF,text='Exit',padx=0,pady=0,bd=1,fg='black',
                 font=('times',20,'bold'),width=6, height=1,command=Ex,relief='raise').grid(row=3,column=0)

root.configure(menu=menubar)
root.mainloop()

