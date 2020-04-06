#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (52.98%)
# Likes:    3151
# Dislikes: 222
# Total Accepted:    553.5K
# Total Submissions: 1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # the easiest way is sort the list then get nums[k-1]
        # O(nlogn)

        # O(n)
        pivot = 0  # choose the first one to be the pivot (like fast sort)
        min = 0
        max = len(nums) - 1
        for idx in range(min, max):
            val = nums[idx]
            pval = nums[pivot]
            if idx < pivot and val > pval:
                # left and bigger
                

        
# @lc code=end

