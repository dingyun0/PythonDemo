import threading
import time
from concurrent.futures import ThreadPoolExecutor

counter=0
lock=threading.Lock()

def increment_counter(thread_id,increment):
    global counter
    for _ in range(increment):
        with lock:
            current=counter
            time.sleep(0.01)
            counter=current+1
    print(f"线程{thread_id}结束，counter={counter}")

def main():
    global counter
    counter=0
    start_time=time.time()
    # 线程池
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(increment_counter,1,100)
        executor.submit(increment_counter,2,100)
        executor.submit(increment_counter,3,100)
    
    print(f"总耗时:{time.time()-start_time:.2f}秒")

if __name__=="__main__":
    main()