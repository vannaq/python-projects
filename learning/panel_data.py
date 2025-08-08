#Pandas (Panel Data) is an open source library with data structures and data analysis tools for Python
#Dataframe is one of Pandas' most important data structures. It's a way to store tabular data 

#Let's create some lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drive = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

#Import pandas as pd
import pandas as pd

#Create a dictionary with three key:value pairs
my_dict = {'country':names, 'drives_right':drive, 'cars_per_cap':cpc}

#Build a Dataframe from the dictionary that was just created
cars = pd.DataFrame(my_dict)
print(cars)                                                             #An indexed table of 7 rows and 3 columns was built.
print("\n")

#Let's label the rows instead of leaving them as indexed values
row_labels = ["US", "AUS", "JPN", "IN", "RU", "MOR", "EG"]              #Create a list of row labels to use
cars.index = row_labels                                                 #Use index attribute to set the index of cars to row_labels
print(cars)                                                             #Prints updated table with row labels instead of index numbers
print("\m")


#Import CSV to DataFrame using pd.read_csv('filename.csv')
#Specify the first column to be used as row labels by adding argument index_col = 0 -->  variable = pd.read_csv('filename.csv', index_col=0)


#Use single square brackets to get Pandas Series
#Use double square brackets to get Pandas DataFrame
#Use square brackets to get rows, or observations, from a DataFrame
# loc is label-based; need to specify rows and columns based on their row and column labels
# iloc is integer index-based; need to specify rows and columns by their integer index




#Note: Python script cannot be named the same thing as an existing package. 
#For exmaple, this script was initially named pandas.py and that returned an AttributeError.
#This is due to Python's import mechanism where it prioritizes current directory so when a script is named the same as a package, and you import the package, Python will find and import the script first instead of the standard module.