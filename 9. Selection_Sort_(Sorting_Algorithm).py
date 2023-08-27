def selection_sort(number_list):
    for i in range(len(number_list) - 1):
        minimum_element_index = i

        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[minimum_element_index]:
                minimum_element_index = j

        if number_list[i] != number_list[minimum_element_index]:
            number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 11]
    selection_sort(nums_list)
    print(nums_list)
