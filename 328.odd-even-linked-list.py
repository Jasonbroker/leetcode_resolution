#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (52.77%)
# Likes:    1423
# Dislikes: 276
# Total Accepted:    218.6K
# Total Submissions: 412.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        odd_head = None
        odd_tail = None
        cur = head
        count = 1
        even_head = None
        even_tail = None
        while cur:
            # even number
            if count % 2 == 0:
                if not even_head:
                    even_head = cur
                    even_tail = even_head
                else:
                    even_tail.next = cur
                    even_tail = cur
            else:
                if not odd_head:
                    odd_head = cur
                    odd_tail = odd_head
                else:
                    odd_tail.next = cur
                    odd_tail = cur

            cur = cur.next
            count += 1

        odd_tail.next = even_head
        if even_tail: even_tail.next = None
        return odd_head

# @lc code=end

