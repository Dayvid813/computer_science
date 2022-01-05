#Create a dictionary (key-valuepairs) aka "HashMap, Map, HashTable"
assignment_scores = {"Mars": 90, "Amy": 93, "Rain": 98, "CHarlie": 98}
amy_assignment = assignment_scores.get("Amy")
print("Amy assignment score", amy_assignment)

#Create a dictuinary using built in dict function (same thing, dufferent function)
exam_scores = dict(Mars=90, Amy=93, Rain=98, Charlie=98)
mars_score = exam_scores.get("Mars")
print("Mars exam score", mars_score)
#iterate over the keys in the dictionary
for key in exam_scores:
    print(key)


#key - studens name value - boolean represent wheather or not the student has pets
has_pets = {"Mars": False, "Henry": False, "Barbie": True, "Angelina": False, "Teacher": True}


#data sturcture operations - add, delete. search. sort
student_has_pets = has_pets.get("Mars")
print("The student has a pet", student_has_pets)

#traverse the dictionary
for student in has_pets:
    print(student, "has a pet", has_pets.get(student))

#removed method - .pop()
student_removed = has_pets.pop("Teacher")
print(student_removed)
print(has_pets)

#create a dictionary (key-value pair)
#key = student name
#value = list of scores (numbers)
student_scores = {"Charlie": [88, 99, 100], "Mandy": [90, 95, 99], "Yujing": [100, 99, 95], "Angelina": [99, 98, 99], "Mr.Amini": [50, 99 , 99]}
students_scores = student_scores.get("Angelina")
for score in student_scores:
    print(score)

#dictionary to represent sibling names of students
student_siblings = {"Howard": ["Barbie", "Anthony", "Annie"], "Barbie": ["Howard", "Anthony", "Annie"], "Mike": ["Angel"], "Yujing": ["Jimmy"]}

student_brothers_sisters = student_siblings.get("Howard")
student_brothers_sisters.sort()
for sibling in student_brothers_sisters:
    print(sibling)

student_classes = {
    "David": ["IGCSE Math", "IGCSE Physics", "IGCSE Computer Science", "IGCSE ESL"],
    "Howard": ["IGCSE Math","IGCSE Computer Science", "Think American 3"],
    "Leon": ["Think American 3", "IGCSE Chemistry", "IGCSE Physics"],
    "Rain": ["Think American 3", "IGCSE Business", "IGCSE Math"]
     }
class_student_takes = student_classes.get("David")
class_student_takes.sort()
for classes in class_student_takes:
    print(classes)