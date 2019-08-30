```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        num = x
        curr = 0
        while num:
            curr = curr * 10 + num % 10
            num //= 10
            
        return curr == x
```
