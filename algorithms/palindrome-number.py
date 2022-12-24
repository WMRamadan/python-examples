# Complexity is O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Get the reverse by converting to string then use string slicing
        xrev = str(x)[::-1]
        # Compare each element making sure to convert x to string
        return str(x) == xrev

# List of integers to use for testing
# tests = [121, -121, 10, 414]
# Example of output results
# The result for test 0 is True
# The result for test 1 is False
# The result for test 2 is False
# The result for test 3 is True

tests = [121, -121, 10, 414]

# Iterate over tests
for idx, test in enumerate(tests):
    result = Solution().isPalindrome(x=test)
    print(f"The result for test {idx} is {result}")
