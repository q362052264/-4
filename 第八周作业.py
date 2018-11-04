#############################
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import threading
def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)

def produce(queue):
    for num in range(10):
        queue.put(num)
        print(f"produce put{num} to queue")

def jianshi(queue):
    while queue.qsize():
        r=queue.qsize()
        print(f'queue.qsize={r}')
        time.sleep(1)

def consumer(queue):
    with ThreadPoolExecutor(max_workers=3) as executor:
        while queue.qsize()>0:
            r=queue.get()
            z=executor.submit(fib,r)
            z1=z.result()
            print(f'fib({r})={z1}')

if __name__=='__main__':
    queue = Queue()
    t1=threading.Thread(target=produce,args=(queue,))
    t1.start()
    t2=threading.Thread(target=jianshi,args=(queue,))
    t2.start()
    t3=threading.Thread(target=consumer,args=(queue,))
    t3.start()



######################################
import asyncio
import aiohttp


async def produce():
    a=0
    while(a<10):
        print(f'ÕýÔÚÌá½»....aµÄÖµÎª{a}')
        yield f"http://httpbin.org/get?a={a}"
        a=a+1

async def consumer():
    async for v in produce():
        print(v)
        async with aiohttp.ClientSession() as session:
            async with session.get(v) as response:
                z=await response.json()
                print(f"a={z.get('args').get('a')}")


if __name__=='__main__':
    loop=asyncio.get_event_loop()
    result=loop.run_until_complete(consumer())
