#Challenge 83 - Ismail AlAdl

# Making the lists of bookings for 
booking = [ [57,68,100,124], [43,52,92,101], [72,78,84,90] ] 

asking_month = int(input('what month would you like me to display? \n If May input 1 \n If july input 2 \n If June input 3 \n If August input 4 \n'))

if asking_month == 1:
    # Bookings for May
    print (booking [0] [0])
    print (booking [1] [0])
    print (booking [2] [0])
elif asking_month == 2:
   # Bookings for June
    print (booking [0] [1])
    print (booking [1] [1])
    print (booking [2] [1])
elif asking_month == 3:
    # Bookings for July
    print (booking [0] [2])
    print (booking [1] [2])
    print (booking [2] [2])
else:
   # Bookings for August
    print (booking [0] [3])
    print (booking [1] [3])
    print (booking [2] [3])