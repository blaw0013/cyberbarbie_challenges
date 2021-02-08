# You’ve been given two lists: a list of names and a list of ages. Create 
# a new list named users that contains the string "Name: name, Age: age" 
# for each pair of elements in the original lists. 
# For example, if the 5th item in the names list is "Aiyana" and the 
# 5th item in ages is 42, then the 5th item in the new list should be
# "Name: Aiyana, Age: 42".

names = ['Alice', 'Brian', 'Catherine','David','Elijah','Frances']
ages = [11, 22, 31, 14, 56, 29]
name_age = ['Name: ' + name_x + ', Age: ' + str(age_x) for (name_x, age_x) in zip(names, ages)]
print(name_age)
