# Create a new list named first_only that contains the
# first element in each sub-list of nested_lists.

nested_lists = [[1,2,3],[4,5,6],[3,1,-3],[2,4],[0,3,6,9,12,15]]
first_only = [item[0] for item in nested_lists]
print(first_only)

# "item" can be any variable name, such as "elem", "ele", or "x"


# cyberbarbie's code seems focused on two-element sub-lists
# first_only = [item1 for (item1, item2) in nested_lists]