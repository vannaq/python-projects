#Functions are reusable pieces of code that do something. It is called using parentheses ().
print("hello world!\n")   #Print is a function that returns whatever's in the parentheses
len('Hello')    #len is a function that returns length of string
sum([1,2,3])    #sum is a function that returns the sum of a list


#Everything is an object in Python as long as it has a type, properties, and a method -> strings, lists, floats. 
#A method is a function that belongs to a specified type of object. 
areas = [18.0, 11.25, 20.0, 19.75, 9.40, 11.25]
print(areas.index(19.75))       #Print out the index of element 20.0. Notice the parentheses around 19.75; a function is called using parentheses. 
print(areas.count(11.25))       #Print out the number of times 11.25 appears in areas list
areas.append(23.50)             #Adds 23.50 to the areas list
print(areas)                    #Print areas list to confirm 23.50 was added
print("\n")


