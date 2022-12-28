from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s

s1 = Solution().reverseString(s=["h","e","l","l","o"])
print(s1)