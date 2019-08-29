## 哈希表
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return True
        
        return False
```
## 排序
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
```
