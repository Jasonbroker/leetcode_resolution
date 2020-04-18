#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (59.49%)
# Likes:    1167
# Dislikes: 93
# Total Accepted:    136.9K
# Total Submissions: 230.1K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
            
        from collections import Counter
        counted = Counter(s)
        counted = counted.most_common()
        ans = ""
        for tup in counted:
            ans += tup[0] * tup[1]
        return ans

        # 用heap
        heap, cnt = [], Counter(s)
        ret = ''
        for key in cnt:
            heappush(heap, (-cnt[key], key))
        while len(heap) > 0:
            cur = heappop(heap)
            ret += cur[1] * (-cur[0])
        return ret

        ## 我的实现慢一点
        # 这样可以进行默认值赋值操作，避免每次判断key是否存在
        dic = collections.defaultdict(int)
        for v in s:
            dic[v] += 1
        # 桶排序
        #生成桶
        length = len(s)
        buckets = [[] for _ in range(length)]
        for char in dic:
            # 次数桶，放入某个元素*出现次数
            count = dic[char]
            b = buckets[count-1]
            data = char * count
            b.append(data)
        res = []
        for bucket in buckets[::-1]:
            if bucket:
                res.extend(bucket)
        return ''.join(res)
            
# @lc code=end

import collections
if __name__ == '__main__':
    Solution.frequencySort('', 'tree')



