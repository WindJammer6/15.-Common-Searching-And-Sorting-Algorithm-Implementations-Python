def swapping_two_elements_in_a_list(a, b, array):
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp


def hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list):
  
    pivot_index = start_index_of_list
    pivot = number_list[pivot_index]

    start_pointer = pivot_index + 1
    end_pointer = end_index_of_list

    while start_pointer <= end_pointer:

        while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
            start_pointer += 1

        while number_list[end_pointer] > pivot:
            end_pointer -= 1

        if start_pointer < end_pointer:
            swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list)  
            
    swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)

    return end_pointer


def lomuto_partition_scheme(number_list, start_index_of_list, end_index_of_list):
  
    pivot = number_list[end_index_of_list]
    partition_index = start_index_of_list

    for i in range(start_index_of_list, end_index_of_list):
        if number_list[i] <= pivot:
            swapping_two_elements_in_a_list(i, partition_index, number_list)
            partition_index += 1

    swapping_two_elements_in_a_list(partition_index, end_index_of_list, number_list)

    return partition_index


def quick_sort(number_list, start_index_of_list, end_index_of_list):

    if start_index_of_list >= end_index_of_list:
        return

    else:
        #Just change the 'hoare_partition_scheme' function here to 'lomuto_partition_scheme' function to carry out the Quick Sort Algorithm via Lomuto Partition scheme instead
        #of via Hoare Partition scheme
        partitioning_point = hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list)
        quick_sort(number_list, start_index_of_list, partitioning_point - 1)
        quick_sort(number_list, partitioning_point + 1, end_index_of_list)


if __name__ == '__main__':
    nums_list = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(nums_list)
    print(nums_list)
