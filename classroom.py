sorted_list = [1, 4, 6, 7, 8, 10, 14, 15]
target = 4
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2)
        if(sorted_list[middle_idx == target]):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return - 1
result = binary_search(sorted_list, target)
print('the target number is at the list index:', result)
