#Dictionaries store key value pairs in curly brackets so we don't need to set up 2 lists and reference the indexes to retrieve a value
#Keys in a dictionary should be unique 
#Lists in a dictionary can be changed after its created

pop = [30.55, 2.77, 39.21]                                                  #Let's create a list of population sizes
countries = ['afghanistan', 'albania', 'algeria']                           #List of corresponding countries to the population sizes

world = {'afghanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}           #Create a dictionary named world with key value pairs
print(world['albania'])                                                     #Print the value corresponding to the "key" albania. The key opens the door to the value.
print(world.keys())                                                         #Prints out all keys of world dictionary. .keys() is a method of dictionary objects in Python.
print("\n")


#Add to dictionary
world['croatia'] = 32.4
print('croatia' in world)                                                   #Ensure croatia was added to dictionary; should return True
print(world)                                                                #Print world dictionary to see the newly added key value pair for croatia
print("\n")

#Remove from dictionary
del(world['albania'])                                                       #It appears the population for albania was wrong so we need to remove it from the dictionary
print(world)                                                                #Check to see if albania was removed. Notice that when script is run, albania is still there in the beginning. This is because order matters in Python. 
print("\n")


#Dictionaries can contain key:value pairs where the value is a dictionary
print("Dictionary of dictionaries")
europe = { 'spain': {'capital':'madrid', 'population': 46.77},
            'france': {'capital':'paris', 'population': 66.03},
            'germany': {'capital':'berlin', 'population': 80.62},
            'norway': {'capital':'oslo', 'population':5.084}}

print(europe['france'])                                                     #Prints out the capital of France and its population
data = {'capital':'rome', 'population':59.83}                               #Creates a sub-dictionary named data containing the capital of Rome and its population
europe['italy'] = data                                                      #Adds data to europe under key value "italy"
print(europe)                                                               #Prints out the latest dictionary named europe with italy and its list added