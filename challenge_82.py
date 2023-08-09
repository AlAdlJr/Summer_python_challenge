# Challenge 82 - Ismail AlAdl

# Making the lists of bookings for 
booking = [ [57,68,100,124], [43,52,92,101], [72,78,84,90] ] 

# DIFING VARIABLES 
totalMay = 0
totaljune = 0

# Printing the bookings
print(booking)

# Getting the total bookings for may
for row in range(3):
	totalMay = totalMay + booking[row][0]	
print ("Total bookings in May: ",totalMay) 

# Getting the total bookings for june
for row in range(3):
	totaljune = totaljune + booking[row][1]
print("Total bookings in june:" , totaljune)

# Deleting a data in a row
del booking [1][2]

# Adding a data in a row
booking[1][2]= "96" , "101"

# printing the bookings
print(booking)
