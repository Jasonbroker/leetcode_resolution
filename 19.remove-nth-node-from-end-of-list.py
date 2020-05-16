#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.89%)
# Likes:    2964
# Dislikes: 218
# Total Accepted:    582.6K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0 or not head: return head
        dummy_head = ListNode(0, head)
        target  = dummy_head
        cur = head
        for i in range(n):
            cur = cur.next
        
        while cur:
            cur = cur.next
            target = target.next
        
        target.next = target.next.next
        
        return dummy_head.next
# @lc code=end

