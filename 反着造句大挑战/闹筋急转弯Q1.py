from tkinter import *
from os import *
def main():
    root = Tk(className='[Q1]')
    root.geometry('600x400')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 A.3 4(大象：开 装 关  长颈鹿：开 搬 装 关)')
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

    l = Label(text='Q1：请问 把大象装进冰箱需要几步?如果冰箱里只能装下一只动物，那么再把长颈鹿放进冰箱需要几步?').pack()
    la_1 = Label(text='(不能输入 请输入答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='A.3 4', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='B.4 3', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='C.10 3', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='D.4 2', command=_show_4)
    b_show_4.pack()

    b_show_5 = Button(root, text='E.3 5', command=_show_5)
    b_show_5.pack()

    b_AI = Button(root, text='点击查看 答案', command=_show_AI)
    b_AI.pack()

    b_clear = Button(root, text='清空', command=_clear)
    b_clear.pack()

    b_ak = Button(root, text='返回选关', command=back)
    b_ak.pack()

    mainloop()
if __name__ == '__main__':
    main()