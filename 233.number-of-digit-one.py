#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (31.02%)
# Likes:    250
# Dislikes: 569
# Total Accepted:    46.7K
# Total Submissions: 150.4K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# Example:
# 
# 
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 
# 
#

# @lc code=start
class Solution:
    # 超时
    # def countDigitOne(self, n: int) -> int:
    #     count = 0
    #     for i in range(1, n + 1):
    #         bit = 0 # 代表第一位
    #         while 10 ** bit  / i <= 1:
    #             digit = (int)(( i % (10 ** (bit + 1)) ) / (10 ** bit))
    #             # print(digit)
    #             if digit == 1:
    #                 count += 1
    #             bit += 1
    #     return count
    
    def countDigitOne(self, n: int) -> int:
        
# @lc code=end

