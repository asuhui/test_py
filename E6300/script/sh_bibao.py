#coding=utf-8
def line_config(a,b):#闭包
    def line(x):
        return a*x+b
    return line
if __name__=="__main__":
    line=line_config(1,1)
    print(line(1))

