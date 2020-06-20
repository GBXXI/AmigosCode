
# %% [markdown]
# In computer science, selection sort is an in-place comparison sorting <br>
# algorithm. It has an O time complexity, which makes it inefficient on large <br>
# lists, and generally performs worse than the similar insertion sort. Selection <br>
# sort is noted for its simplicity and has performance advantages over more <br>
# complicated algorithms in certain situations, particularly where auxiliary <br>
# memory is limited. The algorithm divides the input list into two parts: a <br>
# sorted sublist of items which is built up from left to right at the front of <br>
# the list and a sublist of the remaining unsorted items that occupy the rest of <br>
# the list. Initially, the sorted sublist is empty and the unsorted sublist is <br>
# the entire input list. The algorithm proceeds by finding the smallest element <br>
# in the unsorted sublist, exchanging it with the leftmost unsorted element, and <br>
# moving the sublist boundaries one element to the right.<br>
# <footer>Wikipedia</footer>

# %% [markdown]
# Data.
# %% [codecell]
data = [4, 9, 3, 6, 2]

# %% [codecell]
import copy
def p_solution(list_):
    data_f = copy.deepcopy(list_)
    
    for outer_index in range(len(data_f)-1):
        min_num = data_f[outer_index]

        for element in data_f[outer_index:]:
            if element < min_num:
                min_num = element
                inner_index = data_f.index(min_num)
        
        data_f[inner_index] = data_f[outer_index]
        data_f[outer_index] = min_num
    return data_f

# %% [codecell]
def amc_solution(list_):

    for outer_index in range(len(list_)):
        min_index = outer_index

        for inner_index in range(outer_index+1, len(list_)):
            if list_[inner_index] < list_[min_index]:
                min_index = inner_index
        list_[outer_index], list_[min_index] = list_[min_index], list_[outer_index]
    return list_
# %% [codecell]
print(p_solution(data))