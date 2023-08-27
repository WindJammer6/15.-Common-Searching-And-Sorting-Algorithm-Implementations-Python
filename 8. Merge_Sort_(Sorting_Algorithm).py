def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a, smaller_sorted_list_b, array):

    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            array[k] = smaller_sorted_list_b[j]
            j += 1
        k += 1

    while i < len(smaller_sorted_list_a):
        array[k] = smaller_sorted_list_a[i]
        i += 1
        k += 1

    while j < len(smaller_sorted_list_b):
        array[k] = smaller_sorted_list_b[j]
        j += 1
        k += 1


def merge_sort(array):

    if len(array) <= 1:
        return array
    
    middle_element_index = len(array)//2
    
    left_smaller_subarray = array[:middle_element_index]
    right_smaller_subarray = array[middle_element_index:]

    merge_sort(left_smaller_subarray)
    merge_sort(right_smaller_subarray)

    merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray, array)


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 32, 9]
    merge_sort(nums_list)
    print(nums_list)
