# Create a new list named greater_than that contains True or False
# depending on whether the corresponding item in list a is greater
# than the one in list b. 
# For example, if the 2nd item in list a is 3, and the 2nd item in 
# list b is 5, the 2nd item in the new list should be False.

list_a = [1,2,3,4,5]
list_b = [6,5,4,3,2]
greater_than = [item_a > item_b for (item_a, item_b) in zip(list_a, list_b)]
print(greater_than)
