import requests
import re
import time


def get_lunar():
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    html = requests.get("https://www.d5168.com/nongli.php",
                        headers = header)
    rstr = re.compile("<h1>.*?\d+.*?年(.*?)月(.*?)\s")

    relunar = re.findall(rstr,html.text)
    timestr = get_current_time()
    hour = int(time.strftime("%H"))
    return (relunar[0],timestr,hour)

def get_current_time():
    return time.strftime("%H:%M:%S")

def SuntoLnuar(st):
    if(st == 23 or st == 0):
        return "子"
    elif(st == 1 or st == 2):
        return '丑'
    elif(st == 3 or st == 4):
        return '寅'
    elif(st == 5 or st == 6):
        return '卯'
    elif(st == 7 or st == 8):
        return '辰'
    elif(st == 9 or st == 10):
        return '巳'
    elif(st == 11 or st == 12):
        return '午'
    elif(st == 13 or st == 14):
        return '未'
    elif(st == 15 or st == 16):
        return '申'
    elif(st == 17 or st == 18):
        return '酉'
    elif(st == 19 or st == 20):
        return '戌'
    elif(st == 21 or st == 22):
        return '亥'

