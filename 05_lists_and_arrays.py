"""
Module 05: Lists & Sequences
Contains 5 programs ranging from basic operations to matrix manipulation:
1. List CRUD (append, insert, remove, pop)
2. List slicing and chunking
3. List comprehensions with filters and transformations
4. Second largest number finder without sorting
5. Flattening multidimensional lists
"""

# Program 1: Basic List Operations
def program_1_list_crud():
    items = ["python", "typescript", "rust"]
    items.append("go")
    items.insert(1, "c++")
    removed = items.pop()
    return {"final_list": items, "popped_element": removed}

# Program 2: List Chunking
def program_2_chunk_list(lst: list, chunk_size: int) -> list:
    chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunks

# Program 3: List Comprehensions
def program_3_comprehensions(numbers: list) -> list:
    # Squares of even numbers
    squares = [x**2 for x in numbers if x % 2 == 0]
    return squares

# Program 4: Second Largest Finder (O(n))
def program_4_second_largest(nums: list) -> int:
    first, second = float("-inf"), float("-inf")
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return int(second) if second != float("-inf") else -1

# Program 5: Flatten Nested List
def program_5_flatten(nested: list) -> list:
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(program_5_flatten(item))
        else:
            flat.append(item)
    return flat

if __name__ == "__main__":
    print("=== Module 05: Lists & Sequences ===")
    print("[P1]", program_1_list_crud())
    print("[P2] Chunks:", program_2_chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
    print("[P3] Even squares:", program_3_comprehensions(list(range(1, 11))))
    print("[P4] Second largest in [12, 45, 2, 45, 33]:", program_4_second_largest([12, 45, 2, 45, 33]))
    print("[P5] Flattened list:", program_5_flatten([1, [2, [3, 4], 5], 6]))
