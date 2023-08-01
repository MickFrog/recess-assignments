# Looping through a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# Nesting dictionaries
nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}

for key, nested_dict in nested_dict.items():
    print(f"Key: {key}")
    for nested_key, nested_value in nested_dict.items():
        print(f"Nested Key: {nested_key}, Nested Value: {nested_value}")
