# Create a new list called greater_than_two, in which an entry at
# position i is True if the entry in nums at position i is greater than 2.

nums = [1, 2, 3, 4, 6, 9, 13, 17, 41]
greater_than_two = [x > 2 for x in nums]
print(greater_than_two)
