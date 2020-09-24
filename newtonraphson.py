import numpy as np
from sympy import *
import time

print("\n\nNewton-Raphson Iterative method of solution of algebraic and transcendental equations")
print("~harikrishnav\n\n")

x=Symbol('x')
def getfn():
	e=sympify(input("Enter function in x: "))		#ENTER THE APPROPRIATE FUNCTION HERE	
	f=e.subs({'x':x})
	return f

expression=getfn()
f=lambdify(Symbol('x'),expression,'numpy')
fprime=diff(expression)
deriv=lambdify(Symbol('x'),fprime,'numpy')

def getLimits():
	print("\nNOTE:\n Enter Angles in Radians only.")
	x=np.float32(input("\nx0 = "))
	return x

x=getLimits()

n=np.float32(input("\nNumber of significant digits required= "))
es=np.float32(0.5*np.float_power(10,2-n))

start=time.perf_counter()
ea=1
xold=x
count=0
while ea>es:
	count+=1
	val = f(xold)
	dval = deriv(xold)	
	x=xold-(val/dval)
	ea=np.fabs((100*(x-xold))/x)
	xold=x
	
print("\nx =",end=" ")
print(np.round(x,n))
print("\n\nCalculated in",end=' ')
print(np.round(time.perf_counter()-start,5),end=' ')
print("seconds")
print("\n\nTook",end=' ')
print(count,end=' ')
print(" iterations\n\n\n")
		