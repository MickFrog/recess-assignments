def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

my_dict = {'a': 1, 'b': 2, 'c': 3}
check_key(my_dict, 'b')
check_key(my_dict, 'd')
