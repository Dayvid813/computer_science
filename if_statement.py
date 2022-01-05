#programs make decisions based on control logic (contorl flow)
students_grade = 99
if students_grade >= 100:
    print("Your grade is A+")
elif students_grade < 100 and students_grade >90:
    print("Your grade is A")
elif students_grade < 90 and students_grade > 80:
    print("Your grade is a B")
elif students_grade < 80 and students_grade >70:
    print("Your grade is a C")
else:
    print("Your grade is a D or F")

temperature = 6
if temperature >= 30:
    print("it's hot")
elif temperature < 30 and temperature > 10:
    print("it's warm")
elif temperature < 10 and temperature > 5:
    print("it's cold")
else:
    print("bring an umbrella just in case")




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

