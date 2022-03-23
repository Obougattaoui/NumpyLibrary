# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:15:08 2022

@author: oussama

Numpy Library 
    used for working with arrays
    for working in domain of linear algebra, fourier transform, matrices
    NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
    the array object in numpy is 0called = ndarray
    
"""

"""
        Numpy is faster than Lists
    numpy arrays are stored at one continuous place in memory unlike lists
    so processes can access and manipulate them very efficiently.
    
"""

#Importing library
import numpy as np

#ndarray is the array object in Numpy
ndarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #we can pass a list, tuple or an array
print(ndarray)

#Matrix or 2D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
#check number of dimensions
print(arr.ndim)

#specify the number of dimension
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)

"""
    Access Array elements
array indexing is the same as accessing an array element.
"""
print(ndarray[0])
#access 2-D arrays
print("the first row and the 3nd element", arr[0, 2])
#negative indexing ==> to access an array from the end
print(ndarray[-2])

"""
    Slicing an array
slicing means taking elements from one given index to another given index.
[start:end]
[start:end:step]
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""
print(ndarray[1:4])
print(ndarray[4:])
print(ndarray[:4])
#negative slicing
print(ndarray[-3:-1])
#step
print(ndarray[1:5:2])
#2 D arrays
print(arr[1, 1:4])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#From both elements, return index 2
print(arr[0:2, 2])
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])

"""
        Numpy datatypes
Strings, Integer, float, boolean, complex
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
#checking the datatype of an array
print(ndarray.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#defined a datatype
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#defined size
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#converting a data type on existing array ==> make a copy of the array
arr = np.array([1.1, 2.3, 4.5])
newArray = arr.astype('i') #we can use also int
print(newArray)

"""
    Copy Vs View
view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
"""
x = ndarray.copy()
ndarray[0] = 100
print(x)
print(ndarray)
#view
x = ndarray.view()
ndarray[1] = 200
print(x)
print(x.base) #the copy returns None/ the view returns the original array

"""
    array shape
the number of elements in each dimension
shape is an attribute that returns a tuple with each index having the number of corresponding elements
"""
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #return (2, 4) ==> array has 2 dimensions where number of elements is 4

"""
    Reshaping arrays
means changing the shape of an array.
By reshaping we can add or remove dimensions or change number of elements in each dimension.
the elements required for reshaping are equal in both shapes.
Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#reshape form 1D to 2D
newArray = arr.reshape(4,3)
print(newArray)
#reshape from 1D to 3D
newArray = arr.reshape(2, 3, 2)
print(newArray)
#unkown dimension: Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.
newArray = arr.reshape(2, -1)
print(newArray)

"""
    Flattening the arrays
converting a multidimensional array into a 1D array.
"""
arr = np.array([[1,2,3], [4,5,6]])
newArray  = arr.reshape(-1)
print(newArray)

"""
    Iterating arrays
going through elements one by one
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
for x in arr:
    print(x)
#Iterating 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
#Iterating using for
for x in arr:
    print(x)
    for y in x:
        print(y)
#iterating using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
#Iterating array with different Data Types
#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
for x in np.nditer(arr, flags=["buffered"], op_dtypes=['S']):
    print(x)
#Iterating with different step size
for x in np.nditer(arr[:,:, ::2]):
    print(x)








