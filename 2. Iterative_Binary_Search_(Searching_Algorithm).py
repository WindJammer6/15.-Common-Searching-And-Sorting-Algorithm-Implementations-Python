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


if __name__ == '__main__':
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32
    index = iterative_search(nums_list, num_to_find)
    print(f"Number found at index {index} using iterative Binary Search")
