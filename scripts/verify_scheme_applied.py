#!/usr/bin/env python3
"""Assert Dark.xml reflects docs/hiberbee-color-map.json (applied scheme).

  python3 scripts/verify_scheme_applied.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCHEME = ROOT / "src/intellij/src/main/resources/colors/Dark.xml"
THEME = ROOT / "src/intellij/src/main/resources/themes/HiberbeeDark.theme.json"
MAP_PATH = ROOT / "docs/hiberbee-color-map.json"

STYLE = {
    "FOREGROUND",
    "BACKGROUND",
    "FONT_TYPE",
    "EFFECT_COLOR",
    "EFFECT_TYPE",
    "ERROR_STRIPE_COLOR",
}


def load_scheme(path: Path):
    root = ET.fromstring(path.read_text())
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
            for c in ve.findall("option"):
                val[c.get("name")] = c.get("value")
        attrs[n] = {"base": o.get("baseAttributes"), "value": val}
    return colors, attrs


def main() -> int:
    data = json.loads(MAP_PATH.read_text())
    colors, attrs = load_scheme(SCHEME)
    theme = json.loads(THEME.read_text())
    errors: list[str] = []

    # Identity anchors must not regress
    anchors = {
        "DEFAULT_KEYWORD": ("FOREGROUND", "ee7762"),
        "DEFAULT_STRING": ("FOREGROUND", "ffd866"),
        "DEFAULT_FUNCTION_CALL": ("FOREGROUND", "92d923"),
        "DEFAULT_BLOCK_COMMENT": ("FOREGROUND", "acacac"),
    }
    for key, (prop, exp) in anchors.items():
        got = attrs.get(key, {}).get("value", {}).get(prop)
        if got != exp:
            errors.append(f"anchor {key}.{prop}={got!r} want {exp!r}")

    for m in data["mappings"]:
        kind = m["kind"]
        key = m["key"]
        if kind == "process":
            continue
        if kind == "theme_json":
            sb = theme.get("ui", {}).get("ScrollBar", {})
            if sb.get("thumbColor") != "dark8":
                errors.append(f"theme ScrollBar.thumbColor={sb.get('thumbColor')!r}")
            continue
        if kind == "color":
            exp = (m.get("explicit") or {}).get("value")
            if colors.get(key) != exp:
                errors.append(f"color {key}={colors.get(key)!r} want {exp!r}")
            continue
        if key not in attrs:
            errors.append(f"missing attr {key}")
            continue
        cur = attrs[key]
        if kind == "baseAttributes":
            if cur["value"]:
                continue  # rich existing kept
            if cur["base"] != m.get("baseAttributes"):
                errors.append(
                    f"{key} base={cur['base']!r} want {m.get('baseAttributes')!r}"
                )
        elif kind == "explicit":
            for p, v in (m.get("explicit") or {}).items():
                if p not in STYLE:
                    continue
                if cur["value"].get(p) != str(v):
                    errors.append(
                        f"{key}.{p}={cur['value'].get(p)!r} want {v!r}"
                    )
        elif kind == "pin_empty":
            if cur["value"] and any(cur["value"].values()):
                # pin only when empty was intended; existing rich is ok
                pass

    # Gap closure vs Dracula+Islands if available
    dracula = Path(
        "/Volumes/repos/jasonrm/github.com/dracula/jetbrains/src/main/resources/themes/Dracula.xml"
    )
    islands = ROOT / "Islands_Dark.icls"
    if dracula.is_file() and islands.is_file():
        def names(path, section):
            r = ET.fromstring(path.read_text(errors="replace"))
            return {
                o.get("name")
                for o in r.find(section).findall("option")
                if o.get("name")
            }

        da = names(dracula, "attributes")
        colorful = dracula.with_name("DraculaColorful.xml")
        if colorful.is_file():
            da |= names(colorful, "attributes")
        ia = names(islands, "attributes")
        dc = names(dracula, "colors")
        ic = names(islands, "colors")
        miss_a = sorted((da | ia) - set(attrs))
        miss_c = sorted((dc | ic) - set(colors))
        if miss_a:
            errors.append(f"still missing {len(miss_a)} attrs e.g. {miss_a[:5]}")
        if miss_c:
            errors.append(f"still missing {len(miss_c)} colors: {miss_c}")

    print("verify_scheme_applied")
    print(f"  colors: {len(colors)}  attrs: {len(attrs)}")
    if errors:
        print(f"FAIL ({len(errors)})")
        for e in errors[:40]:
            print(f"  - {e}")
        if len(errors) > 40:
            print(f"  ... +{len(errors) - 40} more")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
