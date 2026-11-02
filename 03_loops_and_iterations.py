"""
Module 03: Loops & Iterations
Contains 5 programs ranging from simple iteration to nested structures:
1. Basic for loop with range (Multiplication table)
2. While loop with accumulator (Sum of digits)
3. Break, continue, and pass statements (Prime filter)
4. For loop with else clause (Search target verification)
5. Nested loops (2D Matrix transpose print)
"""

# Program 1: For Loop with Range
def program_1_multiplication_table(n: int) -> list:
    table = [n * i for i in range(1, 11)]
    return table

# Program 2: While Loop (Sum of digits)
def program_2_sum_of_digits(num: int) -> int:
    total = 0
    temp = abs(num)
    while temp > 0:
        total += temp % 10
        temp //= 10
    return total

# Program 3: Break & Continue (Prime number check)
def program_3_is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Program 4: Loop with Else Clause (Linear Search with Fallback)
def program_4_find_with_else(items: list, target: int) -> str:
    for idx, item in enumerate(items):
        if item == target:
            return f"Found {target} at index {idx}"
    else:
        return f"{target} was NOT found in list"

# Program 5: Nested Loops (Matrix Transpose)
def program_5_transpose_matrix(matrix: list) -> list:
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

if __name__ == "__main__":
    print("=== Module 03: Loops & Iterations ===")
    print("[P1] Table of 5 (first 5):", program_1_multiplication_table(5)[:5])
    print("[P2] Sum of digits of 4839:", program_2_sum_of_digits(4839))
    print("[P3] Is 29 prime?", program_3_is_prime(29))
    print("[P4]", program_4_find_with_else([10, 20, 30], 20))
    mat = [[1, 2, 3], [4, 5, 6]]
    print("[P5] Transposed 2x3 matrix:", program_5_transpose_matrix(mat))
