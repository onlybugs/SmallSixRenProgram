from tkinter import *
from core_fun import *
# lb1.configure(text="sss") 修改标签内容

def InitWindows():
    # all Init
    root = Tk()
    root.title("小六壬推算 v1.0")
    root.geometry('1000x650+300+5')
    root.resizable(0, 0)
    root.configure(bg = "#c8c8a9")

    # init label
    lb1 = Label(root, text="未来的时间",
                font=32,
                bg='#fc9d9a', fg='black')
    lb1.place(x=100, y=20, height=30, width=800)
    # 闭包 显示时间
    def gettime():
        tcurr = get_lunar()
        # 农历时辰的计算
        tet = tcurr[0][0] + "月" + tcurr[0][1] + SuntoLnuar(tcurr[2])\
              + "时" + " " + tcurr[1]
        lb1.configure(text= tet )
        root.after(1000, gettime)

    # Lable
    lb2 = Label(root, text="主卦象显示区",font = ("华文新魏",39),
                bg='#83af9b', fg='black')
    lb2.place(x=300, y=109, height=60, width=680)
    lb3 = Label(root, text="卦辞和卦象简解",font = lfont,
                bg='#83af9b', fg='black')
    lb3.place(x=300, y=213, height=268, width=680)
    lb4 = Label(root, text="作者:KaiLi 日期:8-28 版本:1.0",font = lfont,
                bg='#83af9b', fg='black')
    lb4.place(x=300, y=525, height=60, width=680)

    # Button
    bt1 = Button(root, text="婚姻杂事", font=bfont,command = lambda : get_out(1,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt1.place(x=60, y=79, height=60, width=180)
    bt2 = Button(root, text="求财经商", font=bfont,command = lambda : get_out(2,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt2.place(x=60, y=173, height=60, width=180)
    bt3 = Button(root, text="疾厄病苦", font=bfont,command = lambda : get_out(3,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt3.place(x=60, y=267, height=60, width=180)
    bt4 = Button(root, text="官司诉讼", font=bfont,command = lambda : get_out(4,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt4.place(x=60, y=366, height=60, width=180)
    bt5 = Button(root, text="外出旅行", font=bfont,command = lambda : get_out(5,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt5.place(x=60, y=465, height=60, width=180)
    bt5 = Button(root, text="死亡宫里", font=bfont,command = lambda : get_out(6,lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt5.place(x=60, y=559, height=60, width=180)

    bt6 = Button(root, text="清空", font=bfont,command = lambda : clear(lb2,lb3,lb4),
                 bg='#f9cdad', fg='black')
    bt6.place(x=920, y=20, height=30, width=50)

    gettime()
    root.mainloop()


if __name__ == '__main__':
    InitWindows()
