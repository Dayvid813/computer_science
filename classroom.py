sorted_list = [1, 3, 5, 6, 8, 9, 14, 15]
target_item = 5
def binary_search(sorted_list, target_item):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2)
        if(sorted_list[middle_idx] == target_item):
            return middle_idx
        elif(target_item < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return - 1
result = binary_search(sorted_list, target_item)
print('the target number is at list index:', result)