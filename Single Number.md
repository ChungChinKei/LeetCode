```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return
        res = 0
        for num in nums:
            res ^= num
        return res
```
