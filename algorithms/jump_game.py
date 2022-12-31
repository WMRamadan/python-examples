import collections
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        reachable = 0
        while i < len(nums) and i <= reachable:
            reachable = max(i + nums[i], reachable)
            i +=1
        if i == len(nums):
            return True
        return False

s1 = Solution().canJump(nums=[2,3,1,1,4])
s2 = Solution().canJump(nums=[3,2,1,0,4])
s3 = Solution().canJump(nums=[0])
print("s1", s1)
print("s2", s2)
print("s3", s3)
