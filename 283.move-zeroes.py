#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (56.67%)
# Likes:    3296
# Dislikes: 108
# Total Accepted:    712.5K
# Total Submissions: 1.2M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0   # the place for this loop value to swap
        for idx in range(len(nums)):
            if nums[idx] != 0:
                tmp = nums[idx]
                nums[idx] = nums[zero_pos]
                nums[zero_pos] = tmp
                zero_pos+= 1
        return nums


        
# @lc code=end

