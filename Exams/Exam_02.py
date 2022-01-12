#1. Write code - Function with two parameters 
def addition(number, anotherNumber):
    return number + anotherNumber
result = addition(1, 3)
print(result)

#2. Write code - Random Number generation @@
import random
rannumber = random.randint(0, 99)
print(rannumber)


#3. Write code - While loop
number = 0
while (number < 5):
    print("Today, I am outstanding in every way")
    number = number + 1

#4. Write code - For loop
for i in range(200):
    print("I become what I think about most of the time")

#5. Write code - User input
name = input("What is your name?: ")
print("You look great today", name)

#6. Write code - string operations (length method)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
print(alphabet_length)

#7. Write code - string operations (find method)
position_of_letter_j = alphabet.index("j")
print(position_of_letter_j + 1)

#8. Write code - data structures (Arrays)
from array import array
test_scores = array("i", [90, 70, 40, 98, 97, 93])
#9. Write code - data structures (Arrays)
test_scores.append(89)
#10. Write code - data structures (Arrays)
length = len(test_scores)

#11. Write code - data structures (Lists)
IGCSE_ComputerScience_students = ["Arsalon", "David", "Howard"]
#12. Write code - data structures (Lists)
IGCSE_ComputerScience_students.remove("Arsalon")
#13. Write code - data structures (Lists)
IGCSE_ComputerScience_students.sort()
print(IGCSE_ComputerScience_students)

#14. Write code - data structures (dictionaries)
total_exam_score = {"David": [100, 100, 100], "Arsalon": [99, 100, 99], "Howard": [100, 100, 100]}
#15. Write Code - Data Structures (dictionaries)
Arsalon_score = total_exam_score.get("Arsalon")
print(Arsalon_score)