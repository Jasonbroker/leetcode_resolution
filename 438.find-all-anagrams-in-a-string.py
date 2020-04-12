#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (40.91%)
# Likes:    2366
# Dislikes: 161
# Total Accepted:    193.7K
# Total Submissions: 472.2K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#

# @lc code=start






class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # first deal with the p count as map {'ascii': count, ....}
        ori = [0]*26 # 生成26个字母长度的数组
        
        a = ord('a')
        for val in p:
            ori[ord(val) - a] += 1
        
        finder = [0]*26 # 生成26个字母长度的数组
        
        l, r = 0, 0
        result = []  # record the result
        while r < len(s):
            rv = ord(s[r]) - a
            if ori[rv] == 0: ## 原串没有这个值，只能直接跳过了
                r += 1
                l = r
                for x in range(26) : finder[x] = 0
                continue
            if r - l < len(p) - 1:
                if finder[rv] and finder[rv] >= ori[rv]: # 当前这个还没加呢，但是加了就超过，只能l增加
                    lv = ord(s[l]) - a
                    finder[lv] -= 1
                    l += 1
                else :
                    finder[rv] += 1
                    r += 1
            elif r - l == len(p) - 1:
                lv = ord(s[l]) - a
                if finder[rv] + 1 == ori[rv]:
                    result.append(l)
                    finder[lv] -= 1
                    finder[rv] += 1
                    l += 1
                    r += 1
                else:
                    finder[lv] -= 1
                    l += 1

        return result
        


# @lc code=end

