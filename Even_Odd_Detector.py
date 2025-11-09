number = int(input("Enter A Number:" )) # we use int() because input() only accepts strings
if number % 2 == 0:
    print(number, "is even")
if number % 2 != 0:
    print(number, "is odd")