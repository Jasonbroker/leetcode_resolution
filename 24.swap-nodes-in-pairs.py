#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (48.94%)
# Likes:    2037
# Dislikes: 161
# Total Accepted:    445.2K
# Total Submissions: 903.3K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy_head = ListNode(0, head)
        pre = dummy_head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            c = b.next

            pre.next = b
            b.next = a
            a.next = c
            pre = a

        return dummy_head.next
# @lc code=end

