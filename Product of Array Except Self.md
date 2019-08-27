```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return[]
        
        left, right = 1, 1
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
            
            res[len(nums)-1-i] *= right
            right *= nums[len(nums)-1-i]
        
        return res
```
