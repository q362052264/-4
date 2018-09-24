
def years():
    name=input("your name")
    year=int(input("your age"))
    years=2018-year+100
    print("%s到%d年100岁!" %(name,years))


years()

def xx1(x):
    if x%2==0:
        print("你输入的是偶数")
    else:
        print("是基数")


xx1(int(input("请输入数字")))

def xx2(lst):
	if lst==[]:
		print("你输入的列表里没有元素,将返回None")
		return None
	for a in lst:
		print(a)
		if not bool(a):
			print("have 空对象")
			return True
		else:
			pass
		return False

xx2([None,2,3])
xx2([])



def xxx(x):
	def xx3(a):
		if not bool(a):
			return True
		else:
			return False
	b=filter(xx3,x)
	if list(b)==[]:
		print("no have 空对象")
		return False
	else:
		print("have 空对象")
		return True

xxx([2,3,4])

def x(lst):
    a=lambda x: bool(x)
    for x in lst:
        b=a(x)
        if not b:
            print("have None")
            return True
        else:
            pass
    print("NO None")

x([2,4,6,None])



def x1():
	a=[]
	print("输入所有你要平方的数字,结束就输入空格")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b)**2)
			continue
		elif b.isspace():
			print("正常结束!")
			return a
		else:
			print("你输入的不是数字,异常,将返回None")
			return None

x1()



def x2():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a

		
    a=map(lambda x:x**2,x2())
list(a)



from functools import reduce
def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a

		
    reduce(lambda x,y:x+y,shuruqi())

	
	
def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a

a=[x**2 for x in shuruqi()]
a



def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a


def xx(lst1,lst2):
	a=[]
	for a1 in lst1:
		for a2 in lst2:
			if a1==a2:
				a.append(a1)
	return a

    a=xx(shuruqi(),shuruqi())


	
	
def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a


def max(lst):
	max1=0
	for a in lst:
		if a>max1:
			max1=a
			continue
	return max1

a=max(shuruqi())
a



def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a

reduce(lambda x,y: x if x>y else y,shuruqi())



import random
import string

lowercase=string.ascii_lowercase	       
uppercase=string.ascii_uppercase	       
punctuation=string.punctuation	       
number=string.digits

def shuruqi2(*lst):
	   a=[]
	   for x in lst:
	       a.append(x)
	   return a

	       
def shuruqi3(x):
	a=1
	b=[]
	while a<=x:
		print("输入你刚才输入的字符集要设置的数量")
		c=int(input("这是你输入的第%d个字符集你设置的数量" %(a)))
		b.append(c)
		a+=1
	return b


def psw(x,y):
	lst=""
	for a in range(len(x)):
	    xx=''.join(random.sample(x[a],y[a]))
	    lst=lst+xx
	z=list(lst)
	random.shuffle(z)
	return ''.join(z)

x=shuruqi2(lowercase,uppercase,punctuation,number)
y=shuruqi3(len(x))
psw(x,y)



def xx2(number,lst):
	b=-1
	c=0
	d=[]
	for a in lst:
		if a==number:
			print("列表里有元素%d" %(number))
			c=1
			break
	if c==0:
		print("列表里不存在元素%d,将返回None" %(number))
		return None
	else:
		try:
			while True:
				b=lst.index(number,b+1)
				d.append(b)
		except:
			print("进入except")
		finally:
			for a in d:
				if (len(lst)-1)/2>a:
					print("左边有一个")
				elif (len(lst)-1)/2<a:
					print("右边有一个")
				else:
					print("正好在中间有一个")


def xxx(xx):
	a=[]
	for x in range(1,xx+1):
		z=0
		for zz in range(2,x):
			if x%zz==0:
				z=1
				break
		if z==0:
			a.append(x)
	return a

xxx(100)

x=0.0
y=0.0
def add(x,y):
    return x+y
	
def sub(x,y):
    return x-y
	
def mul(x,y):
    return x*y
	
def div(x,y):
    return x/y


def shuruqi():
	a=[]
	print("输入数字，不是数字就当结束")
	while True:
		b=input("输入数字")
		if b.isdigit():
			a.append(int(b))
			continue
		else:
			return a


def min(lst):
	min1=99
	for a in lst:
		if a<min1:
			min1=a
			continue
	return min1

a=max(shuruqi())
a