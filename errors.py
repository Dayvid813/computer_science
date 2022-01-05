#user input error - this throws an exception if a is given by user 
age = int(input("Enter your age:"))


#try-catch block
try:
    age = int(input("Enter your age:"))
    calculation = 10/age
except (ValueError, ZeroDivisionError) as error:
    print("please enter a valid")
    print(error)

print("if this is executed the pgrom didn't")