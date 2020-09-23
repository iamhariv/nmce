import numpy as np
from sympy import *
import time

print("Successive Approximation method of solution of algebraic and transcendental equations")
print("~harikrishnav")	
x=Symbol('x')
def getfn():
	e=sympify(input("Enter function in x: "))		#ENTER THE APPROPRIATE FUNCTION HERE	
	f=e.subs({'x':x})
	return f

f=getfn()
phi=lambdify(Symbol('x'),f,'numpy')

def getLimits():
	print("\nNOTE:\n Enter Angles in Radians only.")
	x=np.float32(input("\nx0 = "))
	return x

x=getLimits()

n=np.float32(input("\nRequired number of decimal places = "))
es=np.float32(np.float_power(10,-n))

start=time.perf_counter()
ea=10
xold=x
count=0
while (ea>es):
	count+=1
	xold=x	
	x=phi(xold)
	ea=np.abs(x-xold)
	if count>100:
		print("phi(x) is not converging.\nTry another representation for phi(x)")
		exit()
	
print("\nx =",end=" ")
print(np.round(x,n))
print("\n\nCalculated in",end=' ')
print(np.round(time.perf_counter()-start,5),end=' ')
print("seconds")
print("\n\nTook",end=' ')
print(count,end=' ')
print(" iterations")
		