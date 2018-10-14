#1.
from functools import partial
def mul(x,y):
	return x*y

a=partial(mul,2)
#2.

def add(x,y,z):
    return x+y+z

from functools import partial
addA=partial(add,x=1,y=2,z=3)
addA()

#2.2
def add(x,*args):
	sum1=x
	for i in args:
		sum1=sum1+i
	print(f"sum={sum1}")
	return sum1


def add1(x,*args):
	z=add(x,*args)
	return partial(add1,z)


add1(1)(2)(3)
add1(1,2,3)(4)


#3.
def timer(func):
	def Wrapper(*args,**akg):
		start=time.time()
		x=func(*args,**akg)
		end=time.time()
		print(end-start)
		return x
	return Wrapper

@timer
def add1(x,y):
	return x+y

#4.
def timer2(func):
	def Wrapper(*args,**akg):
		try:
			x=func(*args,**akg)
		except Exception as e:
			print(e)
			return None
		return x
	return Wrapper

@timer2
def chu(*args,**akg):
	sum1=args[0]**2
	print(args)
	for i in args:
		sum1=sum1/i
	return sum1

#5.
def timer3(func):
	def Wrapper(*args,**akg):
		start=time.time()
		x=func(*args,**akg)
		end=time.time()
		thiss=end-start
		print(f'Done {thiss}')
		return x
	return Wrapper

@timer3
def chu(*args,**akg):
	sum1=args[0]**2
	print(args)
	for i in args:
		sum1=sum1/i
	return sum1



#1.
def timer4(func):
	def Wrapper(*args,**akg):
		print(type(args))
		new_args=[]
		for i in range(len(args)):
			print(type(args[i]))
			if type(args[i])==type("aa"):
			    if not args[i].isupper():
				    print(args[i])
				    new_args.append(args[i].upper())
			    else:
				    print(args[i])
				    new_args.append(args[i])
		print(new_args)
		x=func(*new_args,**akg)
		return x
	return Wrapper

@timer4
def add2(x,y):
	return x+y

add2("asdsad","ASDSADSA")

#2.
def t1(path):
	def t2(zijie):
		path1=path
		with open(path,'r') as f:
			while True:
				try:
					t=f.read(zijie)
				except Exception as e:
					print(e)
					break
				yield t
		print("½áÊøÁË!")
	return t2

path="C:/new1.txt"
z=t1(path)
x=z(2)
x.send(None)

#3.
def t3():
	sumkey=0
	while True:
		sumkey=sumkey+1
		yield sumkey

x=t3()
next(x)

#4.
x=(i for i in range(1,51,1) if not i%2)
for i in x:
	print(i)

#5.
import os
from os.path import join,getsize
def x(path):
	for root,dirs,files in os.walk(path):
		for name in files:
			fname=join(root,name)
			yield fname


z=x("c:\\")
next(z)
