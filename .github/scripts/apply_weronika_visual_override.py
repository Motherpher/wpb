#!/usr/bin/env python3
"""Re-attach WPB profile-owned visual CSS after the centrally managed shell is synced.

Temporary compatibility shim. Remove when CareerHubZero supports first-class profile-owned
style imports/hooks without patching managed files.
"""
from pathlib import Path

layout = Path("CareerHub/site/app/layout.tsx")
css = Path("CareerHub/site/personal/weronika.css")

if not layout.exists():
    raise SystemExit(f"Missing managed layout: {layout}")
if not css.exists():
    raise SystemExit(f"Missing profile visual override: {css}")

text = layout.read_text(encoding="utf-8")
import_line = "import '../personal/weronika.css';"
anchor = "import './motor.css';"

if import_line not in text:
    if anchor not in text:
        raise SystemExit("CareerHubZero layout import anchor changed; visual override cannot be injected safely.")
    text = text.replace(anchor, anchor + "\n" + import_line, 1)
    layout.write_text(text, encoding="utf-8")
    print("Injected Weronika profile-owned visual override.")
else:
    print("Weronika profile-owned visual override already attached.")
