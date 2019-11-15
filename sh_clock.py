import time

def clock():
    h = int(input("输入小数:"))
    m = int(input("输入分钟:"))
    while True:
        ct = time.localtime()
        if (h,m) == ct[3:5]:
            print("\n时间到了....")
            return
        print("\r%2d:%2d:%2d"%(ct[3:6]), end="")
        time.sleep(1)

if __name__ == "__main__":
    clock()
