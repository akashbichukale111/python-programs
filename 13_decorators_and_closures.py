"""
Module 13: Decorators & Closures
Contains 5 programs ranging from basic closures to caching decorators:
1. Lexical closure maintaining state across calls
2. Function execution logging decorator
3. Parameterized decorator (repeat execution n times)
4. Execution time benchmark decorator using functools.wraps
5. In-memory memoization cache decorator for optimization
"""

import time
from functools import wraps

# Program 1: Closure (Stateful Counter)
def program_1_make_counter(start: int = 0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Program 2: Function Execution Logger Decorator
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_repr = f"{func.__name__}(args={args})"
        result = func(*args, **kwargs)
        return f"[LOG] {call_repr} => {result}"
    return wrapper

@log_execution
def add_numbers(x: int, y: int) -> int:
    return x + y

# Program 3: Parameterized Decorator (Repeat Execution)
def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(times)]
            return results
        return wrapper
    return decorator

@repeat(times=3)
def roll_die() -> int:
    import random
    return random.randint(1, 6)

# Program 4: Performance Timer Decorator
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        duration_ms = (time.perf_counter() - start) * 1000
        return res, round(duration_ms, 3)
    return wrapper

@measure_time
def compute_sum(n: int) -> int:
    return sum(range(n))

# Program 5: Memoization Cache Decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fast_fib(n: int) -> int:
    if n < 2:
        return n
    return fast_fib(n - 1) + fast_fib(n - 2)

if __name__ == "__main__":
    print("=== Module 13: Decorators & Closures ===")
    counter = program_1_make_counter(10)
    print("[P1] Counter calls:", [counter(), counter(), counter()])
    print("[P2]", add_numbers(15, 27))
    print("[P3] Repeated rolls:", roll_die())
    val, duration = compute_sum(100000)
    print(f"[P4] Sum 100k: {val} in {duration} ms")
    print("[P5] Fast Memoized Fib(30):", fast_fib(30))
