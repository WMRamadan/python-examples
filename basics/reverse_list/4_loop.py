"""
Using a for loop.
Creates empty list, loop from the last index,
and decrese until the first index.
Each element is appeneded to the new list.
range(start, stop, step)
"""

my_list = [1, 2, 3, 4, 5]
print("Original List: ", my_list, "\n")


reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print("Reversed Using Loop: ", reversed_list, "\n")
