from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for n in range(m, m + n):
            nums1[n] = nums2[m-n]
        nums1.sort()
        return nums1

s = Solution().merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
print(s)
