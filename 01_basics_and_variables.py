"""
Module 01: Python Basics & Variables
Contains 5 programs ranging from simple to advanced basic concepts:
1. Hello World and basic output formatting
2. Dynamic typing and basic data types
3. Type casting and user input simulation
4. Arithmetic, comparison, and logical operators
5. Bitwise operations and binary representations
"""

# Program 1: Hello World & Formatted Printing
def program_1_hello_world():
    name = "Python Explorer"
    version = 3.12
    print(f"[P1] Hello, {name}! Running Python {version}")

# Program 2: Dynamic Typing & Core Types
def program_2_data_types():
    int_val = 42
    float_val = 3.14159
    str_val = "AEGISNOVA"
    bool_val = True
    none_val = None
    print(f"[P2] Types: int={type(int_val).__name__}, float={type(float_val).__name__}, "
          f"str={type(str_val).__name__}, bool={type(bool_val).__name__}, none={type(none_val).__name__}")

# Program 3: Type Casting & Conversion
def program_3_type_casting():
    raw_str = "150"
    as_int = int(raw_str)
    as_float = float(raw_str)
    as_bool = bool(as_int)
    print(f"[P3] Casting '{raw_str}': int={as_int}, float={as_float:.2f}, bool={as_bool}")

# Program 4: Arithmetic and Comparison Operators
def program_4_operators():
    a, b = 17, 5
    results = {
        "addition": a + b,
        "floor_division": a // b,
        "modulo": a % b,
        "power": a ** 2,
        "is_greater": a > b
    }
    print(f"[P4] a={a}, b={b} -> {results}")

# Program 5: Bitwise Operations & Binary Representation
def program_5_bitwise_ops():
    x, y = 12, 10  # 12 = 1100, 10 = 1010
    and_op = x & y
    or_op = x | y
    xor_op = x ^ y
    shift_op = x << 1
    print(f"[P5] Bitwise: {x} & {y} = {and_op} (bin: {bin(and_op)}), {x} ^ {y} = {xor_op}, {x}<<1 = {shift_op}")

if __name__ == "__main__":
    print("=== Module 01: Basics & Variables ===")
    program_1_hello_world()
    program_2_data_types()
    program_3_type_casting()
    program_4_operators()
    program_5_bitwise_ops()
