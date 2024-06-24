def twoSum(nums, target):
    num_ind = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_ind: 
            return [num_ind[complement], i]
        num_ind[num] = i 
    return []

nums = [3, 2, 4]
target = 9

print(twoSum(nums, target))