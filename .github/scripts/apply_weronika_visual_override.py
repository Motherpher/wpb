#!/usr/bin/env python3
"""Re-attach WPB profile-owned visual CSS after the centrally managed shell is synced.

Temporary compatibility shim. Remove when CareerHubZero supports first-class profile-owned
style imports/hooks without patching managed files.
"""
from pathlib import Path

layout = Path("CareerHub/site/app/layout.tsx")
visual_layers = [
    Path("CareerHub/site/personal/weronika.css"),
    Path("CareerHub/site/personal/weronika-v3.css"),
]

if not layout.exists():
    raise SystemExit(f"Missing managed layout: {layout}")
for css in visual_layers:
    if not css.exists():
        raise SystemExit(f"Missing profile visual override: {css}")

text = layout.read_text(encoding="utf-8")
anchor = "import './motor.css';"
imports = [
    "import '../personal/weronika.css';",
    "import '../personal/weronika-v3.css';",
]

if anchor not in text:
    raise SystemExit("CareerHubZero layout import anchor changed; visual override cannot be injected safely.")

missing = [line for line in imports if line not in text]
if missing:
    existing_profile_imports = [line for line in imports if line in text]
    insert_after = existing_profile_imports[-1] if existing_profile_imports else anchor
    injection = insert_after + "\n" + "\n".join(missing)
    text = text.replace(insert_after, injection, 1)
    layout.write_text(text, encoding="utf-8")
    print("Injected Weronika profile-owned visual layers:", ", ".join(missing))
else:
    print("Weronika profile-owned visual layers already attached.")
