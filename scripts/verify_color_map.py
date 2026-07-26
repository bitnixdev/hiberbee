#!/usr/bin/env python3
"""Verify docs/hiberbee-color-map.json covers all todo gaps with Hiberbee-only colors.

Exit 0 on pass, 1 on failure. Run from repo root:
  python3 scripts/verify_color_map.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def parse_scheme(path: Path):
    root = ET.fromstring(path.read_text(errors="replace"))
    colors = {
        o.get("name"): o.get("value")
        for o in root.find("colors").findall("option")
        if o.get("name")
    }
    attrs = {}
    for o in root.find("attributes").findall("option"):
        n = o.get("name")
        if not n:
            continue
        val = {}
        ve = o.find("value")
        if ve is not None:
            for v in ve.findall("option"):
                val[v.get("name")] = v.get("value")
        attrs[n] = {"base": o.get("baseAttributes"), "value": val}
    return colors, attrs


def main() -> int:
    map_path = ROOT / "docs" / "hiberbee-color-map.json"
    if not map_path.is_file():
        print(f"FAIL: missing {map_path}", file=sys.stderr)
        return 1

    data = json.loads(map_path.read_text())
    MAP = {m["key"]: m for m in data["mappings"]}
    theme = json.loads(
        (ROOT / "src/intellij/src/main/resources/themes/HiberbeeDark.theme.json").read_text()
    )
    palette = theme["colors"]

    hc, ha = parse_scheme(ROOT / "src/intellij/src/main/resources/colors/Dark.xml")
    ha = {k: v for k, v in ha.items() if not k.startswith("MARKDOWN_NAVIGATOR")}

    dracula = Path("/Volumes/repos/jasonrm/github.com/dracula/jetbrains/src/main/resources/themes/Dracula.xml")
    if not dracula.is_file():
        # Fallback: only check internal consistency of the map + palette
        dracula = None

    missing_attrs: list[str] = []
    missing_colors: list[str] = []
    partials: list[str] = []

    if dracula and dracula.is_file():
        dc, da = parse_scheme(dracula)
        colorful = dracula.with_name("DraculaColorful.xml")
        if colorful.is_file():
            _, da_c = parse_scheme(colorful)
            for k, v in da_c.items():
                if k not in da:
                    da[k] = v
        ic, ia = parse_scheme(ROOT / "Islands_Dark.icls")
        missing_attrs = sorted((set(da) | set(ia)) - set(ha))
        missing_colors = sorted((set(dc) | set(ic)) - set(hc))
        for name in sorted(set(da) | set(ia)):
            if name not in ha:
                continue
            ref_val = {}
            if name in da:
                ref_val.update(da[name]["value"])
            if name in ia:
                ref_val.update(ia[name]["value"])
            if not ref_val:
                continue
            if set(ref_val) - set(ha[name]["value"]) or not ha[name]["value"]:
                partials.append(name)

    allowed_hex: set[str] = set()
    for hexv in palette.values():
        if isinstance(hexv, str) and hexv.startswith("#"):
            h = hexv.lstrip("#").upper()
            allowed_hex.add(h)
            if len(h) == 8:
                allowed_hex.add(h[:6])
    for v in hc.values():
        if v:
            allowed_hex.add(v.upper())
    for a in ha.values():
        for vv in a["value"].values():
            if vv and re.fullmatch(r"[0-9a-fA-F]{3,8}", vv):
                allowed_hex.add(vv.upper())

    errors: list[str] = []

    if missing_attrs:
        for k in missing_attrs:
            if k not in MAP:
                errors.append(f"missing attr unmapped: {k}")
    if missing_colors:
        for k in missing_colors:
            if k not in MAP:
                errors.append(f"missing color unmapped: {k}")
    if partials:
        for k in partials:
            if k not in MAP:
                errors.append(f"partial unmapped: {k}")

    for k, m in MAP.items():
        if m["kind"] == "process":
            continue
        if m["kind"] == "baseAttributes":
            if not m.get("baseAttributes"):
                errors.append(f"{k}: baseAttributes kind missing target")
            continue
        if m["kind"] == "pin_empty":
            continue
        ex = m.get("explicit")
        if ex is None:
            errors.append(f"{k}: no explicit recommendation")
            continue
        for prop, val in ex.items():
            if isinstance(val, str) and re.fullmatch(r"[0-9a-fA-F]{3,8}", val):
                if val.upper() not in allowed_hex:
                    errors.append(f"{k}.{prop}={val} not in Hiberbee closed set")

    # Role spot-checks (Hiberbee identity)
    spot = {
        "DEFAULT_BLOCK_COMMENT": lambda m: (m.get("explicit") or {}).get("FOREGROUND", "").lower()
        == "acacac",
        "org.rust.FUNCTION": lambda m: m.get("baseAttributes") == "DEFAULT_FUNCTION_DECLARATION",
        "org.rust.MACRO": lambda m: (m.get("explicit") or {}).get("FOREGROUND", "").lower()
        == "92d923",
        "HTML_ATTRIBUTE_VALUE": lambda m: m.get("baseAttributes") == "DEFAULT_STRING",
        "FILESTATUS_RENAMED": lambda m: (m.get("explicit") or {}).get("value", "").lower()
        == "78dce8",
        "NEXT_EDIT.REMOVAL_BACKGROUND": lambda m: (m.get("explicit") or {}).get("value", "").lower()
        == "320f0f",
    }
    for key, pred in spot.items():
        m = MAP.get(key)
        if not m or not pred(m):
            errors.append(f"role spot-check failed: {key}")

    kinds = Counter(m["kind"] for m in MAP.values())
    print("hiberbee-color-map verification")
    print(f"  entries: {len(MAP)}")
    print(f"  kinds: {dict(kinds)}")
    if missing_attrs:
        print(f"  missing attrs covered: {sum(1 for k in missing_attrs if k in MAP)}/{len(missing_attrs)}")
    if missing_colors:
        print(f"  missing colors covered: {sum(1 for k in missing_colors if k in MAP)}/{len(missing_colors)}")
    if partials:
        print(f"  partials covered: {sum(1 for k in partials if k in MAP)}/{len(partials)}")
    print(f"  foreign hex violations: {sum(1 for e in errors if 'not in Hiberbee' in e)}")

    if errors:
        print(f"FAIL ({len(errors)}):")
        for e in errors[:50]:
            print(f"  - {e}")
        if len(errors) > 50:
            print(f"  ... +{len(errors) - 50} more")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
