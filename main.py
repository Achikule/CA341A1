# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bst import BinarySearchTree


entries_by_name = {

}

entries_by_number = {

}


option = input("Please enter '1' to  add an entry to the phonebook by name. "
               "Otherwise, enter '2' to add an entry by number\n")
if option == "1":
    entries = int(input("Please enter an integer for the number of entries to add to the phonebook\n"))

    for i in range(entries):
        name = input(f'Enter name {i + 1}\n')
        number = input(f'Enter phone number {i + 1} \n')
        address = input(f'Enter address {i + 1}\n')
        entries_by_name[f'{name}'] = number, address

elif option == "2":
    entries = int(input("Please enter an integer for the number of entries to add to the phonebook\n"))

    for i in range(entries):
        name = input(f'Enter name {i + 1}\n')
        number = input(f'Enter phone number {i + 1} \n')
        address = input(f'Enter address {i + 1}\n')
        entries_by_number[f'{name}'] = number, address
else:
    print("Invalid option")

a = [name for name in entries_by_name.items()]
name_tree = BinarySearchTree()
number_tree = BinarySearchTree()


for i in range(len(a)):
    name_tree.put(a[i][0], [a[i][1][0], a[i][1][1]])
    number_tree.put(a[i][0], [a[i][1][0], a[i][1][1]])

key = input("Please enter the exact name or number you would like to search for in the phonebook\n")

if key in entries_by_name.keys():
    print(f'Number: {name_tree[key][0]}\n Address: {name_tree[key][1]}')
else:
    print(f'Number: {number_tree[key][0]}\n Address: {name_tree[key][1]}')
