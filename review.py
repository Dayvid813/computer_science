# data types
#1 write a variable that stores a boolean value
Quizlet_is_good = False
computer_science_is_difficult = True
name = input("Enter your name: ")
print("Welcome to Summoner's Rift")

#2 write a variable that stores an integer
my_conputer_science_grade = 96

#3 write a variable that stores a floting point number
pi = 3.1415926535897932384656

#loop 
#3 write a for loop that says "happybirthday Barbie + Howard" 12

for number in range(14):
    print("happy birthday Barbie and Howard")

#while loop 
#4 write a while loop to print "Good morning" 4x
number = 0
while(number < 4):
    print("Good morning")
    number = number + 1

#function
#5 write a function that takes two arguments and return the sum of those two args
def function(number, anotherNumber):
    return number + anotherNumber
print(function(10,10))

#6 ramdom number generation
import random
random_number = random.randint(1,100)
print(random_number)