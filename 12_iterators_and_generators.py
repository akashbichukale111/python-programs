"""
Module 12: Iterators & Generators
Contains 5 programs ranging from custom iterators to memory-efficient streaming:
1. Custom Iterator implementing __iter__ and __next__
2. Generator function with the yield keyword
3. Generator expression for lazy memory evaluation
4. Infinite sequence generator with bounded limit
5. Chained generator streaming pipeline (Filter -> Transform -> Sum)
"""

# Program 1: Custom Iterator Protocol
class CountdownIterator:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Program 2: Generator Function with Yield
def program_2_fibonacci_gen(limit: int):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Program 3: Generator Expression
def program_3_gen_expression(max_n: int) -> int:
    # Sums squares without constructing an intermediate list in memory
    gen = (x * x for x in range(1, max_n + 1) if x % 2 != 0)
    return sum(gen)

# Program 4: Bounded Infinite Generator
def program_4_counter_stream(step: int = 5, max_steps: int = 4):
    current = 0
    steps_taken = 0
    while steps_taken < max_steps:
        yield current
        current += step
        steps_taken += 1

# Program 5: Chained Streaming Pipeline
def program_5_pipeline(raw_numbers):
    # Step 1: Filter positive numbers
    positives = (n for n in raw_numbers if n > 0)
    # Step 2: Multiply by 10
    scaled = (n * 10 for n in positives)
    # Step 3: Consume top 3 elements
    result = []
    for _ in range(3):
        try:
            result.append(next(scaled))
        except StopIteration:
            break
    return result

if __name__ == "__main__":
    print("=== Module 12: Iterators & Generators ===")
    cd = list(CountdownIterator(5))
    print("[P1] Countdown:", cd)
    fibs = list(program_2_fibonacci_gen(7))
    print("[P2] First 7 Fibonacci numbers:", fibs)
    print("[P3] Sum of odd squares up to 10:", program_3_gen_expression(10))
    print("[P4] Counter stream:", list(program_4_counter_stream(10, 4)))
    print("[P5] Chained Pipeline:", program_5_pipeline([-5, 2, -1, 4, 6, 8]))
