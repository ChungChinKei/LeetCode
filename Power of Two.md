```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0: return False
        
        while n and n != 1:
            n /= 2
        
        return True if n == 1 else False
```

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & n-1) == 0
```
