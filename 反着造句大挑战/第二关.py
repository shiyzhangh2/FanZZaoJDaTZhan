from tkinter import *
from os import *
def main():
    root = Tk(className='第二关')
    root.geometry('350x350')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 Do you like beef?')
    l_tip2 = Label(text = '(请自行退出)')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'you like')

    def _show_2():
        e.insert(0, 'Do')


    def _show_3():
        e.insert(0, 'ef?')

    def _show_4():
        e.insert(0, 'be')

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

    l = Label(text='第二关：嘿嘿嘿').pack()
    l_tip = Label(text='(不能输入 请倒着输入答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='you like', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='Do', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='ef?', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='be', command=_show_4)
    b_show_4.pack()

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