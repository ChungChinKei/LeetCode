```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        
        res = ListNode(0)
        if l1.val <= l2.val:
            res = l1
            res.next = self.mergeTwoLists(l1.next,l2)
        else:
            res = l2
            res.next = self.mergeTwoLists(l1, l2.next)
        
        return res
```
