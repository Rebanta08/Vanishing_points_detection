import numpy as np
import cmath
u=np.array([128,314,565])*0.2645833333
v=np.array([305,18,292])*0.2645833333
A=np.array([[u[0]-u[2],v[0]-v[2]],[u[1]-u[2],v[1]-v[2]]])
b=np.array([[A[0,0]*u[1]+A[0,1]*v[1]],[A[1,0]*u[0]+A[1,1]*v[0]]])
x=np.linalg.solve(A,b)
f_in=-(u[0]-x[0])*(u[1]-x[0])-(v[0]-x[1])*(v[1]-x[1])
f=cmath.sqrt(f_in)
print("\n",A)
print("\n",b)
print("\n",x)
print("\n",f_in)
print("\n",f)