#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (37.03%)
# Likes:    757
# Dislikes: 912
# Total Accepted:    255K
# Total Submissions: 687K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length < 2 or k < 1: return False

        area = set()
        l, r = 0, 0
        while r < length:
            val = nums[r]
            if r - l < k:
                if val in area:
                    return True
            else:
                if val in area:
                    return True
                else:
                    area.remove(nums[l])
                    l += 1
            area.add(val)
            r += 1
        return False
            

        
# @lc code=end

