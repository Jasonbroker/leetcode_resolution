#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (40.27%)
# Likes:    1947
# Dislikes: 350
# Total Accepted:    253.5K
# Total Submissions: 622.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0, head)
        cur = head
        p = dummy_head
        while True:
            new_next_head = self.findNodeAfter(p, k)
            if not new_next_head: break
            p = self.reverseFrom(p, k)
        return dummy_head.next

    def reverseFrom(self, p: ListNode, k: int) -> ListNode:
        pre = p.next
        cur = pre.next
        tail = pre

        for i in range(k - 1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        p.next = pre
        tail.next = cur
        return tail

# 有k个数可用
    def findNodeAfter(self, head: ListNode, k: int) -> bool:
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1
        return cur
        
# @lc code=end

