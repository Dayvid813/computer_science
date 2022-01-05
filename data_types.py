#1 varialbe - 
#a) wrtie a boolean to represent whether or not you will pass the exam
passed_exam = True

#b) write an integer variable to represent your score on the exam 
my_score_on_the_exam = 100

#c) write a flostin point variablr to represent the class average on the exam
class_average = 87.9

#d) write a string variable to represent something you'd say to your friend in the morning
message = "Good morning"

#2 iterations - for loops
#a) write a for loops that print " I am a polite and kind person" *10
for number in range(10):
    print("I am a polite and kind person")

#comtrol flow - wite a simple if-lif a statement to describe this..
#a)if student has a grade of 90-100 print "you rockstar student"
#b)elif student has a grade of 80-90 print "you are good"
#c)elif student has a grade of 80-90 print "not bad, keep working"
#e)elif student has a grade of 70-80 print "keepworking champ"

stuent_grade = 99
if stuent_grade > 90 and stuent_grade <= 100:
    print("you rockstar student")
elif stuent_grade > 80 and stuent_grade <= 90:
    print("you're amazing, keep leveling up")
elif stuent_grade > 70 and stuent_grade <= 80:
    print("not bad, growth mindset, you got it")
else:
    print("you can always do more and become more, gorth mindset")



#Data Types Lecture
computer_science_students = 21 #this is an integer value
has_done_homework = True/False #this is an boolean value
class_name = "IGCSE Computer Science" #this is a string value

#we can now access this data by the variable name
print(computer_science_students)
print(has_done_homework)
print(class_name)

def greetings(hello_teacher_amini):
    return hello_teacher_amini

print = greetings

