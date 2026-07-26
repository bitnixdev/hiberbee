#!/usr/bin/env python3
"""Apply docs/hiberbee-color-map.json into Dark.xml (+ ScrollBar.thumbColor in theme.json).

Idempotent: re-running merges explicit props and skips clobbering rich existing attrs
when the map only asks for baseAttributes.

  python3 scripts/apply_color_map.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCHEME = ROOT / "src/intellij/src/main/resources/colors/Dark.xml"
THEME = ROOT / "src/intellij/src/main/resources/themes/HiberbeeDark.theme.json"
MAP_PATH = ROOT / "docs/hiberbee-color-map.json"

PROP_ORDER = [
    "FOREGROUND",
    "BACKGROUND",
    "FONT_TYPE",
    "EFFECT_COLOR",
    "EFFECT_TYPE",
    "ERROR_STRIPE_COLOR",
]


def prop_sort_key(name: str):
    try:
        return (0, PROP_ORDER.index(name))
    except ValueError:
        return (1, name)


def set_value_props(option_el: ET.Element, props: dict, merge: bool) -> None:
    if "baseAttributes" in option_el.attrib:
        del option_el.attrib["baseAttributes"]

    value_el = option_el.find("value")
    existing: dict = {}
    if value_el is not None:
        for child in list(value_el):
            existing[child.get("name")] = child.get("value")
            value_el.remove(child)
    else:
        value_el = ET.SubElement(option_el, "value")

    merged = {**existing, **props} if merge else dict(props)
    merged = {k: v for k, v in merged.items() if v is not None}
    if not merged:
        return
    for k in sorted(merged.keys(), key=prop_sort_key):
        child = ET.SubElement(value_el, "option")
        child.set("name", k)
        child.set("value", str(merged[k]))


def set_base(option_el: ET.Element, base: str) -> None:
    for child in list(option_el):
        option_el.remove(child)
    option_el.attrib.pop("value", None)
    option_el.set("baseAttributes", base)


def set_pin_empty(option_el: ET.Element) -> None:
    for child in list(option_el):
        option_el.remove(child)
    option_el.attrib.pop("baseAttributes", None)
    ET.SubElement(option_el, "value")


def serialize_scheme(root: ET.Element) -> str:
    lines = [
        f'<scheme name="{root.get("name")}" version="{root.get("version")}" '
        f'parent_scheme="{root.get("parent_scheme")}">'
    ]
    meta = root.find("metaInfo")
    if meta is not None:
        lines.append("  <metaInfo>")
        for p in meta.findall("property"):
            lines.append(f'    <property name="{p.get("name")}">{p.text or ""}</property>')
        lines.append("  </metaInfo>")

    colors = root.find("colors")
    lines.append("  <colors>")
    for o in colors.findall("option"):
        lines.append(f'    <option name="{o.get("name")}" value="{o.get("value") or ""}" />')
    lines.append("  </colors>")

    attrs = root.find("attributes")
    lines.append("  <attributes>")
    for o in attrs.findall("option"):
        n = (o.get("name") or "").replace('"', "&quot;")
        base = o.get("baseAttributes")
        value_el = o.find("value")
        if base is not None and value_el is None:
            lines.append(f'    <option name="{n}" baseAttributes="{base}" />')
            continue
        if value_el is None:
            lines.append(f'    <option name="{n}" />')
            continue
        children = list(value_el)
        if not children:
            lines.append(f'    <option name="{n}">')
            lines.append("      <value />")
            lines.append("    </option>")
            continue
        lines.append(f'    <option name="{n}">')
        lines.append("      <value>")
        for c in children:
            lines.append(
                f'        <option name="{c.get("name")}" value="{c.get("value") or ""}" />'
            )
        lines.append("      </value>")
        lines.append("    </option>")
    lines.append("  </attributes>")
    lines.append("</scheme>")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if not MAP_PATH.is_file():
        print(f"FAIL: missing {MAP_PATH}", file=sys.stderr)
        return 1

    data = json.loads(MAP_PATH.read_text())
    root = ET.fromstring(SCHEME.read_text())
    colors_el = root.find("colors")
    attrs_el = root.find("attributes")

    meta = root.find("metaInfo")
    if meta is not None:
        for p in meta.findall("property"):
            if p.get("name") == "modified":
                p.text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    stats: Counter = Counter()
    color_map = {o.get("name"): o for o in colors_el.findall("option") if o.get("name")}
    attr_map = {o.get("name"): o for o in attrs_el.findall("option") if o.get("name")}

    for m in data["mappings"]:
        kind = m["kind"]
        key = m["key"]

        if kind in ("process", "theme_json"):
            stats[f"skip_{kind}"] += 1
            continue

        if kind == "color":
            val = (m.get("explicit") or {}).get("value")
            if not val:
                stats["skip_no_value"] += 1
                continue
            if key in color_map:
                color_map[key].set("value", val)
                stats["color_updated"] += 1
            else:
                o = ET.SubElement(colors_el, "option")
                o.set("name", key)
                o.set("value", val)
                color_map[key] = o
                stats["color_added"] += 1
            continue

        if kind not in ("baseAttributes", "explicit", "pin_empty"):
            stats[f"skip_{kind}"] += 1
            continue

        is_new = key not in attr_map
        if is_new:
            o = ET.SubElement(attrs_el, "option")
            o.set("name", key)
            attr_map[key] = o
            stats["attr_added"] += 1
        else:
            o = attr_map[key]
            stats["attr_existing"] += 1

        if kind == "baseAttributes":
            base = m.get("baseAttributes")
            if not base:
                stats["skip_no_base"] += 1
                continue
            if not is_new:
                val = o.find("value")
                if val is not None and len(list(val)) > 0:
                    stats["attr_keep_existing_rich"] += 1
                    continue
            set_base(o, base)
            stats["attr_set_base"] += 1
        elif kind == "pin_empty":
            if not is_new:
                val = o.find("value")
                has_props = val is not None and len(list(val)) > 0
                if has_props or o.get("baseAttributes"):
                    stats["attr_keep_existing_vs_pin"] += 1
                    continue
            set_pin_empty(o)
            stats["attr_pin_empty"] += 1
        else:
            props = m.get("explicit") or {}
            style_props = {
                k: v
                for k, v in props.items()
                if k in PROP_ORDER or (isinstance(k, str) and k.isupper())
            }
            if not style_props:
                if is_new:
                    set_pin_empty(o)
                    stats["attr_pin_empty"] += 1
                else:
                    stats["attr_skip_empty_explicit"] += 1
                continue
            set_value_props(o, style_props, merge=not is_new)
            stats["attr_set_explicit"] += 1

    out = serialize_scheme(root)
    ET.fromstring(out)
    SCHEME.write_text(out)

    theme = json.loads(THEME.read_text())
    sb = theme.setdefault("ui", {}).setdefault("ScrollBar", {})
    if "thumbColor" not in sb:
        sb["thumbColor"] = "dark8"
        stats["theme_thumb_added"] += 1
    if "hoverThumbColor" not in sb:
        sb["hoverThumbColor"] = "dark10"
    THEME.write_text(json.dumps(theme, indent=2) + "\n")

    print("apply_color_map:")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
    print(f"  wrote {SCHEME.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
