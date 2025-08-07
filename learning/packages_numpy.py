#A package is a collection of Python code bundled for organization and reuse. It is a collection of modules, each containing functions and methods for specific tasks.
#To use a package, it must be installed and imported.

#1D Array Example
import numpy as np                                      #After NumPy package is installed, import it in your code to use
pizza_size = [6.0, 8.0, 9.0, 10.0, 12.0, 16.0, 20.0]    #Let's create a list of pizza sizes
np_pizza_size = np.array(pizza_size)                    #Create a numpy array from the list of pizza sizes
print(type(np_pizza_size))                              #Print out type of np_pizza_size, which should return numpy array
print(np_pizza_size[4])                                 #Print out element in the 4th index of array 
print(np_pizza_size[4:])                                #Print out elements starting from 4th index to end of array
print("\n")


#2D Array Example
burger = [[4.0, 50],                    #Let's create a list containing 5 elements. Each element is a list containing diameter and weight of homemade burgers.
          [5.0, 85],
          [6.0, 88],
          [8.0, 112],
          [8.0, 133]]             

#Create a 2D numpy array from burger
np_burger = np.array(burger)     
print(type(np_burger))                        #Print out the type of np_burger, which should show array
print(np_burger.shape)                        #Print out the shape of np_burger, which should show how many rows, columns
print("\n")

#Print out 3rd row of np_burger
print(np_burger[2,:])                         #Indexes before the comma refer to rows, after the comma refer to columns. : is for slicing and tells Python to include all columns in this case.
print(np_burger[:,0])                         #Print out all rows, first column
print("\n")


#NumPy Basic Stats
print(np.mean(np_burger))                     #Print out mean of all elements in np_burger
print(np.mean(np_burger[:,0]))                #Print the mean of all rows in first column of np_burger
print(np.median(pizza_size))                  #Print the median of elements in pizza_size list

stddev = np.std(np_burger[:,1])
print("Standard Deviation: " + str(stddev))   #Print standard deviation of homemade burger weight