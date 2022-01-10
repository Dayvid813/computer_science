#Create a list of boolean values to represent students who participated in the Chang Jung Senior High School International Division Secret Santa.
participant_secretsanta = [True, True, False, True, False, False]
#Using the built in list methods, write code to count the number of students who participated (“True” values). Print on the screen
number_of_secretsanta = participant_secretsanta.count(True)
print(number_of_secretsanta)
#Using the built in list methods, write code to sort the list so that all True values are first and all False values come second. 
participant_secretsanta.sort(reverse = True)
print(participant_secretsanta)