"""
Using list comprehension.
Iterates over the range of indices in reverse order.
[expression for item in iterable]
"""

my_list = [1, 2, 3, 4, 5]
print("Original List: ", my_list, "\n")

reversed_list = [my_list[i] for i in range(len(my_list) - 1, -1, -1)]
print("Reversed Using Comprehension: ", reversed_list, "\n")
