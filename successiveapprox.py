import numpy as np
from sympy import *
import time

print("\n\n############################################################################################")
print("\n\nSuccessive Approximation method of solution of algebraic and transcendental equations")
print("~harikrishnav\n\n")	
x=Symbol('x')
def getfn():
	e=sympify(input("Represent the function in the form \"x=phi(x)\" and\n           Enter function phi(x): "))		#ENTER THE APPROPRIATE FUNCTION HERE	
	f=e.subs({'x':x})
	return f

f=getfn()
phi=lambdify(Symbol('x'),f,'numpy')

for i in np.arange(0,1,0.001):
	if np.fabs(np.float64(diff(f).subs({'x':i})))>1:	
		print("phi(x) is not converging.\nTry another representation for phi(x)")
		exit()

def getLimits():
	print("\nNOTE:\n Enter Angles in Radians only.")
	x=np.float32(input("\nx0 = "))
	return x

x=getLimits()

n=np.float32(input("\nRequired number of significant digits = "))
if n>16:
	n=16
es=np.float32(np.float_power(10,-n))

start=time.perf_counter()
ea=1
xold=x
count=0
print('\n')
while (ea>es):
	count+=1
	xold=x	
	x=phi(xold)
	print("Iteration ",end=' ')
	print(count,end=' ')
	print(x)
	if(np.round(x,n)==np.round(xold,n)):
		break
	
print("\nx =",end=" ")
print(np.round(x,n))
print("\n\nCalculated in",end=' ')
print(np.round(time.perf_counter()-start,5),end=' ')
print("seconds")
print("\n\nTook",end=' ')
print(count,end=' ')
print(" iterations\n\n\n")
		
