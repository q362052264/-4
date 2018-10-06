1.
class Animal:
	def __init__(self,name):
		self.name=name
	def call(self):
		print(f"{self.name}叫了")

class Dog(Animal):
	def __init__(self,name):
		self.name=name
	def call(self):
		print("汪汪")

class Cat(Animal):
	def __init__(self,name):
		self.name=name
	def call(self):
		print("喵喵")


2.
def zz(x,y,z):
	  print(x,end=" ")
	  print(y,end=" ")
	  def xx(x,y,z):
	      if not x+y>z:
	          print(x+y,end=" ")
	          sum1=x+y
	          x=y
	          y=sum1
	          xx(x,y,z)
	      print()
	  xx(x,y,z)


zz(1,1,10)

3.
a=[x for x in range(1,101,1) if x%2==1]

4.
class jisuan:
	@staticmethod
	def add(x,y):
		try:
			return x+y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def sub(x,y):
		try:
			return x-y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def mul(x,y):
		try:
			return x*y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def div(x,y):
		try:
			return x/y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None


5.
import sys
con=sys.stdout
fpath='C:\outt1.txt'
f=open(fpath,'w')
sys.stdout=f
import this
f.close()
f=open(fpath,'r')
sys.stdout=con
def cishu(str):
	dic={}
	a=""
	for x in str:
		if x=='\n':
			continue
		elif x==" ":
			if dic.__contains__(a):
				dic[a]=dic.get(a)+1
				a=""
				continue
			elif not dic.__contains__(a):
				dic[a]=1
				a=""
				continue
		a=a+x
	return dic


zzz=f.read()
p=cishu(zzz)
try:
	import cPickle as pickle
except ImportError:
	import pickle

f.close()
ff=open('C:\outt2.txt','wb')
pickle.dump(p,ff)
ff.close()


