# Create a new list named product that contains the 
# product of each sub-list of nested_lists.

import math
nested_lists = [[1,2,3],[4,5,6],[3,1,-3],[2,4],[0,3,6,9,12,15]]
product = [math.prod(x) for x in nested_lists]
print(product)

# I did it!!

#cyberbarbies code, not drawing on the math library (module?) – uses "item#"
# nested_lists = [[4, 8], [15, 16], [23, 42]]
# product = [item1 * item2 for (item1, item2) in nested_lists]