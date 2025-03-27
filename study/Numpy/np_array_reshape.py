import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3) #1D to 2D
# print(newarr)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,3,2)#1D to 3D
# print(newarr)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(2,6).base)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,2,-1)# unknow dimension
# print(newarr)

arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr.ndim)
newarr=arr.reshape(-1) # 2D/3D transform into 1D
print(newarr.ndim)