import asyncio
import time


async def task_async(id):
    print("Task start #{}".format(id))
    await asyncio.sleep(2)
    print("Task end #{}".format(id))

start = time.time()
asyncio.run(task_async(1))
asyncio.run(task_async(2))
asyncio.run(task_async(3))
asyncio.run(task_async(4))
print((time.time() - start)*1000)  # 8013.213872909546


async def main():
    print("main start")
    start = time.time()
    t1 = asyncio.create_task(task_async(1))
    t2 = asyncio.create_task(task_async(2))
    t3 = asyncio.create_task(task_async(3))
    t4 = asyncio.create_task(task_async(4))

    await t1
    await t2
    await t3
    await t4
    end = time.time()
    print((end - start)*1000)

asyncio.run(main())

