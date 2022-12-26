from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res_list = []
        for i in nums:
            res_list.append(i**2)
        res_list.sort()
        return res_list

s = Solution().sortedSquares(nums=[-4,-1,0,3,10])
print(s)
