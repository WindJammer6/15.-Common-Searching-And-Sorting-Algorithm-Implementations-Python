# 15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python :clipboard:
A compilation of various common Searching and Sorting Algorithm implementations in Python. 

## Thoughts on starting this compilation
Searched the internet, however I haven't found a good compilation of the various common Searching and Sorting Algorithm implementations in Python. So I decided to make one for myself, or for anyone else who wish to use this compilation. Of course, every version of an algorithm implementation is slightly different in terms of how they are implemented so if you wish to use these Searching and Sorting Algorithm Python implementations in this compilation for your personal projects you might need to have a understanding on how these implementations are created, so I strongly suggest you take a look at [codebasics' Youtube playlist on Data Structure and Algorithms](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12) that I got these Searching and Sorting Algorithm Python implementations from, or from looking at the seperate repository in my Github profile ['12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python'](https://github.com/WindJammer6/12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python)

<ins>Disclaimer</ins>: Most of these Searching and Sorting Algorithm Python implementations are done by Dhaval Patel, founder of the Youtube channel [codebasics](https://www.youtube.com/@codebasics). I did not create these Searching and Sorting Algorithm Python implementations, I merely compiled them while making some minor changes to them. 

<br>

<br>

## Table of Contents
Here are the common Searching and Sorting Algorithm Python implementations in this compilation:
+ [Big O Notation of Time and Space Complexity for the Searching and Sorting Algorithms](#bigonotation)

+ [Code Description](#codedescription)
   + [Searching Algorithms:](#searchingalgorithms)
      + [Linear Search (Searching Algorithm)](#linearsearch)
      + Binary Search (Searching Algorithm)
         + [Iterative Binary Search (Searching Algorithm)](#iterativebinarysearch)
         + [Recursive Binary Search (Searching Algorithm)](#recursivebinarysearch)

   + [Sorting Algorithms:](#sortingalgorithms)
      + [Bubble Sort (Sorting Algorithm)](#bubblesort)
      + [Quick Sort (Sorting Algorithm)](#quicksort)
      + [Insertion Sort (Sorting Algorithm)](#insertionsort)  
        -> [Shell Sort (Sorting Algorithm) (improved Insertion Sort Algorithm variation)](#shellsort)
      + [Merge Sort (Sorting Algorithm)](#mergesort)
      + [Selection Sort (Sorting Algorithm)](#selectionsort)

+ [Comparing the time complexity of the various Searching and Sorting Algorithms with the pythonic way of searching and sorting elements in a list](#comparing)
        
Notes: 
- This compilation is not exhaustive and there are obviously other more advanced types of searching and sorting Algorithms that I feel are less beginner-friendly that I did not add to this compilation (e.g. Ternary Search Algorithm and Heap Sort Algorithm (improved Selection Sort Algorithm variation))  
- In these Searching and Sorting Algorithm implementations in Python, we will only be implementing them in such a way that they only work on Array Data Structures. It is definitely possible to use these Searching and Sorting Algorithms on other Data Structures depending on the requirements and characteristics of the data. (E.g. Binary Search Algorithm can also be used on sorted Linked List Data Structures and Binary Search Tree Data Structures (with some modifications) and Quick Sort can Algorithm can be used on Linked List Data Structures (with some modifications))

<br>

<br>

## Big O Notation of Time and Space Complexity for the Searching and Sorting Algorithms<a name = "bigonotation"></a>
***For Search Algorithms:***
| **Search Algorithm** | **Space Complexity**  | **Time Complexity** |
|:------:|:------:|:------:|
|      Linear Search	      |       O(1)	     |       O(n)     |
| Iterative Binary Search  |       O(1)		  |     O(log n)   |
| Recursive Binary Search  |     O(log n) 	  |     O(log n)   |

***For Sorting Algorithms:***
| **Sorting Algorithm** | **Space Complexity**  | **Time Complexity** |
|:------:|:------:|:------:|
|       Bubble Sort	     |       O(1)		   |       O(n^2)       |
|       Quick Sort	     |      O(log n)    | 	   O(n log n)     |
|      Insertion Sort     |       O(1)		   |       O(n^2)       |
|       Shell Sort        |       O(1)       |       O(n^2)       |
|       Merge Sort	     |       O(n)	      |     O(n log n)     |
|      Selection Sort     |	    O(1)	      |       O(n^2)       |
|       Heap Sort	        |       O(1)	      |     O(n log n)     |

<br>

<br>

## Code Description <a name = "codedescription"></a>
## Searching Algorithms <a name = "searchingalgorithms"></a>
### [Linear Search (Searching Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/1.%20Linear_Search_(Searching_Algorithm).py) <a name = "linearsearch"></a>
Here are the functions available in the ['1. Linear_Search_(Searching_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/1.%20Linear_Search_(Searching_Algorithm).py) file:
+ linear_search (function)

This implementation of Linear Search Algorithm is implemented iteratively.
 
Linear Search Algorithm code:
```python
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
        
    return -1
```

<br>

<br>

### [Iterative Binary Search (Searching Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/2.%20Iterative_Binary_Search_(Searching_Algorithm).py) <a name = "iterativebinarysearch"></a>
Here are the functions available in the ['2. Iterative_Binary_Search_(Searching_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/2.%20Iterative_Binary_Search_(Searching_Algorithm).py) file:
+ iterative_binary_search (function)

This implementation of Iterative Binary Search Algorithm is implemented iteratively.
 
Iterative Binary Search Algorithm code:
```python
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
```

<br>

<br>

### [Recursive Binary Search (Searching Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/3.%20Recursive_Binary_Search_(Searching_Algorithm).py) <a name = "recursivebinarysearch"></a>
Here are the functions available in the ['3. Recursive_Binary_Search_(Searching_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/3.%20Recursive_Binary_Search_(Searching_Algorithm).py) file:
+ recursive_binary_search (function)

This implementation of Recursive Binary Search Algorithm is implemented recursively.
 
Recursive Binary Search Algorithm code:
```python
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
```

<br>

<br>

## Sorting Algorithms <a name = "sortingalgorithms"></a>
### [Bubble Sort (Sorting Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/4.%20Bubble_Sort_(Sorting_Algorithm).py) <a name = "bubblesort"></a>
Here are the functions available in the ['4. Bubble_Sort_(Sorting_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/4.%20Bubble_Sort_(Sorting_Algorithm).py) file:  
+ bubble_sort (function)

This implementation of Bubble Sort Algorithm is implemented iteratively.
 
Bubble Sort Algorithm code:
```python
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
```

<br>

<br>

### [Quick Sort (Sorting Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/5.%20Quick_Sort_(Sorting_Algorithm).py) <a name = "quicksort"></a>
Here are the functions available in the ['5. Quick_Sort_(Sorting_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/5.%20Quick_Sort_(Sorting_Algorithm).py) file:
+ swapping_two_elements_in_a_list (function)
+ hoare_partition_scheme (function)
+ lomuto_parition_scheme (function)
+ quick_sort (function)

This implementation of Quick Sort Algorithm is implemented recursively.
 
Quick Sort Algorithm code:
```python
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
```

<br>

<br>

### [Insertion Sort (Sorting Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/6.%20Insertion_Sort_(Sorting_Algorithm).py) <a name = "insertionsort"></a>
Here are the functions available in the ['6. Insertion_Sort_(Sorting_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/6.%20Insertion_Sort_(Sorting_Algorithm).py) file:
+ insertion_sort (function)

This implementation of Insertion Sort Algorithm is implemented iteratively.
 
Insertion Sort Algorithm code:
```python
def insertion_sort(number_list):

    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1
 
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j = j - 1

        number_list[j + 1] = anchor
```

<br>

<br>

### [Shell Sort (Sorting Algorithm) (improved Insertion Sort Algorithm variation)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/7.%20Shell_Sort_(Sorting_Algorithm).py) <a name = "shellsort"></a>
Here are the functions available in the ['7. Shell_Sort_(Searching_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/7.%20Shell_Sort_(Sorting_Algorithm).py) file:
+ shell_sort (function)

This implementation of Shell Sort Algorithm is implemented iteratively.
 
Shell Sort Algorithm code:
```python
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
```

<br>

<br>

### [Merge Sort (Sorting Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/8.%20Merge_Sort_(Sorting_Algorithm).py) <a name = "mergesort"></a>
Here are the functions available in the ['8. Merge_Sort_(Sorting_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/8.%20Merge_Sort_(Sorting_Algorithm).py) file:
+ merge_two_smaller_sorted_lists_to_a_merged_sorted_list (function)
+ merge_sort (function)

This implementation of Merge Sort Algorithm is implemented recursively.
 
Merge Sort Algorithm code:
```python
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

```

### [Selection Sort (Sorting Algorithm)](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/9.%20Selection_Sort_(Sorting_Algorithm).py)<a name = "selectionsort"></a>
Here are the functions available in the ['9. Selection_Sort_(Sorting_Algorithm).py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/9.%20Selection_Sort_(Sorting_Algorithm).py) file:
+ selection_sort (function)

This implementation of Selection Sort Algorithm is implemented iteratively.
 
Selection Sort Algorithm code:
```python
def selection_sort(number_list):
    for i in range(len(number_list) - 1):
        minimum_element_index = i

        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[minimum_element_index]:
                minimum_element_index = j

        if number_list[i] != number_list[minimum_element_index]:
            number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]
```

<br>

<br>

## Comparing the time complexity of the various Searching and Sorting Algorithms with the pythonic way of searching and sorting elements in a list<a name = "comparing"></a>
I created 2 additional files, ['comparing_the_time_complexity_of_the_searching_algorithms_and_searching_pythonically.py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/comparing_the_time_complexity_of_the_searching_algorithms_and_searching_pythonically.py) and ['comparing_the_time_complexity_of_the_sorting_algorithms_and_sorting_pythonically.py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/comparing_the_time_complexity_of_the_sorting_algorithms_and_sorting_pythonically.py) files that compares the time complexity of the various Searching and Sorting Algorithms with the pythonic way of searching and sorting an element in a list, via the 'time_it' decorator in the ['time_it'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/time_it.py) file, which measures the runtime of a function.

<br>

***Comparing the time complexity of the various Searching Algorithms with the pythonic way of searching an element in a list:***  
Here is the pythonic way of searching an element I created as the 'python_search_function' function:
```python
def python_search_function(number_list, number_to_find):
    if number_to_find in number_list:
        return number_list.index(number_to_find)
    else:
        return -1
```


Here is the output when I run the ['comparing_the_time_complexity_of_the_searching_algorithms_and_searching_pythonically.py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/comparing_the_time_complexity_of_the_searching_algorithms_and_searching_pythonically.py) file:
```
Testing the searching algorithms on a large unsorted List:
linear_search took 0.0 milliseconds
python_search_function took 0.0 milliseconds


Testing the searching algorithms on a large sorted List:
linear_search took 36.65637969970703 milliseconds
iterative_binary_search took 0.0 milliseconds
recursive_binary_search took 0.0 milliseconds
python_search_function took 16.092300415039062 milliseconds
```

<br>

***Comparing the time complexity of the various Sorting Algorithms with the pythonic way of sorting elements in a list:***  
Here is the pythonic way of sorting elements I created as the 'python_sort_function' function:
```python
def python_sort_function(number_list):
    number_list.sort()
```


Here is the output when I run the ['comparing_the_time_complexity_of_the_sorting_algorithms_and_sorting_pythonically.py'](https://github.com/WindJammer6/15.-Common-Searching-And-Sorting-Algorithm-Implementations-Python/blob/main/comparing_the_time_complexity_of_the_sorting_algorithms_and_sorting_pythonically.py) file:
```
Testing the sorting algorithms on a large sorted List:
bubble_sort took 18.344402313232422 milliseconds
quick_sort took 1.0194778442382812 milliseconds
insertion_sort took 9.144783020019531 milliseconds
shell_sort took 1.0161399841308594 milliseconds
merge_sort took 1.0406970977783203 milliseconds
selection_sort took 9.809255599975586 milliseconds
python_sort_function took 0.9996891021728516 milliseconds


Testing the sorting algorithms on a large unsorted List:
bubble_sort took 1.5571117401123047 milliseconds
quick_sort took 1879.601240158081 milliseconds
insertion_sort took 1.0437965393066406 milliseconds
shell_sort took 18.454313278198242 milliseconds
merge_sort took 24.295806884765625 milliseconds
selection_sort took 1949.8867988586426 milliseconds
python_sort_function took 0.0 milliseconds
```

<br>

***Analysis:***
From the output from these 2 files, you can clearly see proof of the individual Big O Notation of Time Complexity for each of the Searching and Sorting Algorithms, as well as have some insights as to how the in-built ways of searching and sorting in Python are implemented behind the scenes.
