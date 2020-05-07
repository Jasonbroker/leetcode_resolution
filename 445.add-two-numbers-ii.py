#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (53.24%)
# Likes:    1244
# Dislikes: 144
# Total Accepted:    143.6K
# Total Submissions: 268.8K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_stack = []
        second_stack = []

        while l1: 
            first_stack.insert(0,l1.val)
            l1 = l1.next
        while l2: 
            second_stack.insert(0, l2.val)
            l2 = l2.next
        
        len1 = len(first_stack)
        len2 = len(second_stack)
        plus = 0
        result = []
        for i in range(max(len1, len2)):
            val1 = first_stack[i] if i < len1  else 0
            val2 =  second_stack[i] if i < len2 else 0
            val = val1 + val2 + plus
            result.append(val % 10)
            plus = val // 10
        if plus: result.append(1)

        head = None
        cur = None
        for i in range(len(result) - 1, -1, -1):
            if head:
                cur.next = ListNode(result[i])
                cur = cur.next
            else:
                head = ListNode(result[i])
                cur = head
        return head
            
# @lc code=end

