def quickSort(nums):
    if len(nums) < 2:
        return nums
    
    mid = nums[len(nums)//2]
    left, right = [], []
    nums.remove(mid)
    for num in nums:
        if num >= mid:
            right.append(num)
        else:
            left.append(num)
    
    return quickSort(left) + [mid] + quickSort(right)

if __name__ == "__main__":
    nums = [1,2,9,9,4,5,6,6,3,9,4]
    print(quickSort(nums))
