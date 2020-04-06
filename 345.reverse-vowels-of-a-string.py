#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (43.27%)
# Likes:    566
# Dislikes: 1009
# Total Accepted:    201.3K
# Total Submissions: 465K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # aeiou
        l, r = 0, len(s) - 1
        strlist = list(s)
        mset = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while l < r:
            if s[l] not in mset:
                l += 1
                continue
            if s[r] not in mset:
                r -= 1
                continue
            strlist[l], strlist[r] = strlist[r], strlist[l]
            l += 1
            r -= 1
        return ''.join(strlist)  


# @lc code=end

