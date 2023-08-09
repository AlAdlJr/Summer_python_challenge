# Challenge 77 - Ismail AlAdl

# Creating lists of planets and moons
planetList = []
moonList = []
moreData = True
print("\nPlanets and moons\n")

# While loop to get the name of the planets and the number of moons it has
while moreData:
    planetName = input("Enter name of planet, xxx to finish: ")
    if planetName == "xxx":
        moreData = False
    else:
        numMoons = int(input("Enter number of moons: "))
        planetList.append(planetName)
        moonList.append(numMoons)

# For loop to print the output
for index in range(len(planetList)):
    if moonList[index] == 1:                       
        print(planetList[index] + " has " + str(moonList[index]) + " moon")
    else:
        print(planetList[index] + " has " + str(moonList[index]) + " moons")
                   