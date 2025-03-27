# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
import numpy as np

arr=np.array([1,2,3,4],dtype='S')
print(arr.dtype)
arr=np.array([1,2,3,4],dtype='i4')
print(arr.dtype)
arr=np.array([1,2,3,4])
print(arr.dtype)
newarr=arr.astype('f')
print(newarr.dtype)