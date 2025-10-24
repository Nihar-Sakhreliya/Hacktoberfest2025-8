# Filename: radix_sort.py

def counting_sort_by_digit(arr: list[int], exponent: int):
    """A stable sort to sort numbers based on a specific digit."""
    n = len(arr)
    output = [0] * n
    # There are 10 possible digits (0-9)
    count = [0] * 10

    # Store the count of occurrences of each digit
    for i in range(n):
        index = (arr[i] // exponent) % 10
        count[index] += 1

    # Change count[i] so that it now contains the actual
    # position of this digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exponent) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: list[int]) -> list[int]:
    """Sorts a list of non-negative integers using Radix Sort."""
    if not arr:
        return []

    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Use an exponent to extract the k-th digit (1s, 10s, 100s, etc.)
    exponent = 1
    while max_num // exponent > 0:
        counting_sort_by_digit(arr, exponent)
        exponent *= 10
    
    return arr

# --- Example Usage ---
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Original: {my_list}")
radix_sort(my_list)
print(f"Sorted:   {my_list}")
