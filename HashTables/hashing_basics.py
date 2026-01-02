"""
Docstring for HashTables.hashing_basics

This module demonstrates the basic concept of hashing by implementing a simple hash function.
Hash Function : A function that takes an input (or 'key') and returns a fixed-size
string of bytes. The output is typically a 'hash code' that represents the input data.
To implement a basic hash function in a programming language, we need:
1. An input value (string) to be hashed.
2. A method to convert each character in the string to its corresponding ASCII value.
3. A way to combine these ASCII values to produce a single hash code.


"""

my_hash_list = [[] for _ in range(10)]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

lst_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]

for name in lst_names:
    index = hash_function(name)
    my_hash_list[index].append(name)

n1 = input("Enter a name to search: ")
index1 = hash_function(n1)
if n1 in my_hash_list[index1]:
    print(f"{n1} found in hash table at index {index1}.")
else:
    print(f"{n1} not found in hash table.")
    
# Time Complexity: O(1) for average case insertion and search operations.
# Space Complexity: O(n) where n is the number of elements stored in the hash table