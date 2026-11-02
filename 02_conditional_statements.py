"""
Module 02: Conditional Statements
Contains 5 programs ranging from simple to advanced branching:
1. Simple if-else check (Even / Odd)
2. if-elif-else grading ladder
3. Nested if statements (Leap year calculation)
4. Ternary conditional expressions
5. Match-case pattern matching (Python 3.10+)
"""

# Program 1: Simple If-Else (Even/Odd)
def program_1_even_odd(number: int) -> str:
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Program 2: if-elif-else Ladder (Grade Assignment)
def program_2_grade_ladder(score: int) -> str:
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    return f"Score {score} -> Grade {grade}"

# Program 3: Nested Conditions (Leap Year)
def program_3_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# Program 4: Ternary Conditional Expression
def program_4_ternary_max(a: int, b: int) -> int:
    max_val = a if a > b else b
    return max_val

# Program 5: Match-Case Pattern Matching
def program_5_match_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK (Success)"
        case 201:
            return "Created (Resource generated)"
        case 400:
            return "Bad Request (Client error)"
        case 404:
            return "Not Found (Missing resource)"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status code: {status_code}"

if __name__ == "__main__":
    print("=== Module 02: Conditional Statements ===")
    print("[P1]", program_1_even_odd(28))
    print("[P2]", program_2_grade_ladder(85))
    print("[P3] Year 2024 is leap?", program_3_leap_year(2024))
    print("[P4] Max of 10 and 25:", program_4_ternary_max(10, 25))
    print("[P5] HTTP 404:", program_5_match_status(404))
