#Pseudo code: 

# Add index 0 and index 1 
# repeat all combinations 
# print which combo is equal to target

nums = [3,2,4] 
target = 6 

x = 0
y = 1 
round = 1

while y < len(nums):
    if nums[x] + nums[y] == target: 
        print(f"[{x}, {y}]")
    y = y + 1
    if y == 3 and x < len(nums):
        x = x + 1
        y = round + 1
        round = round + 1