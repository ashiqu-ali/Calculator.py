from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root,width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

#clear function
def button_clear():
    e.delete(0,END)

#add button
def button_add():
    num1 = e.get()
    global fnum
    global math
    math='add'
    fnum = int(num1)
    e.delete(0,END)

#equals
def button_equal():
    num2=e.get()
    e.delete(0,END)
    if math == 'add':
        e.insert(0,fnum+int(num2))

    elif math=='sub':
        e.insert(0,fnum-int(num2))

    elif math=='mul':
        e.insert(0,fnum*int(num2))

    elif math=='div':
        e.insert(0,fnum/int(num2))

    

def button_subs():
    num1 = e.get()
    global fnum
    global math
    math='sub'
    fnum = int(num1)
    e.delete(0,END)

def button_mul():
    num1 = e.get()
    global fnum
    global math
    math='mul'
    fnum = int(num1)
    e.delete(0,END)

def button_div():
    num1 = e.get()
    global fnum
    global math
    math='div'
    fnum = int(num1)
    e.delete(0,END)
    
#button
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))
button_ad = Button(root,text='+',padx=39,pady=20,command=button_add)
button_sub = Button(root,text='-',padx=42,pady=20,command=button_subs)
button_mu = Button(root,text='x',padx=40,pady=20,command=button_mul)
button_di = Button(root,text='/',padx=40,pady=20,command=button_div)
button_eq = Button(root,text='=',padx=91,pady=20,command=button_equal)
button_clear = Button(root,text='Clear',padx=79,pady=20,command=button_clear)

# buttons on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_ad.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_eq.grid(row=5,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mu.grid(row=6,column=1)
button_di.grid(row=6,column=2)

root.mainloop()