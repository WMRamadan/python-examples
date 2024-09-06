my_list = [1, 2, 3, 4, 5]
original_list = my_list.copy()  # Store the original list
print("Original List: ", my_list, "\n")


"""
Using the reverse method
How it works: reverses the list in place.
"""
my_list.reverse()
print("Reversed Using Reverse: ", my_list, "\n")


# Reset my_list to the original
my_list = original_list.copy()


"""
Using slicing
How it works: list[start:stop:step]
"""
reversed_list = my_list[::-1]
print("Reversed Using Slicing: ", reversed_list, "\n")


"""
Using the reversed function
How it works: produces values in reverse order.
"""
reversed_list = list(reversed(my_list))
print("Reversed Using Reversed: ", reversed_list, "\n")


"""
Using a for loop
How it works: Creates empty list,
loop from the last index,
and decrese until the first index.
Each element is appeneded to the new list.
range(start, stop, step)
"""
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print("Reversed Using Loop: ", reversed_list, "\n")


"""
Using list comprehension
How it works: iterates over the range of indices in reverse order.
[expression for item in iterable]
"""
reversed_list = [my_list[i] for i in range(len(my_list) - 1, -1, -1)]
print("Reversed Using Comprehension: ", reversed_list, "\n")


"""
Using recursion
How it works: the function calls itself until the list is empty.
The recursive step takes the last element of the list and appends
it to reversed_list.
"""
def reverse_list(my_list):
    if len(my_list) == 0:
        return []
    return [my_list[-1]] + reverse_list(my_list[:-1])

reversed_list = reverse_list(my_list)
print("Reversed Using Recursion: ", reversed_list)
