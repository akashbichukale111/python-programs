"""
Module 08: Functions & Functional Programming
Contains 5 programs ranging from basic functions to higher-order patterns:
1. Functions with type hints, docstrings, and return statements
2. Default parameters and keyword argument handling
3. Variable length arguments (*args and **kwargs)
4. Recursive algorithms (Factorial and Fibonacci)
5. Lambda functions combined with map, filter, and sorted
"""

# Program 1: Function with Type Annotations
def program_1_calculate_bill(amount: float, tax_rate: float = 0.05) -> float:
    """Calculates total bill including applicable tax rate."""
    return round(amount * (1 + tax_rate), 2)

# Program 2: Default & Keyword Arguments
def program_2_greet_user(name: str, greeting: str = "Welcome", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"

# Program 3: Variable Arguments (*args & **kwargs)
def program_3_dynamic_logger(*messages, **metadata) -> dict:
    combined_message = " ".join(str(m) for m in messages)
    return {
        "message": combined_message,
        "metadata": metadata,
        "total_args": len(messages)
    }

# Program 4: Recursion (Factorial & Fibonacci)
def program_4_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * program_4_factorial(n - 1)

# Program 5: Lambda & Higher Order Functions
def program_5_functional_tools(numbers: list) -> dict:
    # Filter evens, map square, sort by magnitude
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    doubled = list(map(lambda x: x * 2, numbers))
    sorted_desc = sorted(numbers, key=lambda x: -x)
    return {"evens": evens, "doubled": doubled, "sorted_desc": sorted_desc}

if __name__ == "__main__":
    print("=== Module 08: Functions & Lambdas ===")
    print("[P1] Bill (100 @ 18%):", program_1_calculate_bill(100.0, 0.18))
    print("[P2]", program_2_greet_user("Akash", greeting="Namaskar"))
    print("[P3]", program_3_dynamic_logger("Agent", "Patrol", "Online", severity="LOW", module="NightShift"))
    print("[P4] 6! =", program_4_factorial(6))
    print("[P5] Functional:", program_5_functional_tools([5, 2, 8, 1, 9]))
