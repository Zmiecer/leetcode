# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def step(l, y):
            x = ListNode(l.val)
            y.next = x
            y = y.next
            l = l.next
            return [l, y]
            
        if not l1 or not l2:
            return l1 or l2
        
        x = y = ListNode(0)
            
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                l1, y = step(l1, y)
            else:
                l2, y = step(l2, y)
                
        if l1 is None:
            y.next = l2
        else:
            y.next = l1
            
        return x.next
        
