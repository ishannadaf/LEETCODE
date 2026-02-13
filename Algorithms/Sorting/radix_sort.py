"""
Docstring for Algorithms.Sorting.radix_sort
This module implements the Radix Sort algorithm to sort an array of non-negative integers in ascending order.
Radix Sort : A non-comparison based sorting algorithm that sorts numbers by processing individual digits.
To implement the Radix Sort algorithm in a programming language, we need:
1. An array with non-negative integer values to sort.
2. A function to perform counting sort based on the digit represented by the current exponent.

"""

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array:", myArray)