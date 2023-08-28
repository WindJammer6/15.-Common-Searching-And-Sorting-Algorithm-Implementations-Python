#This time_it decorator is used in the 'comparing_the_time_complexity_of_the_searching_algorithms_and_searching_pythonically.py' and the
#'comparing_the_time_complexity_of_the_sorting_algorithms_and_sorting_pythonically.py' files

import time

def time_it(function):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(function.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")
        return result
    
    return wrapper
