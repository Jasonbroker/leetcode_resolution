#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (38.40%)
# Likes:    1805
# Dislikes: 3726
# Total Accepted:    515.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """                                                                                                                                                              
        backward_idx1 = m - 1
        backward_idx2 = n - 1
        put_idx = m + n - 1
        while backward_idx2 >= 0:
            if backward_idx1 == -1 || nums1[backward_idx1] <= nums2[backward_idx2]:
                nums1[put_idx] = nums2[backward_idx2]
                backward_idx2 -= 1
            else:
                nums1[put_idx] = nums1[backward_idx1]
                backward_idx1 -= 1
            put_idx -= 1
        return nums1
        
# @lc code=end

