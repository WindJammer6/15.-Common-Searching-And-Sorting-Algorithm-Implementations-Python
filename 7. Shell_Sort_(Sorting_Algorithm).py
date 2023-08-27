def shell_sort(number_list):

    gap = len(number_list)//2

    while gap > 0:

      
        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~
        
        for i in range(gap, len(number_list)):

            anchor = number_list[i]

            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor

        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        gap = gap // 2


if __name__ == '__main__':
    nums_list = [70, 3, 1, 56, 34, 12, 9, 13, 80]
    shell_sort(nums_list)
    print(nums_list)
