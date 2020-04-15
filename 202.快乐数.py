#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (57.93%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    54.5K
# Total Submissions: 94K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到
# 1。如果 可以变为  1，那么这个数就是快乐数。
# 
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 
# 
# 
# 示例：
# 
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0: return 0
        cache = set()
        return self.__calculate(n, cache)

    def __calculate(self, n: int, cache : set) -> bool:
        res = self.calculate(n)
        if res == 1:
            return True
        else:
            if res not in cache:
                cache.add(res)
                return self.__calculate(res, cache)
            else:
                return False

    def calculate(self, n: int) -> int:
        unit = 0
        result = 0
        while (int)(n / (10 ** unit)) > 0: # 当前位
            digit = (int)(n % (10 ** (unit + 1)) / 10 ** unit)
            result += digit ** 2
            unit += 1
            # print(result)
        return result
            
# @lc code=end

