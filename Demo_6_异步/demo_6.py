import asyncio
import time

async def download_file(file_name,duration):
    print(f"开始下载{file_name}")
    await asyncio.sleep(duration)
    print(f"下载完成{file_name}")
    return f"下载完成{file_name}"

async def main():
    start_time=time.time()
    tasks=[
        download_file("file1.txt",2),
        download_file("file2.txt",3),
        download_file("file3.txt",1)
    ]
    results=await asyncio.gather(*tasks)
    for result in results:
        print(result)

    print(f"总耗时:{time.time()-start_time:.2f}秒")

if __name__=="__main__":
    asyncio.run(main())