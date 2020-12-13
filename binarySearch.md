## 二分查找
要求数组为有序排列，每次取中间的数与target进行比较，若相等，则查找成功；
若中间数较大，则在前一部分查找，反之，在后一部分查找。
其时间复杂度为O(logn)。
```python
def binarySearch(nums, target):
    if not nums:
        return False
    
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return False

if __name__ == "__main__":
    nums = range(100)
    print(binarySearch(nums,66))
```
