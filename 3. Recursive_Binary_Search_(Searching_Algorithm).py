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


if __name__ == '__main__':
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32
    index = recursive_binary_search(nums_list, num_to_find)
    print(f"Number found at index {index} using recursive Binary Search")
