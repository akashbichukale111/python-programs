"""
Module 06: Tuples & Sets
Contains 5 programs ranging from immutability to mathematical set operations:
1. Tuple creation, indexing, and immutability demonstration
2. Tuple packing and multiple variable unpacking
3. Set operations (union, intersection, difference, symmetric diff)
4. Set comprehensions and unique item extraction
5. Frozen sets as immutable collection keys
"""

# Program 1: Tuple Immutability & Indexing
def program_1_tuple_basics() -> tuple:
    point = (10, 25, 30)
    x, y, z = point
    return f"x={x}, y={y}, z={z}, count_25={point.count(25)}"

# Program 2: Tuple Packing & Unpacking
def program_2_packing_unpacking() -> dict:
    data = ("Akash", "Developer", "India", "Python", "NextJS")
    name, role, country, *skills = data
    return {"name": name, "role": role, "country": country, "skills": skills}

# Program 3: Mathematical Set Operations
def program_3_set_operations(set_a: set, set_b: set) -> dict:
    return {
        "union": set_a | set_b,
        "intersection": set_a & set_b,
        "difference_a_b": set_a - set_b,
        "symmetric_diff": set_a ^ set_b
    }

# Program 4: Set Comprehension (Unique vowels extractor)
def program_4_unique_vowels(sentence: str) -> set:
    vowels = {char.lower() for char in sentence if char.lower() in "aeiou"}
    return vowels

# Program 5: Frozenset as Dictionary Keys
def program_5_frozenset_keys() -> dict:
    role_permissions = {
        frozenset(["read", "view"]): "Viewer",
        frozenset(["read", "write", "edit"]): "Editor",
        frozenset(["read", "write", "delete", "admin"]): "Administrator"
    }
    user_perms = frozenset(["read", "view"])
    return {"matched_role": role_permissions.get(user_perms, "Custom")}

if __name__ == "__main__":
    print("=== Module 06: Tuples & Sets ===")
    print("[P1]", program_1_tuple_basics())
    print("[P2]", program_2_packing_unpacking())
    print("[P3]", program_3_set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))
    print("[P4] Unique vowels in 'AEGISNOVA AI PLATFORM':", program_4_unique_vowels("AEGISNOVA AI PLATFORM"))
    print("[P5]", program_5_frozenset_keys())
