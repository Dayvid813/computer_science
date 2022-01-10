sorted_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
def binary_search(sorted_list, target):
    #set of the algorithm - getting the pointers ready
    left_idx = 0
    right_idx = len(sorted_list) - 1

    #repeat steps - 
    #1. calculate the middle between two points
    #2. cheak if the value at the middle 

    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2) #cast to integer - make 5.0 10 5 w/ int () fn

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1

    return - 1 #if the value isn't in the list, return - 1 

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)






sortedlist = [1, 3, 5, 6, 7, 8, 9, 13, 14, 16, 18]
item = 9
def binseach(sortedlist, item):
    leftidx = 0
    rightidx = len(sortedlist) - 1

    while(leftidx <= rightidx):
        middleidx = int((leftidx + rightidx) / 2)

        if(sortedlist[middleidx] == item):
            return middleidx
        elif(item < sortedlist[middleidx]):
            rightidx = middleidx - 1
        else:
            leftidx = middleidx + 1

    return -1

resultt = binseach(sortedlist, item)
print('the target number is at list index:', resultt)

sortlistt = [1, 4, 5, 6, 7, 8, 9, 14, 15, 18, 19,]
target_item = 18
def bsearch(sortlistt, target_item):
    leftdx = 0
    rightdx = len(sortlistt) - 1
    while(leftdx <= rightdx):
        middledx = int((leftdx + rightdx) / 2)
        if(sortlistt[middledx] == target_item):
            return middledx
        elif(target_item < sortlistt[middledx]):
            rightdx = middledx - 1
        else:
            leftdx = middledx + 1
    return - 1
resulttt = bsearch(sortlistt, target_item)
print('the target number s at list index:', resulttt)