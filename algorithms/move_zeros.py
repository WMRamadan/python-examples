from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                length -=1
            else:
                i +=1
        return nums

s = Solution().moveZeroes(nums=[0,1,0,3,12])
s2 = Solution().moveZeroes(nums=[0,0,1])
print(s)
print(s2)
