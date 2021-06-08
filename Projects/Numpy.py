#%%
import numpy as np

a = np.array ([1,2,3])
print(a)

a = np.array([1, 2, 3,4,5], ndmin = 1) 
print (a)
## minimum dimensions

# dtype parameter
a = np.array([1,2,3], dtype = complex)
print (a)

np.eye(3)
#matrix

# check number of dimensions
import numpy as np
a = np.array(42)
print (a.ndim)

#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

#negative slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

rr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

#2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])

#data type
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
#data type

#shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
#shape

#reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
#reshaping

 #iterating  array
arr = np.array([1, 2, 3])

for x in arr:
  print(x)
 #iterating  array
 
 #iterating 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
    #iterating 2D array
    
#iterating
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
#iterating
    
#join
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
#join
    
#join using stacks
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
#join using stacks
    
#join using rows
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
#join using rows
    
#join using columns
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
#join using columns
    
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
    
#searching (index)

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
    
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

#
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)
#return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order
#

#sort
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

#%%    
#GENERATE RANDOM NUMBER

from numpy import random

x = random.randint(100)

print(x)

#%%
x = random.rand()

print(x)
#%% 

x = random.randint(100, size=(3, 5))

print(x)

#%%

x = random.choice([3, 5, 7, 9])

print(x)
#choice() method also allows you to return an array of values
    
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
#permutation() method returns a re-arranged array (and leaves the original array un-changed
    
a = np.arange(10,50)
print(a)
    
    
    
    
    
    
    
    
    