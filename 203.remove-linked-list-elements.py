#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (37.34%)
# Likes:    1368
# Dislikes: 81
# Total Accepted:    305.4K
# Total Submissions: 816.3K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 虚拟头结点
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next    
        return dummyHead.next
        
# @lc code=end

