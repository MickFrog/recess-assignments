# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

# Error handling
# Use defined error to handle zero age
class ZeroAgeError(Exception):
    def __init__(self, message):
        self.message = message

# Use defined error to handle under age
class UnderAgeError(Exception):
    def __init__(self, message):
        self.message = message


def get_user_age():
    try:
        age = int(input("Enter your age: "))
        if age == 0:
            raise ZeroAgeError("Age cannot be zero")
        elif age < 18:
            raise UnderAgeError("The person is underage")
        else:
            print("Age:", age)
    except ValueError:
        print("Invalid input. Please enter a valid age.")
    except ZeroAgeError as e:
        print(e.message)
    except UnderAgeError as e:
        print(e.message)

# Test the function
get_user_age()


# File handling
# File reading
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# File writing
# Beauty of python, attempts to create file if it doesn't exist
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to '{filename}'.")
    except IOError:
        print(f"Error writing to '{filename}'.")


# Using my reading and writing functions
filename = "example.txt"
content = "Ssenono Jordan Michael. The best student."

write_file(filename, content)
read_file(filename)
