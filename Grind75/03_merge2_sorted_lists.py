# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2 

    def merge(self):
        merged = sorted(self.list1 + self.list2)
        return merged 

merged_list = Solution(list1=[1, 2, 4], list2=[1, 3, 4])
print(merged_list.merge())