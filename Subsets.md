## 动态规划  
f(0) = [[]]  
f(1) = [[],[1]]  
f(2) = [[],[1],[2],[1,2]]  
f(3) = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  
...  
相当于f(n)在f(n-1)的基础上对每个元素加上n
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if not nums: return res
        
        for i in range(len(nums)):
            res += [x + [nums[i]] for x in res]
        
        return res
```
