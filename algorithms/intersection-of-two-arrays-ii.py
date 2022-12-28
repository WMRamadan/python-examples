from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        i = 0
        j = 0
        intersect_list = []

        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            elif sorted_nums2[j] < sorted_nums1[i]:
                j += 1
            else:
                intersect_list.append(sorted_nums1[i])
                i += 1
                j += 1

        return intersect_list

s = Solution().intersect(nums1=[1,2,2,1], nums2=[2,2])
s2 = Solution().intersect(nums1=[4,9,5], nums2=[9,4,9,8,4])

print(s)
print(s2)
