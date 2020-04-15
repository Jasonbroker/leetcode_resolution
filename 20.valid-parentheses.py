#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.22%)
# Likes:    4447
# Dislikes: 206
# Total Accepted:    912.7K
# Total Submissions: 2.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for idx in range(0, len(s)):
            val = s[idx]
            if len(stack) == 0:
                stack.append(val)
            else:
                if self.isPair(stack[-1], val):
                    stack.pop()
                else:
                    stack.append(val)
        return len(stack) == 0

    def isPair(self, l: str, r: str):
        if r == ']':
            return l == '['
        elif r == ')':
            return l == '('
        elif r == '}':
            return l == '{'
        return False
        
# @lc code=end

