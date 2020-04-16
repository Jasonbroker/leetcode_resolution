#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (47.30%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 73K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 
# 示例 1:
# 
# 输入: s = "egg", t = "add"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "foo", t = "bar"
# 输出: false
# 
# 示例 3:
# 
# 输入: s = "paper", t = "title"
# 输出: true
# 
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache_s = {}
        cache_t = {}
        length = len(s)
        for idx in range(length):
            sv = s[idx]
            tv = t[idx]
            if sv not in cache_s and tv not in cache_t:
                cache_t[tv] = sv
                cache_s[sv] = tv
            else:
                if sv in cache_s:
                    if cache_s[sv] != tv: return False
                if tv in cache_t:
                    if cache_t[tv] != sv: return False
        return True
# @lc code=end

