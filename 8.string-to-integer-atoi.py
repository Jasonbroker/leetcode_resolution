#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        # 这个题的关键点在边界条件，特别需要考虑
        pre = None
        res = []
        for char in str:
            if not pre and char == ' ':
                continue
            else:
                
# @lc code=end

