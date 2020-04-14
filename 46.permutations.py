#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (60.96%)
# Likes:    3312
# Dislikes: 95
# Total Accepted:    545K
# Total Submissions: 891.2K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#






# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.__permute(len(nums) - 1, nums);

    def __permute(self, idx: int, nums: List[int]) -> int :
        if idx == 0:
            return [[nums[0]]]
        else:
            arr = self.__permute(idx - 1, nums)
            output = []
            val = nums[idx]
            for optionArr in arr:
                itemLength = len(optionArr)
                for x in range(itemLength):
                    tmp = optionArr[:]
                    tmp.insert(x, val)
                    output.append(tmp)
                tmp = optionArr[:]
                tmp.append(val)
                output.append(tmp)
            return output
        
# @lc code=end

