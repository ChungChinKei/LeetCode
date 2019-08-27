## 快慢指针
```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return 
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        
        return 
```

## 辅助空间（复杂度大）
```python
class Solution(object):
    def detectCycle(self, head):
		if not head or not head.next: return None
		
        temp_list = []
        while head:
            if head in temp_list:
                return head
            temp_list.append(head)
            head = head.next
            
        return None
```
