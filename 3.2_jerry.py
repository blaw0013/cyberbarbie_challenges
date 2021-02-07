# Create a new list called is_Jerry, in which an entry at position i is True 
# if the entry in names at position i equals "Jerry".
# The entry should be False otherwise.

names = ['Alice', 'Brian', 'Catherine','David','Elijah','Frances', 'Jerry']
is_Jerry = ['True' if x == 'Jerry' else 'False' for x in names]
# is_Jerry = [name == "Jerry" for name in names]
print(is_Jerry)

# cyberbarbie did more elegantly as follows; actually -- gives a boolean result instead of a text string
# is_Jerry = [name == "Jerry" for name in names]
