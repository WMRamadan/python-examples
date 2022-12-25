from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, i in enumerate(nums):
            if target < i:
                return idx
            elif i == target:
                return idx
            elif target < i and target > nums[idx - 1]:
                return idx
            elif target > i and idx == len(nums) - 1:
                return idx + 1

case1 = Solution().searchInsert(nums=[1,3,5,6], target=5)
case2 = Solution().searchInsert(nums=[1,3,5,6], target=2)
case3 = Solution().searchInsert(nums=[1,3,5,6], target=7)

print("Case 1: ", case1)
print("Case 2: ", case2)
print("Case 3: ", case3)
