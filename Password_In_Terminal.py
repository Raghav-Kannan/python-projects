password = input("Create your password: ") # creates password

if len(password) > 8: # checks the length of your password
    print("Your password is secure.")
else:
    print("You password is less than 8 characters long, add more characters.")

if len(password) > 8 and password.isalnum(): # checks if password contains alphanumeric characters
    print("Your password is valid.")
else:
    print("It seems like you entered a space somewhere. Your password must contain only alphanumeric characters.")

user_input = input("Enter your password: ") # enters password
if user_input == password: # verifies if password is correct or not
    print("Your password is correct. Welcome.")
else:
    print("You password is incorrect. Please try again.")