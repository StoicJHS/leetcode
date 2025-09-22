# *****************************************
# 1. Two Sum
# *****************************************

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
# 사고의 흐름

# python 같은 경우, enumerate와 같은 인덱스와 값을 동시에 다룰 수 있는 편리한 기능이 있다.
# 포인트는 타겟에서 내용물 하나를 골라 빼는 것
# 남은 요소가 리스트 안에 존재한다면 그 인덱스를 리턴하는 식으로 해서 최종적으로 2개의 인덱스 리스트를 만들 수 있다.

# -------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[num] = i
        return []

# 2 ms | Beats 52.87%
# 19.07 MB | Beats 23.67%
