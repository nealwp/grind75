"""
Problem:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

v1:
    - set an anchor
    - iterate through the list
    - check if the element + anchor = target
    -- if so, return the index of the anchor and the element
    -- else move the anchor to the next element in the list
    
    !! this takes too long for list of 10k!
    
v2:
    -- subtract the target from largest list item
    -- find index of the difference
    -- if exists return the two indices
    -- else compare the target to the next largest
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums, start=1):
            difference = target - nums[-idx]
            if difference in nums[:-idx]:
                index1 = nums.index(difference)
                index2 = nums.index(nums[-idx], index1+1)
                return [index1, index2]  

"""
Results:
    Runtime: 223 ms, faster than 35.49% of Python3 online submissions for Two Sum.
    Memory Usage: 15 MB, less than 76.73% of Python3 online submissions for Two Sum.
"""