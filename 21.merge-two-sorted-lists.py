#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.98%)
# Likes:    3650
# Dislikes: 541
# Total Accepted:    910K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur_1 = l1
        cur_2 = l2
        cur = head
        while cur_1 and cur_2:
            if cur_1.val < cur_2.val:
                cur.next = cur_1
                cur_1 = cur_1.next
                cur = cur.next
            else:
                cur.next = cur_2
                cur_2 = cur_2.next
                cur = cur.next
        if cur_1:
            cur.next = cur_1
        if cur_2:
            cur.next = cur_2
        return head.next


        
# @lc code=end

