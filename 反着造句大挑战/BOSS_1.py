from tkinter import *
from os import *
def main():
    root = Tk(className='打打BOSS关')
    root.geometry('500x500')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 Where is it?')
    l_tip2 = Label(text = '(请自行退出)')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'W')

    def _show_2():
        e.insert(0, 'r')

    def _show_3():
        e.insert(0, 'h')

    def _show_4():
        e.insert(0, 'i')

    def _show_5():
        e.insert(0, 'e')

    def _show_6():
        e.insert(0, 's')

    def _show_7():
        e.insert(0, 't')

    def _show_8():
        e.insert(0, '?')

    def _show_():
        e.insert(0, ' ')

    def _show_AI():
        l_AI.pack()
        l_tip2.pack()
    # 清空e输入框中的内容
    def _clear():
        e.delete(0, END)

    def back():
        system('选关.py')
        root.quit()
    content = StringVar()

    l = Label(text='BOSS关：文字勇士出现了！！！').pack()
    la_1 = Label(text='(不能输入 请倒着输入答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='W', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='r', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='h', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='i', command=_show_4)
    b_show_4.pack()

    b_show_5 = Button(root, text='e', command=_show_5)
    b_show_5.pack()

    b_show_6 = Button(root, text='s', command=_show_6)
    b_show_6.pack()

    b_show_7 = Button(root, text='t', command=_show_7)
    b_show_7.pack()

    b_show_8 = Button(root, text='?', command=_show_8)
    b_show_8.pack()

    b_show = Button(root, text='点击我显示 空格 ', command=_show_)
    b_show.pack()

    b_AI = Button(root, text='点击查看答案', command=_show_AI)
    b_AI.pack()

    b_clear = Button(root, text='清空', command=_clear)
    b_clear.pack()

    b_ak = Button(root, text='返回选关', command=back)
    b_ak.pack()

    mainloop()
if __name__ == '__main__':
    main()