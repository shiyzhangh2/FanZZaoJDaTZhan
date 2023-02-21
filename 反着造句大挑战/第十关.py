from tkinter import *
from os import *
def main():
    root = Tk(className='第十关')
    root.geometry('475x400')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 Let us clean the windows!')
    l_tip2 = Label(text = '(请自行退出)')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'Let u')

    def _show_2():
        e.insert(0, 's ')

    def _show_3():
        e.insert(0, 'clean the ')

    def _show_4():
        e.insert(0, 'windows!')

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

    l = Label(text='第十关：终于摆脱他了吗?').pack()
    la_1 = Label(text='(不能输入 请倒着再倒着(意思就是正着按)输入答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='windows!', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='clean the', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='s', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='Let u', command=_show_4)
    b_show_4.pack()

    b_AI = Button(root, text='点击查看 答案', command=_show_AI)
    b_AI.pack()

    b_clear = Button(root, text='清空', command=_clear)
    b_clear.pack()

    b_ak = Button(root, text='返回选关', command=back)
    b_ak.pack()

    mainloop()
if __name__ == '__main__':
    main()