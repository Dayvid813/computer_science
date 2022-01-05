#get and store user input
name = input("Enter your name: ")

#output the user input an the screen
print("Good morning", name)

#ask user to enter a number (integer)
#save it in a variable called "number"
number = int(input("Enter a number:"))

#defining a new function called "get_square"
#it takes one value and return value * value (square)
def get_square (number):
    return number * number

#call function, pass user input, print output
#save the result in a variable called "square"
#print the va;ue of "square" on screen
square = get_square(number)
print(number)