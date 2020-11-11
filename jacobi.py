import numpy as np
A=np.array([[float(input('a11 = ')),float(input('a12 = ')),float(input('a13 = '))],
[float(input('a21 = ')),float(input('a22 = ')),float(input('a23 = '))],
[float(input('a31 = ')),float(input('a32 = ')),float(input('a33 = '))]])
print("\n\nA =\n",A)

A1=A
m=len(A)
apq=A[0,1]
p=0
q=1

def hoe(A):
	apq=A[0,1]
	p=0
	q=1
	for i in range(m):
		for j in range(m):
			if(i!=j):
				if(apq<np.abs(A[i,j])):
					apq=np.abs(A[i,j])
					p=i
					q=j
	return apq,p,q

def j(A):
	apq,p,q=hoe(A)
	print("Highest off-diagonal element: ",apq)

	J=np.eye(3,3)
	phi=(A[q,q]-A[p,p])/(2*A[p,q])
	print("Phi = ",phi)
	theta1=np.arctan(-phi-np.sqrt(1+(phi*phi)))
	theta2=np.arctan(-phi+np.sqrt(1+(phi*phi)))
	theta=np.minimum(theta1,theta2)
	print("Theta = ",theta)
	J[p,p]=np.cos(theta)
	J[p,q]=np.sin(theta)
	J[q,p]=-np.sin(theta)
	J[q,q]=np.cos(theta)
	print("\nJacobian Matrix = \n\n",J)
	return J

def diagonalize(A):
	J=j(A)
	Jinv=np.linalg.inv(J)
	print("\nJinv =\n\n",Jinv)
	AJ=np.matmul(A,J)
	print("\nAJ = \n\n",AJ)
	A1=np.matmul(Jinv,AJ)
	print("\nA1 = \n\n",np.around(A1,4))
	return A1

count=1
while(np.round(apq,5)!=0):
	input("\n\nPress Enter to continue....")
	print("\n\n\n\n\n\t\t\t\t\tIteration no. ",count)
	print("------------------------------------------------------------------------------------------------------------------------------------------")
	A1=diagonalize(A1)
	apq,p,q=hoe(A1)
	count+=1