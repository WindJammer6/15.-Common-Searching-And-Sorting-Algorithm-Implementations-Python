def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1


  if __name__ == '__main__':
    nums_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    num_to_find = 32
    index = linear_search(nums_list, num_to_find)
    print(f"Number found at index {index} using Linear Search")
