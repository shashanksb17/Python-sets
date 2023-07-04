# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def add_entry(dictionary, name, age):
    dictionary[name] = age

def update_entry(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_entry(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Main program
my_dictionary = {}

add_entry(my_dictionary, "John", 25)
print(my_dictionary)

update_entry(my_dictionary, "John", 26)
print(my_dictionary)

delete_entry(my_dictionary, "John")
print(my_dictionary)
