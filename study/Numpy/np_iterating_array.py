import numpy as np
arr=np.array([1,2,3,4])

# for x in arr:
    # print(x) # iterating 1D array that return the values

arr=np.array([[1,2,3],[4,5,6]])
# for x in arr:
#     print(x) # Default iteration 2D array that return te arrays

# for x in arr:
#     for y in x:
#         print(y) # iterating the arrays in each dimension that will return each value on array's  | 2D array

arr=np.array([[[1,2,3,4],[5,6,7,8]],[[11,22,33,44],[55,66,77,88]]])

# for x in arr:
#     print(x) # Default iteration 3D array

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z) # return each value at array's | 3D array

# for x in np.nditer(arr):
#     print(x) # using nditer to return the values, withou use n for loops

arr=np.array([1,2,3,4])
# for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']): # changing the value type, np doesn't do the type mutage in-place (where the element is in array), so it needs some more space, that extra space called buffer
    # print(x)
arr=np.array([[1,2,3,4],[5,6,7,8]])
void_array=np.array([])

# for x in np.nditer([arr[:,::2]]): #slicing arrays with nditer
#     print(x)
arr=np.array([1,2,3,4])

for idx,x in np.ndenumerate(arr): # enumerate the array values
    print(idx,x)
    