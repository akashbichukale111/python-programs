"""
Module 10: Exception Handling
Contains 5 programs ranging from basic error interception to custom hierarchies:
1. Basic try-except block catching ZeroDivisionError
2. Handling multiple specific exceptions independently
3. Full try-except-else-finally lifecycle
4. Programmatic exception raising with input validation
5. Defining and raising custom user-defined domain exceptions
"""

# Program 1: Basic Try-Except
def program_1_safe_division(a: float, b: float) -> str:
    try:
        res = a / b
        return f"Result: {res}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

# Program 2: Multiple Specific Exceptions
def program_2_parse_int_item(items: list, index: int) -> str:
    try:
        val = int(items[index])
        return f"Parsed integer: {val}"
    except IndexError:
        return f"Error: Index {index} is out of bounds (len={len(items)})"
    except ValueError:
        return f"Error: Item at index {index} cannot be parsed as int"

# Program 3: Try-Except-Else-Finally
def program_3_lifecycle(x: int) -> dict:
    events = []
    try:
        events.append("Entering try")
        reciprocal = 100 / x
        events.append(f"Calculation success: {reciprocal}")
    except ZeroDivisionError:
        events.append("Handled ZeroDivisionError")
    else:
        events.append("Executing else block (no exception)")
    finally:
        events.append("Executing finally block (cleanup)")
    return {"trace": events}

# Program 4: Raising Built-in Exceptions
def program_4_validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age value: {age}")
    return True

# Program 5: Custom Domain Exception Hierarchy
class CircuitBreakerTrippedError(Exception):
    """Raised when safety limits are exceeded in autonomous operations."""
    def __init__(self, failure_count: int, threshold: int):
        super().__init__(f"Circuit breaker tripped after {failure_count} failures (limit: {threshold})")
        self.failure_count = failure_count

def program_5_check_circuit(failures: int) -> str:
    try:
        if failures >= 3:
            raise CircuitBreakerTrippedError(failures, 3)
        return "Circuit is CLOSED (Normal operation)"
    except CircuitBreakerTrippedError as ex:
        return f"SAFETY LOCKDOWN: {ex}"

if __name__ == "__main__":
    print("=== Module 10: Exception Handling ===")
    print("[P1]", program_1_safe_division(10, 0))
    print("[P2]", program_2_parse_int_item(["42", "not_a_number"], 1))
    print("[P3]", program_3_lifecycle(25))
    try:
        program_4_validate_age(-5)
    except ValueError as e:
        print("[P4] Caught expected validation error:", e)
    print("[P5]", program_5_check_circuit(4))
