def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r='200 OK'

def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...' % n)
        r=c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c=consumer()
produce(c)

# 1. c=consumer() 创建了一个生成器对象c，但是consumer函数并没有执行，只是准备好
# 2. produce(c)调用了生产者函数，produce开始执行
# 3. 执行到了c.send(None)，consumer函数被调用，初始化了r，通过yield给生产者返回了一个r空值
# 4. 后续n=1，调用c.send(1)，来到的yield的地方。将n赋值为1，r赋值为200ok，并再次来到yield r，返回了r为200ok
# 5. 如此反复
# 重点是n = yield r
# 分成两部分：
# yield r 是将r 返回给外部调用程序，交出控制权，暂停；
# n = yield 可以接收外部程序通过send()发送的信息，并赋值给n