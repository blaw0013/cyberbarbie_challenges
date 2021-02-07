# Create a new list named greater_than that contains True 
# if the first number in the sub-list is greater than the
# second number in the sub-list, and False otherwise.

nested_lists = [[1,2],[4,5],[3,1],[2,4],[0,3],[-1,3],[-1,-7]]
greater_than = [item1 > item0 for (item0, item1) in nested_lists] 
print(greater_than)

# note I used item0 and item1 because I think that is how 
# Python counts, beginning with zero