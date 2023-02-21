from tkinter import *
from os import *

def Q1():
    system("智商大闯关Q1.py")
    root.quit()

def Q2():
    system("智商大闯关Q2.py")
    root.quit()

def Q3():
    system("智商大闯关Q3.py")
    root.quit()

def Q4():
    system("智商大闯关Q4.py")
    root.quit()

def back():
    system("选关.py")
    root.quit()

root = Tk(className='智商大闯关')
root.geometry('500x200')
root.resizable(0,0)

l1 = Label(text='点击下方按钮选关吧！！！').pack()
b1 = Button(text='Q1',command=Q1).place(x=40,y=40)
b2 = Button(text='Q2',command=Q2).place(x=80,y=40)
b3 = Button(text='Q3',command=Q3).place(x=120,y=40)
b4 = Button(text='Q4',command=Q4).place(x=160,y=40)

B_button = Button(text='返回普通模式',command=back).pack()

root.mainloop()