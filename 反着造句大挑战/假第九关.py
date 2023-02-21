from tkinter import *
from os import *
def main():
    root = Tk(className='第九关')
    root.geometry('350x350')
    root.resizable(0,0)

    l_AI = Label(text = '**是 陷入死循环了吧？好玩吗？哈哈哈哈哈！')
    l_tip2 = Label(text = '(继续按退出按钮啊！继续啊！)')
    # e输入框显示字符串:***
    def _show_1():
        e.insert(0, 'you like')

    def _show_2():
        e.insert(0, 'ef?')


    def _show_3():
        e.insert(0, 'Do')

    def _show_4():
        e.insert(0, 'be')

    def _show_():
        e.insert(0, ' ')

    def _show_AI():
        l_AI.pack()
        l_tip2.pack()
    # 清空e输入框中的内容
    def _clear():
        print('下次再玩吧！')
        system('选关.py')

    def back():
        system('假第九关.py')
        root.quit()
    content = StringVar()

    l = Label(text='第九关：完蛋了！我来到第二关了！').pack()
    l_tip = Label(text='(*能输入 请倒着输入**)').pack()

    e = Entry(root, textvariable=content)
    e.pack()

    b_show_1 = Button(root, text='you like', command=_show_1)
    b_show_1.pack()

    b_show_2 = Button(root, text='ef?', command=_show_2)
    b_show_2.pack()

    b_show_3 = Button(root, text='Do', command=_show_3)
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