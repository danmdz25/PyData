import numpy as np 

arr=np.array([1,2,3,4])
x=arr.copy()
arr[0]=42
print(x) 
print(arr) 

print('')
print('Copy\n______________________________________ ')
print('')
arr=np.array([-1,-2,-3,-4])
x = arr.view()
print(arr)
print(x)
print('')
print('View\n______________________________________ ')
arr[0:4]= [1,2,3,4]
print(arr)
print(x)
print('')
print('View com alteração\n______________________________________ ')
x[0:4]=[-24,2,13,15]
print(arr)
print(x)