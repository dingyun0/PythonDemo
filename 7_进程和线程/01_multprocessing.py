from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


# Only works on Unix/Linux/macOS:
# linux调用方法，window系统上面没有fork()
# import os

# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 进程池 pool
from multiprocessing import Pool
import os,random,time

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# 子进程
import subprocess
r=subprocess.call(['nslookup','www.python.org'])
print(r)

# 进程间的通信queue
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue' % value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()