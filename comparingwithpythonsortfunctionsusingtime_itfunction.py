from time_it import time_it

#Linear Search Algorithm
@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1

#Iterative Binary Search Algorithm
@time_it
def iterative_binary_search(numbers_list, number_to_find):

    left_index = 0
    right_index = len(numbers_list) - 1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = numbers_list[middle_index]

        if middle_number == number_to_find:
            return middle_index
        
        if middle_number < number_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1

#Recursive Binary Search Algorithm
@time_it
def recursive_binary_search(numbers_list, number_to_find, left_index, right_index):

    if right_index < left_index:
        return -1
    
    middle_index = (left_index + right_index) // 2
    if middle_index >= len(numbers_list) or middle_index < 0:
        return -1
    middle_number = numbers_list[middle_index]

    if middle_number == number_to_find:
        return middle_index
    
    if middle_number < number_to_find:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1

    return recursive_binary_search(numbers_list, number_to_find, left_index, right_index)


