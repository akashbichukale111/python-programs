"""
Module 04: String Manipulation
Contains 5 programs ranging from basic slicing to pattern analysis:
1. String indexing, slicing, and reversal
2. Common string methods (strip, split, join, replace)
3. Advanced formatting with f-strings and format specifiers
4. Palindrome validator (case & punctuation insensitive)
5. Anagram checker using character frequencies
"""

# Program 1: String Slicing and Reversal
def program_1_slicing(text: str) -> dict:
    return {
        "original": text,
        "first_5": text[:5],
        "last_5": text[-5:],
        "every_second": text[::2],
        "reversed": text[::-1]
    }

# Program 2: Clean and Join String Methods
def program_2_clean_and_join(raw: str) -> str:
    cleaned = raw.strip()
    words = cleaned.split(",")
    trimmed = [w.strip().upper() for w in words]
    return " -> ".join(trimmed)

# Program 3: Format Specifiers
def program_3_formatting(name: str, score: float, total: int) -> str:
    percentage = (score / total) * 100
    return f"User: {name:<12} | Score: {score:06.2f} / {total} | Rate: {percentage:6.1f}%"

# Program 4: Robust Palindrome Check
def program_4_is_palindrome(text: str) -> bool:
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]

# Program 5: Anagram Checker
def program_5_is_anagram(s1: str, s2: str) -> bool:
    c1 = {}
    for ch in s1.lower().replace(" ", ""):
        c1[ch] = c1.get(ch, 0) + 1
    c2 = {}
    for ch in s2.lower().replace(" ", ""):
        c2[ch] = c2.get(ch, 0) + 1
    return c1 == c2

if __name__ == "__main__":
    print("=== Module 04: String Manipulation ===")
    print("[P1] Slicing 'AEGISNOVA_INTELLIGENCE':", program_1_slicing("AEGISNOVA_INTELLIGENCE")["reversed"])
    print("[P2]", program_2_clean_and_join("  apple , banana , cherry  "))
    print("[P3]", program_3_formatting("Akash", 94.5, 100))
    print("[P4] 'A man a plan a canal Panama' palindrome?", program_4_is_palindrome("A man a plan a canal Panama"))
    print("[P5] 'listen' and 'silent' anagram?", program_5_is_anagram("listen", "silent"))
