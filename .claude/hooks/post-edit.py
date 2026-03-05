#!/usr/bin/env python3
# PostToolUse hook (Write, Edit, NotebookEdit) — logs AI file edits

import sys
import json
import os
from datetime import datetime

data = json.load(sys.stdin)
tool_name = data.get("tool_name", "unknown")
tool_input = data.get("tool_input", {})

# Resolve file path across different edit tools
file_path = (
    tool_input.get("file_path")
    or tool_input.get("notebook_path")
    or "unknown"
)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "edits.log")

with open(log_file, "a") as f:
    f.write(f"[{timestamp}] [{tool_name}] {file_path}\n")
