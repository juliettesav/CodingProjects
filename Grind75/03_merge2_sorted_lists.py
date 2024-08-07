class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2 

    def merge(self):
        merged = sorted(self.list1 + self.list2)
        return merged 

merged_list = Solution(list1=[1, 2, 4], list2=[1, 3, 4])
print(merged_list.merge())