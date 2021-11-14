# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bst import BinarySearchTree


entries_by_name = {

}

entries_by_number = {

}


entries = int(input("Please enter an integer for the number of entries to add to the phonebook\n"))

for i in range(entries):
    name = input(f'Enter name {i + 1}\n')
    number = input(f'Enter phone number {i + 1} \n')
    address = input(f'Enter address {i + 1}\n')
    entries_by_name[f'{name}'] = number, address
    entries_by_number[f'{number}'] = name, address


a = [name for name in entries_by_name.items()]
b = [name for name in entries_by_number.items()]
name_tree = BinarySearchTree()
number_tree = BinarySearchTree()


for i in range(len(a)):
    name_tree.put(a[i][0], [a[i][1][0], a[i][1][1]])
    number_tree.put(b[i][0], [b[i][1][0], b[i][1][1]])


def search(key):
    try:
        if key is not None and key in entries_by_name.keys():
            print(f'Number: {name_tree[key][0]}\nAddress: {name_tree[key][1]}\n')
        elif key is not None:
            print(f'Name: {number_tree[key][0]}\nAddress: {number_tree[key][1]}\n')
    except TypeError:
        print("Name/number not found in phonebook. Please check the input and try again\n")


key = input("Please enter the exact name or number you would like to search for in the phonebook\n"
            "Otherwise, enter 'quit' to exit the program\n")

while key != "quit":
    key = input("Please enter the exact name or number you would like to search for in the phonebook\n"
                "Otherwise, enter 'quit' to exit the program\n")
    if key != "quit":
        search(key)
