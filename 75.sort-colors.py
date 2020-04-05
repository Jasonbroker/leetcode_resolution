#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (45.00%)
# Likes:    2665
# Dislikes: 198
# Total Accepted:    427.2K
# Total Submissions: 949.1K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 元素比较少时可以使用计数排序, 思路为三路快排partition简化版
        one = -1
        two = len(nums)
        index = 0
        while index < two :
            val = nums[index]
            if val == 0:
                one += 1
                nums[one], nums[index] = nums[index], nums[one]
                index += 1
            elif val == 1:
                index += 1
            else:
                two -= 1
                nums[two], nums[index] = nums[index], nums[two]
        
# @lc code=end

