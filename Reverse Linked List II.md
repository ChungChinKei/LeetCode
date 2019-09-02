```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next: return head
        if m < 1 or m >= n : return head
        
        pre, curr = None, head
        
        for i in range(m-1):
            pre, curr = curr, curr.next
        
        start, end = pre, curr
        pre = None
        for i in range(n-m+1):
            curr.next, curr, pre = pre, curr.next, curr
            
        end.next = curr
        
        if m != 1:
            start.next = pre
            return head
        else:
            return pre
```
