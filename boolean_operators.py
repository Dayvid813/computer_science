is_computer_science_student = True
is_chang_jung_student = True

#and - both value must be true for the expression to be true
is_enrolled_and = is_computer_science_student and is_chang_jung_student
print('the value of our AND statement', is_enrolled_and)

#or - one of the values must be true for the expression to be true
is_enrolled_or = is_chang_jung_student or is_computer_science_student
print('the value of our OR statement', is_enrolled_or)

A = True
B = True
C = A or B #expect this to be ture if either A or B is true

D = True
E = False
F = D and E #expect F to be false if both D and E are not true

print(C)
print(F)

if(is_chang_jung_student and is_computer_science_student):
    print("You are enrolled in my computer science class")
elif(not is_computer_science_student and is_chang_jung_student):
    print("You are not in my computer science class")