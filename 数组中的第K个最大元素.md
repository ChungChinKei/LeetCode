## 快排返回[-k]
```python
class Solution:
    def quickSort(self, nums):
        if len(nums) < 2: return nums
        
        mid = nums[len(nums)//2]
        nums.remove(mid)
        
        left, right = [], []
        for i in range(len(nums)):
            if nums[i] <= mid:
                left.append(nums[i])
            else:
                right.append(nums[i])
        
        return self.quickSort(left) + [mid] + self.quickSort(right)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums) or k <= 0: return 
        
        nums = self.quickSort(nums)
        
        return nums[-k]
```
## 
