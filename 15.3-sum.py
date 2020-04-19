#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.93%)
# Likes:    6076
# Dislikes: 736
# Total Accepted:    830K
# Total Submissions: 3.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#

# https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
from typing import List

# @lc code=start

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3: return []
        # 先对数组进行排序确定
        nums.sort()
        res = []
        for i in range(length - 2):
            v = nums[i]
            if v > 0: break
            if i > 0 and nums[i-1] == v: continue

            l = i + 1
            r = length - 1 # last num

            while l < r:
                sum = v + nums[l] + nums[r]
                if sum > 0: # 说明r太大了
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 避免重复数字
                    while l < r:
                        if nums[r] == nums[r+1]:
                            r -= 1
                        else: break
                    while l < r:
                        if nums[l] == nums[l - 1]:
                            l += 1
                        else: break

        return res
                    
# @lc code=end


if __name__ == '__main__':
    print(Solution.threeSum('', [-1,0,1,2,-1,-4]))

