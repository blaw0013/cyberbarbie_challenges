# Use list comprehension and the zip function to create a new list 
# named sums that sums corresponding items in lists a and b. 
# For example, the first item in the new list should be 5 from 
# adding 1 and 4 together.

list_a = [1,2,3,4,5]
list_b = [6,5,4,3,2]
list_ab = zip(list_a,list_b)
sums = [item1 + item2 for (item1, item2) in list_ab]
print(sums)


# or using my code in 4.1 and the math module – take that back, the sum(x) code orks without math module
# list_a = [1,2,3,4,5]
# list_b = [6,5,4,3,2]
# list_ab = zip(list_a,list_b)
# sums = [sum(x) for x in list_ab]
# print(sums)


# cyberbarbie includes this more elegant solution
# list_a = [1,2,3,4,5]
# list_b = [6,5,4,3,2]
# sums = [item1 + item2 for (item1, item2) in zip(list_a, list_b)]
# print(sums)