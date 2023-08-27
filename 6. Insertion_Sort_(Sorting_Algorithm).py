def insertion_sort(number_list):

    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1
 
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j = j - 1

        number_list[j + 1] = anchor


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 11]
    insertion_sort(nums_list)
    print(nums_list)
