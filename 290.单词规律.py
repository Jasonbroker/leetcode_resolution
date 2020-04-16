#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.42%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 49.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#

# @lc code=start

# 这个解法有点笨，但是leetcode 上的解法都大同小异，都挺笨的
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        arr = str.split(' ')
        patternArr = list(pattern)
        if len(arr) != len(patternArr): return False
        dic1 = {}
        dic2 = {}
        for idx in range(len(arr)):
            val = arr[idx]
            pattern_c = patternArr[idx]
            if pattern_c not in dic1 and val not in dic2:
                dic1[pattern_c] = val
                dic2[val] = pattern_c
            else:
                if pattern_c in dic1:
                    if dic1[pattern_c] != val: return False
                if val in dic2:
                    if dic2[val] != pattern_c: return False 
        return True
                
        

# @lc code=end

