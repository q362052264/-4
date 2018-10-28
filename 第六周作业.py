import requests
import threading
import time
from queue import Queue
lock=threading.Lock()
queue1=Queue(maxsize=10)
queue2=Queue(maxsize=10)
def qingqiu(max1):
	for x in range(1,max1+1,1):
		func=requests.get
		args=f'http://httpbin.org/get?a={x}'
		queue1.put((func,args))

qingqiu(10)
num=threading.Semaphore(3)
class Test(threading.Thread):
	def __init__(self,queue,lock,num):
		threading.Thread.__init__(self)
		self.queue=queue
		self.lock=lock
		self.num=num
	def run(self):
		with self.num:
			while not queue1.empty():
			    func,args=self.queue.get()
			    lock.acquire()
			    r=func(args,auth=('user','123456'))
			    global queue2
			    queue2.put(r)
			    lock.release()
			    time.sleep(1)


for i in range(5):
	t=Test(queue1,lock,num)
	t.start()







###################################
import requests
import time
import threading
from queue import Queue
queue1=Queue(maxsize=10)
queue2=Queue(maxsize=10)
def qingqiu(max1):
	for x in range(1,max1+1,1):
		func=requests.get
		args=f'http://httpbin.org/get?a={x}'
		queue1.put((func,args))

qingqiu(10)
def consumer(cond,event,queue,num,lock):
		t=threading.currentThread()
		event1=event.wait(1)
		print(f'{t} event1 is {event1}')
		global queue2
		if event1:
			lock.acquire()
			try:
				for x in range(1,num+1,1):
					func,args=queue.get()
					r=func(args,auth=('user','123456'))
					queue2.put(r)
					time.sleep(1)
				lock.release()
				event.clear()
				return '事件处理了'
			except IndexError:
				lock.release()
				pass
		elif cond:
			with cond:
			    print(cond)
			    cond.wait()
			    print(f'cond.wait() is successful')
			    lock.acquire()
			    for x in range(1,num+1,1):
				    func,args=queue2.get()
				    r=func(args,auth=('user','123456'))
				    queue2.put(r)
				    time.sleep(1)
			    lock.release()
			    return '任务处理了'


def producer(cond,event):
	t=threading.currentThread()
	event.set()
	time.sleep(1)
	with cond:
		print(cond)
		cond.notifyAll()
		print('producer is end')


cond=threading.Condition()
event=threading.Event()
lock=threading.Lock()
c1=threading.Thread(name='c1',target=consumer,args=(cond,event,queue1,5,lock))
c2=threading.Thread(name='c2',target=consumer,args=(cond,event,queue1,5,lock))
c3=threading.Thread(name='c3',target=producer,args=(cond,event))
c3.start()
c1.start()
c2.start()
