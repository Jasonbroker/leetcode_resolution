#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (40.21%)
# Likes:    1098
# Dislikes: 277
# Total Accepted:    204K
# Total Submissions: 505.4K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 思路 双指针链表
        cur = head
        small_head = None
        small_tail = None
        big_head = None
        big_tail = None
        pre = None
        while cur:
            if cur.val < x:
                if small_head == None:
                    small_head = cur
                else:
                    small_tail.next = cur
                small_tail = cur
            else:
                if big_head == None:
                    big_head = cur
                else:
                    big_tail.next = cur
                big_tail = cur   
            cur = cur.next

        if small_head:
            small_tail.next = big_head
            # 如果重置会出现最后一个元素的next没变nil的问题，其实根本原因是需要每次只把tail更新到cur，
            # 但是没管他的next指向，因为前后都连起来了
            # 只有最后一个元素受影响
            if big_tail: big_tail.next = None
            return small_head
        else:
            return head
# @lc code=end

