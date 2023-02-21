from tkinter import *
from os import *

def _1_():
    system("第一关.py")
    root.quit()

def _2_():
    system("第二关.py")
    root.quit()

def _3_():
    system("第三关.py")
    root.quit()

def Boss_1():
    system("BOSS_1.py")
    root.quit()

def _4_():
    system("第四关.py")
    root.quit()

def _5_():
    system("第五关.py")
    root.quit()

def _6_():
    system("第六关.py")
    root.quit()

def Boss_2():
    system("BOSS_2.py")
    root.quit()

def _7_():
    system("第七关.py")
    root.quit()

def _8_():
    system("第八关.py")
    root.quit()

def _9_():
    system("第九关.py")
    root.quit()

def Boss_3():
    system("BOSS_3.py")
    root.quit()

def _10_():
    system("第十关.py")
    root.quit()

def _11_():
    system("第十一关.py")
    root.quit()

def ZSDCG():
    system("智商大闯关.py")
    root.quit()

def NJJZW():
    system("闹筋急转弯.py")
    root.quit()

def SZDT():
    system("死宅答题.py")
    root.quit()

root = Tk(className='反着造句大挑战 V4.2.')
root.geometry('500x300')
root.resizable(0,0)

l1 = Label(text='点击下方按钮选关吧！！！').pack()
l2 = Label(text='————————————————模式—————————————————').place(x=25,y=180)

b1 = Button(text='1',command=_1_).place(x=40,y=40)
b2 = Button(text='2',command=_2_).place(x=80,y=40)
b3 = Button(text='3',command=_3_).place(x=120,y=40)
b_BOSS_1 = Button(text='BOSS!!!去死吧！！！(第一阶)',command=Boss_1).place(x=10,y=80)
b4 = Button(text='4',command=_4_).place(x=40,y=120)
b5 = Button(text='5',command=_5_).place(x=80,y=120)
b6 = Button(text='6',command=_6_).place(x=120,y=120)
b_BOSS_2 = Button(text='BOSS!!!去死吧！！！(第二阶)',command=Boss_2).place(x=10,y=160)
b7 = Button(text='7',command=_7_).place(x=325,y=40)
b8 = Button(text='8',command=_8_).place(x=365,y=40)
b9 = Button(text='9',command=_9_).place(x=405,y=40)
b_BOSS_3 = Button(text='BOSS!!!去死吧！！！(第三阶)',command=Boss_3).place(x=295,y=80)
b10 = Button(text='10',command=_10_).place(x=325,y=120)
b11 = Button(text='11',command=_11_).place(x=365,y=120)

ZSDCG_button = Button(text='智商大闯关模式',command=ZSDCG).place(x=40,y=200)
NJJZW_button = Button(text='闹筋急转弯',command=NJJZW).place(x=160,y=200)
SZDT_button = Button(text='死宅答题',command=SZDT).place(x=260,y=200)

root.mainloop()

