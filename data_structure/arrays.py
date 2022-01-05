#first data sturcture
from array import array

#creat a new array using built in array method
test_scores = array("i", [90, 70, 40, 98, 97, 93])

# add another test scores to end of our array 
test_scores.append(100)

#add another test score to start of the array (possition 0)
test_scores.insert(0, 93)
print(test_scores[1])

#delete a number from our array
test_scores.remove(0)

#iterate over the array 
for score in test_scores:
    print(score)

#get length of the array
length = len(test_scores)
print(length)
