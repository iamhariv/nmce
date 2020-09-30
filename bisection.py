import numpy as np
from sympy import *
import time

print("\n\nBisection method of solution of algebraic and transcendental equations")
print("~harikrishnav")

x=Symbol('x')
def getfn():
	e=sympify(input("Enter function in x: "))		#ENTER THE APPROPRIATE FUNCTION HERE	
	f=e.subs({'x':x})
	return f

e=getfn()
f=lambdify(Symbol('x'),e,'numpy')

def getLimits():
	print("\nNOTE:\n1. Enter Angles in Radians only.")
	print("2. a should be smaller than b\n")
	a=np.float32(input("a = "))
	b=np.float32(input("b = "))
	return a,b

a,b=getLimits()

while(f(a)*f(b)>0 or a>b):
	print("\nError")
	a,b=getLimits()

n=np.float32(input("\nNumber of significant digits required= "))
es=np.float32(0.5*np.float_power(10,2-n))

start=time.perf_counter()
ea=1
xold=a
count=0
x=(a+b)/2
while ea>es:
	count+=1
	x=(a+b)/2
	print(count,end='   ')
	print(x)
	if f(a)*f(x)>0:
		a=x
	else:
		b=x
	ea=np.fabs((100*(x-xold))/x)
	xold=x
print("\nx =",end=" ")
print(np.round(x,n))
print("\n\nCalculated in",end=' ')
print(np.round(time.perf_counter()-start,5),end=' ')
print("seconds")
print("\n\n")
		
