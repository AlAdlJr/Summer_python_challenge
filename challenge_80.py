# Challenge 80 - Ismail AlAdl

# Creating lists of planets and percantages
planet = ["Jupiter" , "Saturn" , "Uranus" , "Neptune" , "Venus" , "Mercury" , "Mars" , "Earth"]
percentage = ["1120%" , "945%" , "400%" , "390%" , "95%" , "53%" , "38%" , "100%"]

# Operations to write out the name of the planet and its percentage size relative to earth
for i in range (len(planet)):
    print(planet[i] + " is " + percentage[i] + " the size of earth")

print("\n Sorry Neptunes information is wrong we will print the right information \n")

# Deleteing 390%
del percentage[3]

# Inserting 388%
percentage.insert(3,"388%")

# Printing the new lists
for i in range (len(planet)):
    print(planet[i] + " is " + percentage[i] + " the size of earth")
