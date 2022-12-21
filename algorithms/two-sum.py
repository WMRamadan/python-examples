# Complexity of O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    # Create a dictionary to store the elements and their indices
    element_dict = {}
    # Iterate through the list of elements
    for i, num in enumerate(nums):
        # Check if the difference between the target 
        # and the current element is present in the dictionary
        if target - num in element_dict:
            # If it is, return the indices of the current element 
            # and the element from the dictionary
            return [element_dict[target - num], i]
        # If it's not, add the current element 
        # and its index to the dictionary
        element_dict[num] = i

# Test the function
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))  # [1, 2]
print(twoSum([3, 3], 6))  # [0, 1]
