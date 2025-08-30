#Let house be a list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         

def print_room_size(house, unit="sqm", complex=True):                         #We define a function here to print room size, with parameters house and unit. The default value of the unit parameter is sqm when a unit argument is not passed.
    if complex:
        print("Complex")                                                      #To illustrate how this function works given the two ways of printing the x is y unit, we define a parameter named complex.
        for room, house in enumerate(house):                                  #Using enumerate here is unnecessary, but it works to print out "the x is y sqm" where x is the name of the room and y is the area of the room
            print(f"the {str(house[0])} is {str(house[1])} {unit}")           #Beginner's basic version would be --> print("the " + str(house[0]) + " is " + str(house[1]) + " " + unit)
    else :
        print("Simple")                                                       #The simple, straightforward way of printing out "the x is y in"; using inches here instead of sqm to differentiate from compexs
        for room in (house):
            print("the " + room[0] + " is " + str(room[1]) + " in")

print_room_size(house, unit="ftm", complex=False)                              #If we pass the argument complex=False, then this would print the Simple version. Note the units - it prints out inches and not ftm or sqm because it is processing the else loop.


print("\n")         


#The names for key and value are arbitrary, can call them anything and it would still return key first, value second (order matters)
#To iterate over key-value pairs in a dictionary, use the .items() method on dictionary to define the sequence in the for loop  --> Note: Dictionaries require a method

#Let's create a dictionary named europe and include definitions, or countries
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

#Use .items() method to iterate over europe to print "The capital of x is y"
for k, v in europe.items():
    print("The capital of " + k + " is " + v)



#To iterate over all elements in a NumPy array, use the .nditer() to specify the sequence --> Note: NumPy arrays use a function



#While loops are less common in data science but good to know and understand