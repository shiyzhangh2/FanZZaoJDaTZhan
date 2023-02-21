from tkinter import *
from os import *
def main():
    root = Tk(className='[Q2]')
    root.geometry('550x550')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 D.125(结论：这是一个“兔子数列” 第一个数加后面一个数等于第三个数)')
    l_tip2 = Label(text = '(请自行退出)')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'A')

    def _show_2():
        e.insert(0, 'B')

    def _show_3():
        e.insert(0, 'C')

    def _show_4():
        e.insert(0, 'D')

    def _show_5():
        e.insert(0, 'E')

    def _show_6():
        e.insert(0, 'F')

    def _show_7():
        e.insert(0, 'G')

    def _show_AI():
        l_AI.pack()
        l_tip2.pack()

    # 清空e输入框中的内容
    def _clear():
        e.delete(0, END)

    def back():
        system('智商大闯关.py')
        root.quit()
    content = StringVar()

    l = Label(text='Q2：一串数列是这样的 1,9,10,19,29,48,77,( ) 那么括号里该填下列哪个数才能使数列规律成立?').pack()
    la_1 = Label(text='(不能输入 请输入答案 如果你觉得都不是，请自己写下答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='A.110', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='B.123', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='C.172', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='D.125', command=_show_4)
    b_show_4.pack()

    b_show_5 = Button(root, text='E.201', command=_show_5)
    b_show_5.pack()

    b_show_6 = Button(root, text='F.126', command=_show_6)
    b_show_6.pack()

    b_show_7 = Button(root, text='G.173', command=_show_7)
    b_show_7.pack()

    b_AI = Button(root, text='点击查看 答案', command=_show_AI)
    b_AI.pack()

    b_clear = Button(root, text='清空', command=_clear)
    b_clear.pack()

    b_ak = Button(root, text='返回选关', command=back)
    b_ak.pack()

    mainloop()
if __name__ == '__main__':
    main()