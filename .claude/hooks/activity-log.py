#!/usr/bin/env python3
"""Append one line per user prompt or skill run to the active project's activity.log."""
import json, os, sys, datetime

root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
try:
    name = open(os.path.join(root, ".factory/active")).read().strip()
except OSError:
    sys.exit(0)  # no active project, nothing to log
proj = os.path.join(root, "projects", name)
if not name or not os.path.isdir(proj):
    sys.exit(0)

data = json.load(sys.stdin)
event = data.get("hook_event_name")
if event == "UserPromptSubmit":
    text = " ".join(data.get("prompt", "").split())[:120]
    line = f"prompt | {text}"
elif event == "PostToolUse":
    inp = data.get("tool_input", {})
    line = f"skill  | {inp.get('skill', '?')} {inp.get('args', '')}".rstrip()
else:
    sys.exit(0)

stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
with open(os.path.join(proj, "activity.log"), "a") as f:
    f.write(f"{stamp} | {line}\n")
