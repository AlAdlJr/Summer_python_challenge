# Challenge 81 - Ismail AlAdl

# Creating lists of planets and percentages
planet = ["Jupiter" , "Saturn" , "Uranus" , "Neptune" , "Venus" , "Mercury" , "Mars" , "Earth"]
percentage = ["1120%" , "945%" , "400%" , "388%" , "95%" , "53%" , "38%" , "100%"]

# Operations to write out the name of the planet and its percentage size relative to earth
for i in range (len(planet)):
    print(planet[i] + " is " + percentage[i] + " the size of earth")

# Printing the biggest and smallest planets
print("\n" + planet[0] + " is " + percentage[0] + " the size of earth. It is also the bigest planet")
print(planet[6] + " is " + percentage[6] + " the size of earth. It is alos the smallest planet")