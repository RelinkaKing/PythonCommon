import multiprocessing
from threading import Lock, Thread,currentThread
from queue import Queue
import time
import sys

q = Queue()

# numTag和Lock用来演示多线程同步
numTag = 0
lock = Lock()
queList = []
threadCount=0
threadProcess={}
firstout = ""
"""
    用来演示输出
"""
def print_num(id,item):
    time.sleep(0.5)
    # 声明numTag是全局变量，所有的线程都可以对其进行修改
    global numTag
    with lock:
        numTag += 1
        x=">"
        # 输出的时候加上'\r'可以让光标退到当前行的开始处，进而实现显示进度的效果
        for r in range(0,100,1):
            if r <numTag:
                x=x+">"
            else:
                x=x+" "
        sys.stdout.write('\r{2}:Queue Item: {0}\tNumTag:[{1}]'.format(str(item),x,str(id)))
def printMultiProcess():
    global firstout
    time.sleep(0.1)
    # 声明numTag是全局变量，所有的线程都可以对其进行修改
    global numTag
    with lock:
        numTag += 1
        result = ""
        if firstout == "":
            for i in range(0,50,1):
                firstout = firstout+"\r\n\r\n"
        for t in threadProcess:
            x=">"
            # 输出的时候加上'\r'可以让光标退到当前行的开始处，进而实现显示进度的效果
            for r in range(0,100,1):
                if r <threadProcess[t]:
                    x=x+">"
                else:
                    x=x+" "
            result =result+ '\r{0}:\tNumTag:[{1}]'.format(t,x) +"\r\n"
        
        sys.stdout.write(firstout+result)

"""
    worker是一个中间件，把Queue接收到的值传给对应的功能函数进行处理
"""
def worker(name):
    while True:
        item = q.get()
        if item is None:
            break
        threadProcess[name]=item
        #print_num(name,item)
        printMultiProcess()
        q.task_done()

if __name__ == '__main__':

    # 根据CPU的数量创建对应数量的线程
    threadCount = multiprocessing.cpu_count()
    print(threadCount)
    for i in range(threadCount):
        t = Thread(target=worker,args=(str(i)))
        # 设置daemon为True, 可以让线程在主线程退出的时候一起结束
        # 否则线程还会继续等待
        t.daemon = True
        t.start()

    # 通过Queue给线程传值
    for i in range(150):
        q.put(i)

    q.join()
    print('')