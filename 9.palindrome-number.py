#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (47.06%)
# Likes:    2047
# Dislikes: 1496
# Total Accepted:    844.6K
# Total Submissions: 1.8M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        unit = 0  ## 代表的是索引数, 小心等号，第一次提交没写！导致wrong answer
        while x / 10**(unit + 1) >= 1:
            unit += 1
        l, r = unit, 0 # 对应的值是 10**unit
        while l > r:
            ld = int(x%(10**(l+1))/(10**l))
            rd = int(x%(10**(r+1))/(10**r))
            if ld != rd:
                return False
            else:
                l -= 1
                r += 1
        return True

        
# @lc code=end

