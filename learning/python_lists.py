#Define variables
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.5

#Create a list named areas
areas = [hall, kit, liv, bed, bath]     #Use square brackets when building and accessing lists
areas2 = ['hallway', hall, 'kitchen', kit, 'living room', liv, 'bedroom', bed, 'bathroom', bath, 'laundry', 88]   #Lists can store a mix of strings, variables, integers  

print(areas)
print(areas2)       
print("\n")     #Prints new line


#Access data in list using indexes
my_kit = areas[1]
print(my_kit)
print("\n")     #Prints new line


#Create a list of lists named house
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]


#Slice lists using a colon to create downstairs
downstairs = areas2[:6]     #Lists are referenced by index [start:end] so this is returning everything from beginning to 5th element; 6th element is not included
print(downstairs)
print("\n")

upstairs = house[3:]        #This is returning everything from 4th element, index 3, to the end of the list
print("upstairs using house list") 
print(upstairs)


#Subset, or splice, the house list to get 9.5
print(house[4][1])      #Index 4 is looking at the 5th row of the list and index 1 is the second element of that row
print("\n")


#Adding elements to a list
new_house = house + ['garage', 18.5]
print(new_house)