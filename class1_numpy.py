# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=10
print(x)
x
l1=[10,20,30,40,50]
type(l1)
l2=[]
l3=list()

# Numpy-Numerical python

import numpy as np
arr1=np.array([100,200,300,400,500,500,600])
type(arr1)
# create an array from a list l1
l1=[10.3,5.6,7.8,9.0,11.5]
arr2=np.array(l1)
type(arr2)
print(arr1)
print(arr2)
#we can also print like only naming the variable
arr1
arr1[0]
arr2
arr4=np.array(['aaa','bbb','ccc','ddd'])

import numpy
arr3=numpy.array(['aaa','bbb','ccc','ddd'])


#from numpy import *
#arr5=array([10,20,30])
#arr5

arr1
#what is the dimension of arr1?
arr1.ndim
#what is the shape of arr1?
arr1.shape
#what is size?
arr1.size
#what is the type of values stored in the array?
arr1.dtype
#what is the type of arr1?
type(arr1)
type(x)

a1=np.array([])


str1="good morning everyone"
str1.split()
arr6=np.array(str1.split())
arr6

a2=np.array((10,20,30,40,50,60,70)).reshape(3,2)
x=10
x=20
a1=np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)

#check the attributes of the 2D array
a1.ndim
a1.shape
a1.size
a1.dtype

# arange method
a3=np.arange(20)
a4=np.arange(20).reshape(5,4)
a4=np.arange(1,50,2)
a5=np.arange(1,50,2).reshape(5,5)
a5.reshape(5,5)

#indexing
a3[0]
a5[0]
a5[3]
a5[0:3]
a5[3:5]
a5[:,]
a5[:,1]
a5[:,0:2]
a5[0:3,2:4]
a5[1:4,1:4]
a5[-1]
a5[:,-1]
a5[-1,-1]
a5[0,0]
a5[1,2]

#creating a 3D array

b1=np.arange(27)
b1
b1.ndim
#2Darray
b2=np.arange(27).reshape(9,3)
b2
b2.ndim
#3Darray
b3=np.arange(27).reshape(3,3,3)
b3
b4.ndim
b4=np.arange(120).reshape(4,5,6)
b4


























