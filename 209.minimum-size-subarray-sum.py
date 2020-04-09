#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (36.95%)
# Likes:    1857
# Dislikes: 97
# Total Accepted:    237.9K
# Total Submissions: 643.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # slipper window problem
        # if len(nums) == 1 and nums[0] == s : return 1
        if len(nums) == 0: return 0
        backward, forward = 0, 0
        minResult,lastSum = 0, nums[0]
        while True:
            if backward == forward and nums[backward] == s: return 1
            if lastSum < s:
                forward += 1
                if forward < len(nums):
                    lastSum += nums[forward]
                else:
                    break
                # print("min %d" %(lastSum))
            else:
                    minResult = min(minResult, forward - backward + 1)
                lastSum -= nums[backward]
                backward += 1
                if backward >= len(nums) - 1:
                    break

        return minResult

        
# @lc code=end


