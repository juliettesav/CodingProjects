nums = [3, 2, 4]
target = 6

x = 0

while x < len(nums): 
    y = x + 1
    while y < len(nums):
        if nums[x] + nums[y] == target:
            print(f'[{x},{y}]')
            break
        y += 1
    x += 1