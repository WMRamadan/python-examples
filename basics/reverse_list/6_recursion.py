"""
Using recursion.
The function calls itself until the list is empty.
The recursive step takes the last element of the
list and appends it to reversed_list.
"""

my_list = [1, 2, 3, 4, 5]
print("Original List: ", my_list, "\n")


def reverse_list(my_list):
    if len(my_list) == 0:
        return []
    return [my_list[-1]] + reverse_list(my_list[:-1])

reversed_list = reverse_list(my_list)
print("Reversed Using Recursion: ", reversed_list)
