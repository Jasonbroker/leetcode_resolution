#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.99%)
# Likes:    1382
# Dislikes: 1756
# Total Accepted:    614.6K
# Total Submissions: 1.8M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        nee = needle[0]
        left = -1
        length = len(haystack)
        i = 0
        while i < length:
            char = haystack[i]
            if char == nee:
                for j in range(len(needle)):
                    left = i
                    if i + j >= length:
                        return -1
                    else:
                        if haystack[i + j] != needle[j]:
                            i += 1
                            left = -1
                            break
                if left >= 0:
                    break
                #print(left)
            else:
                i += 1
        #print(left)
        return left

        
# @lc code=end

if __name__ == '__main__':
    Solution.strStr('', 'a', 'a')

