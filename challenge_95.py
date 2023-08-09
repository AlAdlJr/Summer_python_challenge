# Challenge 95 - Ismail AlAdl

# Display password requirements
print("Your password must be at least 10 characters long")
print("It must contain at least one uppercase and one lowercase letter")

# Setting validation variable
validPassword = False

# Loop to check if the password is valid
while not validPassword:
    validPassword = True
    # Input password
    password = input("Please enter password: ")
    # Check passord length
    if len(password) < 10:
        validPassword = False
        print("Must be at least 10 characters")
    # Check password is not all upper case
    elif password.isupper():
        validPassword = False
        print("Must contain at least one lowercase letter")
    # Check password is not all lower case    
    elif password.islower():
        validPassword = False
        print("Must contain at least one uppercase letter")
    # Disply if password does not fulfill the requirements
    if not validPassword:
        print("Invalid password")
    
# Display the password is valid    
print("Valid password entered")

# Input passord again to confirm
password_1 = input("Re-enter password to conferm: ")

# Check if passwords match
if password_1 != password:
    print("Invalid password entered")
else:
    print("Password confermed")

