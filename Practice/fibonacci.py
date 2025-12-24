# Using Loop
first_no = 0
second_no = 1
n = int(input("Enter the number of terms: "))
print("Fibonacci Sequence using Loop:")
for i in range(n):
    print(first_no, end=' ')
    next_no = first_no + second_no
    first_no = second_no
    second_no = next_no

# Time Complexity: O(n)
# Space Complexity: O(1)

# Using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
n = int(input("\nEnter the number of terms: "))
print("Fibonacci Sequence using Recursion:")
fib_sequence = fibonacci_recursive(n)
print(' '.join(map(str, fib_sequence)))

# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack

# Using Dynamic Programming
def fibonacci_dynamic(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq[:n]

n = int(input("\nEnter the number of terms: "))
print("Fibonacci Sequence using Dynamic Programming:")
fib_sequence = fibonacci_dynamic(n)
print(' '.join(map(str, fib_sequence)))
# Time Complexity: O(n)
# Space Complexity: O(n)
