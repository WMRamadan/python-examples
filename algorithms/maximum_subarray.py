from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_n = len(nums)
 
        if len_n == 1:
            return nums[0]
        
        sums = []
        sums.append(nums[0])
        max_sum = nums[0]
        
        for i in range(1, len_n):
            sums.append(max(sums[i - 1] + nums[i], nums[i]))
            max_sum = max(max_sum, sums[i])
        
        return max_sum

s = Solution().maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
print(s)