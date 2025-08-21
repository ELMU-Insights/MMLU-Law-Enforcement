
import json
import sys

REQUIRED_FIELDS = [
    "id",
    "question",
    "options",
    "answer",
    "category",
    "difficulty",
    "reference",
    "explanation"
]

VALID_DIFFICULTY = {"Basic", "Intermediate", "Advanced"}

def validate_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                entry = json.loads(line.strip())
            except json.JSONDecodeError as e:
                print(f"[Line {i}] ❌ Invalid JSON: {e}")
                continue

            missing = [field for field in REQUIRED_FIELDS if field not in entry]
            if missing:
                print(f"[Line {i}] ❌ Missing fields: {missing}")
                continue

            if not isinstance(entry["options"], list) or len(entry["options"]) != 4:
                print(f"[Line {i}] ❌ 'options' must be a list of 4 items.")
                continue

            if entry["difficulty"] not in VALID_DIFFICULTY:
                print(f"[Line {i}] ❌ Invalid difficulty '{entry['difficulty']}' — must be one of {VALID_DIFFICULTY}")
                continue

            print(f"[Line {i}] ✅ Passed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_submission.py <your_file.jsonl>")
    else:
        validate_jsonl(sys.argv[1])
