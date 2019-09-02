## 递归
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return newhead
```
## 循环
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        
        pre = None
        while head:
            head.next, pre, head =pre, head, head.next
        
        return pre
```
