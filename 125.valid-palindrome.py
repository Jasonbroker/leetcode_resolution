#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (34.54%)
# Likes:    977
# Dislikes: 2631
# Total Accepted:    516.1K
# Total Submissions: 1.5M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start


class Solution:
    lower = ord('a')
    num = ord('0')
    def isChar(self, c: int) -> bool:
        return self.lower <= c <= (self.lower + 25) or self.num <= c <= (self.num + 9)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            lchar = ord(s[l])
            if not self.isChar(lchar):
                l += 1
                continue
            rchar = ord(s[r])
            if not self.isChar(rchar):
                r -= 1
                continue
            print(lchar)
            print(rchar)
            if lchar == rchar:
                l += 1
                r -= 1
            else:
                return False
        return True


        
# @lc code=end

