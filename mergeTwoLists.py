class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        if l1 and l2:
            
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

s = Solution()
a = ListNode(1)
b = ListNode(2)

c = ListNode(2)
d = ListNode(3)

a.next = b
c.next = d
s.mergeTwoLists(a,b)