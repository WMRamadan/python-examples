from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums

s = Solution().rotate(nums=[1,2,3,4,5,6,7], k=3)
print(s)
