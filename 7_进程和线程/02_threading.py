# 多线程
import time,threading
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(0.1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

# 共享变量，会乱(数字多的时候会)
# multithread
import time, threading
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('9999999999',balance)

# 通过加锁来避免
import threading,time
lock=threading.Lock()
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('9999999999',balance)

# python的线程是真正的线程，但是解释器执行代码的时候，他有一个GIL锁。
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。