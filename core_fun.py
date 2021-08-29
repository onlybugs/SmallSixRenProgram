from utils import *
from var import *

bfont = (32)
lfont = ("华文新魏",15)

def get_out(type,lb1,lb2,lb3):
    tmd,rubbish,h = get_lunar()
    m = month[tmd[0]] #7
    d = day[tmd[1]]   # 22
    h = hour[SuntoLnuar(h)] # 10
    # m d h -> i
    image_index = (h+(d+((m+type-1)%6)-1)%6-1)%6
    lb1.configure(text="当前的卦象为:" + images[image_index-1])
    lb2.configure(text = imagewords[images[image_index-1]])


def clear(lb2,lb3,lb4):
    lb2.configure(text="主卦象显示区")
    lb3.configure(text="卦辞和卦象简解")
    lb4.configure(text="作者:KaiLi 日期:8-28 版本:1.0")

