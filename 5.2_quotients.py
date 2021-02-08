# Use list comprehension and the zip function to create a new list named 
# quotients that divides the elements in list b by those in list a. 
# For example, the second item in the new list should be
# 2.5 from dividing 5.0 by 2.0.

list_a = [1,2,3,4,5]
list_b = [6,5,4,3,2]
quotients = [item_b / item_a for (item_b, item_a) in zip(list_b, list_a)]
print(quotients)