password = input("ex/nter a password:")

password_length = len(password)

if(password_length < 7 or password_length > 15):
    print("your password must be between 7 - 15 chracters")

#data validation - 
admin_password = input("enter your new password")
admin_password_length = len(admin_password)

if(admin_password_length >= 6 and admin_password_length <= 12):
    print("password is updated")
else:
    print("password must be 6 - 12 chraacters")

name = input("Enter your name: ")

#check if user enters an empty string

name_length = len(name)

if(name_length == 0):
    print("You cannnot more enter an empty name")
elif(name_length < 3):
    print("Name must be more than three letters")
elif(name_length > 25):
    print("name must be less than 25 chracters")



#write a program that takes a newe pet name and validates its length
#in other words, it prints an error message to the user if...
#the name is less than 2 chars and greater than 20 chars.

#outline the steps - algorithm
#ask user for pet name, store it in a variable
#use fn to get pet name length, store length in a new variable
#validate - if-elif to print error messages if len is outside boundaries

pet_name = input("Enter your pet name: ")
pet_name_length = len(pet_name)

if(pet_name_length == 0):
    print("You must enter something")
elif(pet_name_length < 2):
    print("Error. You can't enter your pet name less than 2 chars.")
elif(pet_name_length >= 20):
    print("Error. You can't enter your pet name greater than 20 chars.")
else:
    print("Hello", pet_name)


#validation task - write code that takes user input and validates its length
#ask the user for a restaurant name
#validate that the name is greater than 5 letters and less than 55 letters

#1
restaurant_name = input("Enter a restaurant name: ")
print(restaurant_name)
#2
restaurant_name_length = len(restaurant_name)

if(restaurant_name_length == 0):
    print("you must enter something")
elif(restaurant_name_length < 5):
    print("You have to write down the name more than 5 letters")
elif(restaurant_name_length > 55):
    print("You have to write down the name less than 55 letters")
else:
    print("It is good name")