from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        l = len(numbers) - 1
        while i != l:
            print(f"{numbers[i]} + {numbers[l]}")
            sum = numbers[i] + numbers[l]
            if sum > target:
                l -= 1
            elif sum < target:
                i +=1
            else:
                return [i + 1, l + 1]

s = Solution().twoSum(numbers=[2,7,11,15], target=9)
s2 = Solution().twoSum(numbers=[2,3,4], target=6)
s3 = Solution().twoSum(numbers=[-1,0], target=-1)
print(s)
print(s2)
print(s3)