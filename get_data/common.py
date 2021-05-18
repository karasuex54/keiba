from time import sleep
from requests import get


def custom_get(url: str):
    sleep(2)
    cnt = 0
    e = False
    while cnt < 5:
        try:
            r = get(url, timeout=3.5)
            e = True
            break
        except:
            cnt += 1
            sleep(10)
    return r, e

def time_to_seconds(time_txt: str) -> str:
    txt = time_txt.split(":")
    if len(txt) == 1:
        return time_txt
    txt = list(map(float, txt))
    txt = str(txt[0]*60 + txt[1])
    return txt