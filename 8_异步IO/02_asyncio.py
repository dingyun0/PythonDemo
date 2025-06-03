# hello world
import asyncio
import threading
import time

# async def hello():
#     print("Hello world!")
#     await asyncio.sleep(1)
#     print("Hello again!")
# asyncio.run(hello())

# #(异步io)
# async def hello(name):
#     print("Hello %s! (%s)" % (name, threading.current_thread()))
#     await asyncio.sleep(1)
#     print("Hello %s again! (%s)" % (name, threading.current_thread()))
#     return name
# async def main():
#     L=await asyncio.gather(hello("world"), hello("python"))
#     print(L)
# asyncio.run(main())

# # 同步io
# def hello(name):
#     print("Hello %s! (%s)" % (name, threading.current_thread()))
#     time.sleep(1)
#     print("Hello %s again! (%s)" % (name, threading.current_thread()))
#     return name
# def main():
#     L=[hello("world"), hello("python")]
#     print(L)
# if __name__ == "__main__":
#     main()

# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页
import asyncio
async def wget(host):
    print("wget %s..." % host)
    reader,writer=await asyncio.open_connection(host,80)
    header=f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode("utf-8"))
    await writer.drain()

    while True:
        line=await reader.readline()
        if line==b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    writer.close()
    await writer.wait_closed()
    print("wget %s...ok" % host)

async def main():
    await asyncio.gather(
        wget("www.sina.com.cn"),
        wget("www.sohu.com"),
        wget("www.163.com")
    )
asyncio.run(main())







