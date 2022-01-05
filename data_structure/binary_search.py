sorted_list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1
def binary_search(sorted_list, target):
    #set of the algorithm - getting the pointers ready
    left_idx = 0
    right_idx = len(sorted_list) - 1
    print(right_idx)

    #repeat steps - 
    #1. calculate the middle between two points
    #2. cheak if the value at the middle 

    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2) #cast to integer - make 5.0 10 5 w/ int () fn

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target <sorted_list[middle_idx]):
            right_idx = middle_idx -1
        else:
            left_idx = middle_idx +1

    return - 1 #if the value isn't in the list, return - 1 

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)