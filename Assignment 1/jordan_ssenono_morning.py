# Ssenono Jordan Michael 
# 21/U/1013 
# 2100701013

# Lists are ordered, mutable collections of elements
# Creating a list
fruits = ['apple', 'banana', 'orange']
print(fruits)

# Adding elements to a list
fruits.append('grape')
fruits.insert(1, 'kiwi')
print(fruits) 


# Tuples are ordered, immutable collections of elements
# Creating a tuple
numbers = (1, 2, 3)
print(numbers)

# Appending tuples
numbers += (4, 5)
print(numbers)

# Set is an unordered collection of unique elements.
# Create a set
my_set = {1, 2, 3, 4, 5}

# Print the length of the set
print("Length of the set:", len(my_set))

# Print the data type of the set
print("Data type of the set:", type(my_set))

# Loop through items in the set and print them
print("Items in the set:")
for item in my_set:
    print(item)

# Add items to the set
my_set.add(6)
my_set.add(7)

# Add two sets together
other_set = {8, 9, 10}
merged_set = my_set.union(other_set)

# Print the merged set
print("Merged set:", merged_set)
