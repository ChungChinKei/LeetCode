```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        carry = 0
        curr = ListNode(0)
        res = curr
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
                
            val += carry
            curr.next = ListNode(val%10)
            curr = curr.next
            carry = val // 10
          
        if carry:
            curr.next = ListNode(1)
        
        return res.next
```
