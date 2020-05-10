#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (55.71%)
# Likes:    1316
# Dislikes: 134
# Total Accepted:    527K
# Total Submissions: 942.1K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        l = [0] * 26
        baseline = ord('a')
        for v in s:
            index = ord(v) - baseline
            l[index] += 1
        for v in t:
            index = ord(v) - baseline
            l[index] -= 1

        for v in l:
            if v != 0: return False
        return True
        
# @lc code=end

