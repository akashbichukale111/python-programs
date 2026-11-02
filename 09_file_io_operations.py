"""
Module 09: File I/O Operations
Contains 5 programs ranging from text writing to structured serialization:
1. Writing and reading text files safely using the 'with' context manager
2. Appending timestamped log records to a persistent file
3. Line-by-line buffered file reading for memory efficiency
4. Parsing and writing CSV tabular records
5. Serializing and deserializing JSON payloads
"""

import os
import json
import csv
import tempfile

# Program 1: Write and Read Text File
def program_1_read_write_text() -> str:
    path = os.path.join(tempfile.gettempdir(), "aegis_demo_text.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("Line 1: AEGISNOVA Autonomous Core\nLine 2: Safe AI Standard")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

# Program 2: Append Log Records
def program_2_append_log(entry: str) -> int:
    path = os.path.join(tempfile.gettempdir(), "aegis_demo_log.txt")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[LOG] {entry}\n")
    return os.path.getsize(path)

# Program 3: Buffered Line Reader
def program_3_read_lines() -> list:
    path = os.path.join(tempfile.gettempdir(), "aegis_demo_text.txt")
    lines = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                lines.append(line.strip())
    return lines

# Program 4: CSV Serialization
def program_4_csv_operations() -> list:
    path = os.path.join(tempfile.gettempdir(), "aegis_records.csv")
    data = [
        ["id", "service", "status"],
        ["1", "NightShift", "ACTIVE"],
        ["2", "CausalImpact", "PASS"]
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    read_back = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            read_back.append(row)
    return read_back

# Program 5: JSON Serialization & Parsing
def program_5_json_operations() -> dict:
    payload = {
        "project": "AEGISNOVA",
        "verified": True,
        "score": 99.4,
        "tags": ["AI", "Safety", "Governance"]
    }
    serialized = json.dumps(payload, indent=2)
    deserialized = json.loads(serialized)
    return deserialized

if __name__ == "__main__":
    print("=== Module 09: File I/O Operations ===")
    print("[P1] Text Read:\n", program_1_read_write_text())
    print("[P2] Log appended, file size:", program_2_append_log("3 AM patrol check passed"))
    print("[P3] Buffered lines:", program_3_read_lines())
    print("[P4] CSV rows parsed:", program_4_csv_operations())
    print("[P5] JSON parsed payload:", program_5_json_operations())
