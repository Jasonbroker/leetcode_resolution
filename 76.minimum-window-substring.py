#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.61%)
# Likes:    3803
# Dislikes: 266
# Total Accepted:    354K
# Total Submissions: 1.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        l, r = -1, -1
        tset = set(t)
        tmap = {}
        for char in tset: tmap[char] = []
        
        lval
        length = len(s)
        tlen = len(t)
        charfind = 0
        res = ''

        minl = 0
        minr = -1
        while l == length:
            val = s[idx]
            # 找到全了，那么左边往右移动
            if charfind == tlen:
                if r - l < minr - minl:
                    minl = l
                    minr = r
                else:
            else:
                if val in tset:
                    if lval != val:
                        tmap[val].append(idx)
                        if len(tmap[val]) == 1:  # 第一次找到
                            charfind += 1
                    else:
                        l = idx
                    r += 1
                    r = Math.min(r, length - 1) # 为了不溢出
                else:
                    r += 1
# @lc code=end

