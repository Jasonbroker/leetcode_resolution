#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (51.35%)
# Likes:    366
# Dislikes: 607
# Total Accepted:    64.8K
# Total Submissions: 126.2K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for point in points:
            map = collections.defaultdict(int)
            for point2 in points:
                if point is not point2:
                    map[self.distance(point, point2)] += 1
            # print(map)
            for val in map.values():
                if val >= 2:
                    res += val * (val - 1)
        return res            
        
    def distance(self, point1: List[int], point2: List[int]) -> int:
        return (point1[0] - point2[0]) ** 2  + (point1[1] - point2[1]) ** 2
# @lc code=end

