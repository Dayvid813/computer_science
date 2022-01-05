student_names = ["Mike", "amy", "marco", "david"]

#add a nam to our list
student_names.append("Mars")
student_names.insert(0, "Mr.Amini") #insert at index (0) first position

#delete a name
student_names.remove("marco")

#iterate over our list
for name in student_names:
    print(name)

#Create a nre list represent class letter grades 
letter_grade = ["A", "A-", "A", "B", "B", "C", "C"]

#count numberof people with grade A
number_of_A_grades = letter_grade.count("A")
print("number of grades A:", number_of_A_grades)

numbers = [0, 0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 3, 4, 5, 6, 7]
zero_frequency = numbers.count(0)
print("number of zeros:", zero_frequency)

#boolean list
has_completed_homework = [True, True, False, True, False, False, True]
number_of_completed_homeworks = has_completed_homework.count(True)
print("number of people who did homework:", number_of_completed_homeworks)

#sort list using built in list method .sort
student_names.sort()
for name in student_names:
    print(name)


#integer list 
numbers = [0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 4, 3, 3, 2, 1, 1]

#cpunt number of zeros
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#sort list
numbers.sort()

#print each item in list (iteration)
for number in numbers:
    print(number)

numbers = [100, 50, 10, 300, 55, 0, 1, 44, 23, 22, 55, 89, 90]

numbers.sort()

for number in numbers:
    print(number)

#create a bollean values to represent students who have one their homework
has_done_homework = [True, False, False, False, True, False, True, True]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)
number_of_False = has_done_homework.count(False)
print("number of people who did homework:", number_of_False)

#iterate (traverse the data structure)
for students in has_done_homework:
    print(students)

#make a list that stores amount of money each student has in their pocket

money_in_student_pockets = [153, 123, 343, 435, 6453, 23455, 75644, 5454]
print(money_in_student_pockets)
money_in_student_pockets.sort()
print(money_in_student_pockets)
money_in_student_pockets.append(34)
print(money_in_student_pockets)

#create a list of strings
student_name = ["Mike", "Leon", "Henry", "Howard", "Rain","Hanson", "Charlie", "Barbie", "Mars", "Marco", "Angelina", "Mandy", "Yujing", "David"]
student_name.sort()
print(student_name)