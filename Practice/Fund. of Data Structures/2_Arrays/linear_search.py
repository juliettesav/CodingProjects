#Linear Search 

list = [8, 5, 0, 3, 9, 7]
item = 7

def search(item, listy):
    for element in listy: 
        if element == item: 
            return True
        return False

print(search(item, list))

item_ind = list.index(item)

print(item_ind)