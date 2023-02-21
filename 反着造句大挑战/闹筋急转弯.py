from tkinter import *
from os import *

def Q1():
    system("闹筋急转弯Q1.py")
    root.quit()

def back():
    system("选关.py")
    root.quit()

root = Tk(className='闹筋急转弯')
root.geometry('500x200')
root.resizable(0,0)

l1 = Label(text='点击下方按钮选关吧！！！').pack()
b1 = Button(text='Q1',command=Q1).place(x=40,y=40)

B_button = Button(text='返回普通模式',command=back).pack()

root.mainloop()