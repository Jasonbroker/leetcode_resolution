#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (50.68%)
# Likes:    1579
# Dislikes: 1935
# Total Accepted:    422.9K
# Total Submissions: 830.4K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        for num in nums:
            sum1 += num
        
        sum2 = (1 + n) * n // 2
        return sum2 - sum1
# @lc code=end

