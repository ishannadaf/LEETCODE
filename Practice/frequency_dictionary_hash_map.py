nums = [1,2,3,4,1,1,2,5,6,4,3,2,1]

#    Brute Force Method
#    Using Hash Map (Dictionary) to count frequencies
frequency_dict = {}
for num in nums:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1
print("Frequency Dictionary:", frequency_dict)


# Time Complexity: O(n) where n is the number of elements in the list
# Space Complexity: O(k) where k is the number of unique elements in the list