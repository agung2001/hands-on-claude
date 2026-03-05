#!/usr/bin/env python3
# PreToolUse hook (Bash) — blocks dangerous shell commands

import sys
import json

DANGEROUS_PATTERNS = [
    "rm -rf /",
    "rm -rf ~",
    "rm -rf *",
    ":(){ :|:& };:",
    "dd if=/dev/zero",
    "mkfs",
    "> /dev/sda",
    "chmod -R 777 /",
    "format c:",
    "del /f /s /q c:\\",
    "rd /s /q c:\\",
    "Remove-Item -Recurse -Force C:\\",
]

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

for pattern in DANGEROUS_PATTERNS:
    if pattern.lower() in command.lower():
        print(json.dumps({
            "decision": "block",
            "reason": f"Blocked: dangerous command detected — '{pattern}'"
        }))
        sys.exit(0)

# Allow
print(json.dumps({"decision": "approve"}))
