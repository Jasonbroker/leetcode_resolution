#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (37.70%)
# Likes:    2015
# Dislikes: 131
# Total Accepted:    255.5K
# Total Submissions: 675K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m == n: return head
        count = 1
        pre = None
        cur = head
        innerHead = None
        prelinkm = None
        while count <= n:
            if count == m: 
                innerHead = cur
                prelinkm = pre
                pre = cur
                cur = cur.next
            elif count < m:
                pre = cur
                cur = cur.next
            elif count > m:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next    
            if count == n:
                if prelinkm:
                    prelinkm.next = pre
                else:
                    head = pre
                innerHead.next = cur
            count += 1
        
        return head
        
# @lc code=end

