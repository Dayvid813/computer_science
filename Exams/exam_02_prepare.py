#Create a list of boolean values to represent students who participated in the Chang Jung Senior High School International Division Secret Santa.
participant_secretsanta = [True, True, False, True, False, False]
#Using the built in list methods, write code to count the number of students who participated (“True” values). Print on the screen
number_of_secretsanta = participant_secretsanta.count(True)
print(number_of_secretsanta)
#Using the built in list methods, write code to sort the list so that all True values are first and all False values come second. 
participant_secretsanta.sort(reverse = True)
print(participant_secretsanta)

#Create a dictionary that stores the students’ names (string) as the key, and a list of their past three exam scores (list of integers). 
Exam_score = {"David": [96, 93, 88], "Mars": [86, 78, 88], "Howard": [95, 94, 91], "Rain": [97, 88, 91], "Mr.Amini": [99, 98, 100]}
#Using the built in dictionary methods, get Mr. Amini’s exam scores (a list) and print them out on the screen (for each loop)
MrAmini_score = Exam_score.get("Mr.Amini")
for score in MrAmini_score:
    print(score)

#Create a dictionary that stores the students names and their pets’ names (at least 3 each). 
pet_names = {"Daivd": ["cat", "cat02","cat03"], "MrAmini": ["dog", "cat04", "dog02"], "Howard": ["dog_03","dog04", "dog05"]}
#Using the built in dictionary methods, get Mr. Amini’s pets’ names.
MrAmini_pet = pet_names.get("MrAmini")
#Using the built in dictionary methods, sort the list of strings (Mr. Amini’s pet names) and print the sorted list on the screen 
MrAmini_pet.sort()
print(MrAmini_pet)

