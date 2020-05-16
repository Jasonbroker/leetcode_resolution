#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.63%)
# Likes:    1124
# Dislikes: 2032
# Total Accepted:    177.4K
# Total Submissions: 350.3K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # 最初版本
    def getSum1(self, a: int, b: int) -> int:
        result = 0
        plus = 0 # 进位
        for i in range(32):
            abit = a >> i & 1
            bbit = b >> i & 1
            # 都等于1 或者 都是0 必然进位，或不进位，取决于是否abit & bbit == 1
            # 亦或的特点，相同的数亦或 == 0
            # 当前位只考虑plus
            if abit ^ bbit == 0:
                result |= plus << i
                plus = abit & bbit
            else:
            # 两数和 == 1
            # 取决于plus = 多少， 1 就进位，否则不进位
            # 当前位只考虑plus
                result |= plus ^ 1 << i
                # if plus == 1:
                  #  result |= 0 << i
                    # plus = 1 不重复赋值
                # else:
                   # result |= 1 << i
                    # plus = 0  不重复赋值
                    
        return result

    # def getSum(self, a: int, b: int) -> int:
    #     result = 0
    #     plus = 0 # 进位
    #     for i in range(32):
    #         abit = a >> i & 1
    #         bbit = b >> i & 1
    #         # 都等于1 或者 都是0 必然进位，或不进位，取决于是否abit & bbit == 1
    #         # 亦或的特点，相同的数亦或 == 0
    #         # 当前位只考虑plus
    #         nor = abit ^ bbit
    #         if nor == 0:
    #             result |= plus << i
    #             plus = abit & bbit
    #         else:
    #         # 两数和 == 1
    #         # 取决于plus = 多少， 1 就进位，否则不进位
    #         # 当前位只考虑plus
    #             result |= (plus ^ nor) << i        
    #     return result

    def getSum(self, a: int, b: int) -> int:
        # 让他们在32位内    
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)



if __name__ == "__main__":
    print(Solution.getSum(Solution, -1, 10))
# 20\n30

# @lc code=end

