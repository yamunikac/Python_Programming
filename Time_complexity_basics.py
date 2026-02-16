"""
TIME COMPLEXITY (Big-O Notation) – BASIC EXAMPLES
"""


# -----------------------------
# 1️⃣ O(1) – Constant Time
# -----------------------------

def get_first_element(arr):
    return arr[0]

# Always takes same time regardless of input size


# -----------------------------
# 2️⃣ O(n) – Linear Time
# -----------------------------

def print_all_elements(arr):
    for element in arr:
        print(element)

# Time increases as input size increases


# -----------------------------
# 3️⃣ O(n^2) – Quadratic Time
# -----------------------------

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Nested loops → slower growth


# -----------------------------
# 4️⃣ O(log n) – Logarithmic Time
# -----------------------------

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example
numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 7))

#Output
#3
