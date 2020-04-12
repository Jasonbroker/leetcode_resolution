#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.74%)
# Likes:    8252
# Dislikes: 500
# Total Accepted:    1.4M
# Total Submissions: 4.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        pre, post = 0, 0
        result = -1
        length = len(s)
        mapcache = {}
        while pre < length:
            if s[pre] not in mapcache:
                mapcache[s[pre]] = pre
                # print('not', mapcache)
            else:
                result = max(result, (pre - post))
                lastshowcharidx = mapcache[s[pre]]
                post = lastshowcharidx + 1
                mapcache[s[pre]] = pre
                for k in list(mapcache):
                    if mapcache[k] < post:
                        del mapcache[k]
                # print(pre, post)
            pre += 1
            if pre == length:
               result = max(result, (pre - post)) 
        return result        
            


        
# @lc code=end