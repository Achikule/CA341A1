#!usr/bin/env python3

from bst import BinarySearchTree

# Using built-in dictionaries to store name/number as keys and other two attribute as values
entries_by_name = {

}

entries_by_number = {

}


def search(key):
    try:
        if key is not None and key in entries_by_name.keys():  # indexing works here since tree has special attribute
            print(f'Number: {name_tree[key][0]}\nAddress: {name_tree[key][1]}\n')  # __getitem__ defined
        elif key is not None:
            print(f'Name: {number_tree[key][0]}\nAddress: {number_tree[key][1]}\n')
    except TypeError:  # an item not existing results in a TypeError, which is handled by this clause
        print("Name/number not found in phonebook. Please check the input and try again\n")


entries = int(input("Please enter an integer for the number of entries to add to the phonebook\n"))
# asking user for number of entries to add beforehand

for i in range(entries):  # getting required attributes for dictionary
    name = input(f'Enter name {i + 1}\n')
    number = input(f'Enter phone number {i + 1} \n')
    address = input(f'Enter address {i + 1}\n')
    entries_by_name[f'{name}'] = number, address
    entries_by_number[f'{number}'] = name, address

a = [name for name in entries_by_name.items()]  # creating a list from dicts for definite order
b = [name for name in entries_by_number.items()]
name_tree = BinarySearchTree()  # creating tree objects, one for searching by name, other by number
number_tree = BinarySearchTree()

for i in range(len(a)):  # adding keys and values to tree
    name_tree.insert(a[i][0], [a[i][1][0], a[i][1][1]])
    number_tree.insert(b[i][0], [b[i][1][0], b[i][1][1]])

key = input("Please enter the exact name or number you would like to search for in the phonebook\n"
            "Otherwise, enter 'quit' to exit the program\n")

while key != "quit":
    if key != "quit":
        search(key)  # calling function to print values associated with keys
    key = input("Please enter the exact name or number you would like to search for in the phonebook\n"
                "Otherwise, enter 'quit' to exit the program\n")
