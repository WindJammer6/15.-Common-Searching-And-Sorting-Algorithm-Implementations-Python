def bubble_sort(number_list):
    size = len(number_list)

    for i in range(size - 1):

        swapped = False
        for j in range(size - 1 - i):

            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    nums_list = [38, 28, 29, 7, 2, 15, 9]
    bubble_sort(nums_list)
    print(nums_list)
