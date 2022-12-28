class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]


s1 = Solution().reverseWords(s="Let's reverse this text")
print(s1)