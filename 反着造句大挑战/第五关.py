from tkinter import *
from os import *
def main():
    root = Tk(className='第五关')
    root.geometry('575x575')
    root.resizable(0,0)

    l_AI = Label(text = '答案是 Please wait for the green light.')
    l_tip2 = Label(text = '(请自行退出)')

    l_CH = Label(text = '中文解释是：请等绿灯。')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'ht.')

    def _show_2():
        e.insert(0, 'lig')

    def _show_3():
        e.insert(0, 'n')

    def _show_4():
        e.insert(0, 'the')

    def _show_5():
        e.insert(0, 'ait fo')

    def _show_6():
        e.insert(0, 'r')

    def _show_7():
        e.insert(0, 'gree')

    def _show_8():
        e.insert(0, 'Please w')

    def _show_():
        e.insert(0, ' ')

    def _show_AI():
        l_AI.pack()
        l_tip2.pack()

    def _show_CH():
        l_CH.pack()
    # 清空e输入框中的内容
    def _clear():
        e.delete(0, END)

    def back():
        system('选关.py')
        root.quit()
    content = StringVar()

    l = Label(text='第五关：?eman ruoy si tahW').pack()
    la_1 = Label(text='(不能输入 请倒着输入答案)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='ht.', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='lig', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='n', command=_show_3)
    b_show_3.pack()

    b_show_4 = Button(root, text='the', command=_show_4)
    b_show_4.pack()

    b_show_5 = Button(root, text='ait fo', command=_show_5)
    b_show_5.pack()

    b_show_6 = Button(root, text='r', command=_show_6)
    b_show_6.pack()

    b_show_7 = Button(root, text='gree', command=_show_7)
    b_show_7.pack()

    b_show_8 = Button(root, text='Please w', command=_show_8)
    b_show_8.pack()

    b_show = Button(root, text='点击我显示 空格 ', command=_show_)
    b_show.pack()

    b_AI = Button(root, text='点击查看 答案', command=_show_AI)
    b_AI.pack()

    b_CH = Button(root, text='点击查看 中文解释', command=_show_CH)
    b_CH.pack()

    b_clear = Button(root, text='清空', command=_clear)
    b_clear.pack()

    b_ak = Button(root, text='返回选关', command=back)
    b_ak.pack()

    mainloop()
if __name__ == '__main__':
    main()