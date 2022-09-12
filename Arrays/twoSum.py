#https://leetcode.com/problems/two-sum/

#Brute Force Solution:
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and j != i:
                    return [i,j]
 
"""
#Optimal Solution
from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,val in enumerate(nums):
            if target - val in nums[idx + 1:]:
                    return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]
