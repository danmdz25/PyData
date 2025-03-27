import numpy as np
arr=np.array([[1,2,3,4],[4,2,3,1]])

# print(arr[1,3])#printing 2d array # second array, fourth position at array

arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
# print(arr[1,0,2]) # second block of 2d arrays, first array, third position at array

print(arr[0,1,-1])