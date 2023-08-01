# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

print("####################################################")
print("################### Lists ##########################")
print("####################################################")

#1 
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])

#2
names[0] = "Alex"
print(names)

#3 
names.append("Kalooli")
print(names)

#4 
names.insert(2, "Bathel")
print(names)

#5
del names[3]
print(names)

#6
print(names[-1])

#7
items = [10, 20, 30, 40, 50, 60, 70]
print(items[2:5])

#8
countries = ["USA", "Canada", "Germany", "Australia", "Japan"]
countries_copy = countries.copy()
print(countries_copy)

#9
countries = ["USA", "Canada", "Germany", "Australia", "Japan"]
for country in countries:
    print(country)

#10
animals = ["Dog", "Cat", "Bear", "Wolf", "Fox"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)

#11
for anim in animals:
    if 'a' in anim.lower():
        print(anim)

#12
first_names = ["Kalooli", "Mawagali", "Katende"]
second_names = ["Lwanga", "Noah", "Density"]
full_names = [first + " " + second for first, second in zip(first_names, second_names)]
print(full_names)


print("####################################################")
print("################### Tuples #########################")
print("####################################################")

#1
x = ("samsung", "iphone", "tecno", "redmi")
fav = x[0]
print(fav)

#2
print(x[-2])

#3
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

#4
x = x + ("Huawei",)
print(x)

#5
for phone in x:
    print(phone)

#6
x = x[1:]
print(x)

#7
ug_cities = tuple(["Kampala", "Mbarara", "Jinja", "Gulu"])
print(ug_cities)

#8
phone1, phone2, phone3, phone4 = x
print(phone1), print(phone2), print(phone3), print(phone4)

#9
print(ug_cities[1:4])

#10
first_names = ["Kalooli", "Mawagali", "Katende"]
second_names = ["Lwanga", "Noah", "Density"]
full_names = first_names + second_names
print(full_names)

#11
colors = ("red", "green", "blue")
multi = colors * 3
print(multi)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)


print("####################################################")
print("################### Sets ###########################")
print("####################################################")

#1
bevs = set(["coffee", "milk", "juice"])
print(bevs)

#2
bevs.add("water")
bevs.add("soda")
print(bevs)

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave in set.")
else:
    print("Microwave not in set.")

#4
mySet.remove("kettle")
print(mySet)

#5
for item in mySet:
    print(item)

#6
newSet = {1, 2, 3, 4}
myList = [5, 6]
newSet.update(myList)
print(mySet)

#7
ages = {25, 30, 35}
first_names = {"Kalooli", "Lwanga", "Noah"}
joined_set = ages.union(first_names)
print(joined_set)


print("####################################################")
print("################### Strings ########################")
print("####################################################")

#1
my_int = 10
my_str = "Hello"
combined = str(my_int) + my_str
print(combined)

#2
txt = "      Hello,       Uganda!       "
newTxt = txt.replace(" ", "")
print(newTxt)

#3
newTxtUpper = newTxt.upper()
print(newTxtUpper)

#4
txtReplace = newTxtUpper.replace('U', 'V')
print(txtReplace)

#5
y = "I am proudly Ugandan"
myChars = y[1:4]
print(myChars)

#6
x = 'All "Data Scientists" are cool!'
print(x)


print("####################################################")
print("################### Dictionaries ###################")
print("####################################################")

#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

#2
Shoes["brand"] = "Adidas"
print(Shoes)

#3
Shoes["type"] = "sneakers"
print(Shoes)

#4
keys_list = list(Shoes.keys())
print(keys_list)

#5
values_list = list(Shoes.values())
print(values_list)

#6
if "size" in Shoes:
    print("The key 'size' exists in dictionary.")
else:
    print("The key 'size' does not exist in dictionary.")

#7
for key, value in Shoes.items():
    print(key, value)

#8
del Shoes["color"]
print(Shoes)

#9
Shoes.clear()
print(Shoes)

#10
myDict = {"1": "one", "2": "two"}
copy_dict = myDict.copy()
print(copy_dict)

#11
nested_dict = {
    "dict1": {"innerDict_key1": "innerDict_value1"},
    "dict2": {"innerDict_key2": "innerDict_value2"}
}
for key, value in nested_dict.items():
    print(key, value)