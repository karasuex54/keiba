import time

cnt = 0
while cnt < 10:
    try:
        print(1/0)
        break
    except:
        cnt += 1

print(cnt)
