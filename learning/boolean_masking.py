# This script is an example of boolean masking and how it's applied

import numpy as np

cookie_dough = np.array([1, 2, 3, 4, 5, 6, 7, 8]) #Creating a numpy array of numbers named cookie dough
stencil = cookie_dough > 4  #Creating a boolean mask named stencil. This boolean mask is created based on the specified condition of elements in the cookie dough array greater than 4. Note that a boolean mask is an array of True or False values.

cookie = cookie_dough[stencil]  #Apply the boolean mask to the array. This is akin to applying the stencil to cookie dough to get the desired shape.
print(cookie) #The result should be what you'd expect from the boolean mask previously created.


cookie_dough2 = np.array([10, 234, 45, 65, 78, 201, 2, 23]) #Creating a new numpy array containing different numbers to illustrate what happens when stencil is applied
cookie2 = cookie_dough2[stencil]    #Since stencil was previously created, it can be applied again
print(cookie2)  #Note that the boolean mask, aka stencil, returns True for the last 4 elements of the 8 element array, regardless of what element is within the array. This is true and applicable only if the arrays contain the same number of elements. 


cookie_dough3 = np.array([1, 3, 55, 223, 5656, 1324, 435, 22, 122, 58, 23, 44, 202])
cookie3 = cookie_dough3[stencil]
print(cookie3)  #This will return an error stating that the boolean index did not match indexed array along axis 0. The number of array elements in the boolean mask and the specified array must match in order for boolean mask to be applied.