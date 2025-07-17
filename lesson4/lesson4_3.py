# 4.3 模擬非同步網路請求
import asyncio
import time

async def task(id, delay):
    print(f"開始任務{id}")
    await asyncio.sleep(delay)
    print(f"任務{id}完成")


async def main():
    
#     await task(1, 1)
#     await task(2, 2)
#     print(f"非同步總耗時: {time.time() - start:.2f} 秒")
    tasks = [task(1, 1), task(2, 2), task(3, 3), task(4, 4), task(5, 5) ]
    start = time.time()
    await asyncio.gather(*tasks)
    print(f"非同步總耗時: {time.time() - start:.2f} 秒")

asyncio.run(main())

