"""
Module 15: Regular Expressions (Regex)
Contains 5 programs ranging from pattern searches to text transformations:
1. Pattern searching and span matching with re.search
2. Extracting all matching occurrences with re.findall
3. Email address format validation pattern
4. Phone number format extractor and normalizer
5. Text sanitization and credential masking with re.sub
"""

import re

# Program 1: re.search Pattern Matching
def program_1_search_pattern(text: str) -> dict:
    match = re.search(r"CVE-\d{4}-\d+", text)
    if match:
        return {"matched": match.group(0), "start": match.start(), "end": match.end()}
    return {"matched": None}

# Program 2: re.findall Token Extraction
def program_2_find_all_numbers(text: str) -> list:
    numbers = re.findall(r"\b\d+\b", text)
    return [int(n) for n in numbers]

# Program 3: Email Address Validator
def program_3_validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))

# Program 4: Phone Number Extractor & Cleaner
def program_4_extract_phones(text: str) -> list:
    # Matches patterns like (123) 456-7890 or 123-456-7890
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    matches = re.findall(pattern, text)
    # Normalize to digits only
    cleaned = [re.sub(r"\D", "", m) for m in matches]
    return cleaned

# Program 5: Redacting Sensitive Credentials (re.sub)
def program_5_redact_secrets(log_message: str) -> str:
    # Redacts Bearer tokens or API keys
    sanitized = re.sub(r"(token=)[^\s&]+", r"\1[REDACTED]", log_message, flags=re.IGNORECASE)
    sanitized = re.sub(r"(Bearer\s+)[a-zA-Z0-9._-]+", r"\1[REDACTED_BEARER]", sanitized, flags=re.IGNORECASE)
    return sanitized

if __name__ == "__main__":
    print("=== Module 15: Regular Expressions ===")
    sample_text = "Security advisory for CVE-2026-4091 affecting 12 clusters across 4 regions."
    print("[P1]", program_1_search_pattern(sample_text))
    print("[P2] Numbers found:", program_2_find_all_numbers(sample_text))
    print("[P3] 'engineer@aegisnova.io' valid?", program_3_validate_email("engineer@aegisnova.io"))
    phone_text = "Call on 123-456-7890 or (987) 654-3210 for emergency response."
    print("[P4] Extracted normalized phones:", program_4_extract_phones(phone_text))
    log = "Request authorization: Bearer gho_99887766554433 and token=sec_12345 received."
    print("[P5] Sanitized Log:\n", program_5_redact_secrets(log))
