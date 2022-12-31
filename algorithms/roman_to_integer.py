class Solution:

    def romanToInt(self, s: str) -> int:
        # Dictionary of roman numerals
        roman_dict = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
            }
        # Get the length of the given string
        n = len(s)
        # This variable will store result 
        # and is initiated with the last roman numeral
        num = roman_dict[s[n - 1]]
        # Loop through each character from right to left
        for i in range(n - 2, -1, -1):
            # Check if the character to the right of the 
            # current character is bigger or smaller
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                num += roman_dict[s[i]]
            else:
                num -= roman_dict[s[i]]
        return num

s = Solution().romanToInt("XIVI")
print(s)
