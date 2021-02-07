# Create a new list named greetings that adds "Hello, " in front of each name in the list names.

names = ['Alice', 'Brian', 'Catherine','David','Elijah','Frances']
hello = ['Hello ' + x for x in names]
print(hello)

# This prints the text Hello [name] but does not save to a new list
for x in ['Alice', 'Brian', 'Catherine','David','Elijah','Frances']:
    print('Hello ',x)
