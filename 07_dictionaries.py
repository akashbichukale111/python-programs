"""
Module 07: Dictionaries (Key-Value Mappings)
Contains 5 programs ranging from basic lookup to nested structures:
1. Dictionary CRUD and safe access with .get() defaults
2. Iterating through keys, values, and items
3. Dictionary comprehension and key-value inversion
4. Merging dictionaries using union (|) and unpacking (**)
5. Word frequency counter across text tokens
"""

# Program 1: Dict CRUD & Safe Access
def program_1_dict_basics() -> dict:
    config = {"env": "production", "debug": False, "timeout": 30}
    config["retries"] = 3
    port = config.get("port", 8080)
    config["port"] = port
    return config

# Program 2: Dict Iteration
def program_2_dict_iteration(data: dict) -> list:
    formatted = [f"Key: {k} => Value: {v}" for k, v in data.items()]
    return formatted

# Program 3: Dict Comprehension & Inversion
def program_3_invert_dict(d: dict) -> dict:
    # Swaps keys and values
    inverted = {v: k for k, v in d.items()}
    return inverted

# Program 4: Dictionary Merging
def program_4_merge_dicts(base: dict, override: dict) -> dict:
    # Modern Python 3.9+ union operator
    merged = base | override
    return merged

# Program 5: Word Frequency Counter
def program_5_word_frequency(text: str) -> dict:
    words = text.lower().split()
    freq = {}
    for w in words:
        cleaned = "".join(c for c in w if c.isalnum())
        if cleaned:
            freq[cleaned] = freq.get(cleaned, 0) + 1
    return dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

if __name__ == "__main__":
    print("=== Module 07: Dictionaries ===")
    print("[P1] Config:", program_1_dict_basics())
    print("[P2] Items:", program_2_dict_iteration({"a": 1, "b": 2}))
    print("[P3] Inverted:", program_3_invert_dict({"status": 200, "error": 500}))
    print("[P4] Merged:", program_4_merge_dicts({"host": "localhost", "port": 3000}, {"port": 8080}))
    sample = "Python is powerful and Python is fast and expressive"
    print("[P5] Word Frequency:", program_5_word_frequency(sample))
