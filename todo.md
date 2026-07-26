# Hiberbee Dark — full scheme expansion todo

Goal: **expand Hiberbee editor definitions as far as practical** so languages and platform chrome do not silently fall back to Darcula.

## Color recommendations (apply these)

Every gap below has a pre-evaluated Hiberbee color / `baseAttributes` choice:

| Artifact | Path |
|---|---|
| **Human map** | [`docs/hiberbee-color-map.md`](docs/hiberbee-color-map.md) |
| **JSON (full)** | [`docs/hiberbee-color-map.json`](docs/hiberbee-color-map.json) |
| **CSV** | [`docs/hiberbee-color-map.csv`](docs/hiberbee-color-map.csv) |

Rules baked into the map: only palette tokens + hex already in `Dark.xml`; prefer `baseAttributes` → `DEFAULT_*`; no Dracula/Islands hex. Items marked **QA** in the map need a quick visual check after apply.

## References

| Source | Path | Role |
|---|---|---|
| **Dracula** (primary language catalog) | `/Volumes/repos/jasonrm/github.com/dracula/jetbrains/src/main/resources/themes/Dracula.xml` (+ Colorful extras) | Curated multi-language overrides (~453 attrs). Best peer theme for coverage. |
| **Islands Dark** (modern platform chrome) | `Islands_Dark.icls` (PhpStorm 2026.1) | Newer editor colors (Next Edit, inlays, doc UI, ignored-line borders). Sparse on languages. |
| **Hiberbee** (target) | `src/intellij/src/main/resources/colors/Dark.xml` | `parent_scheme="Darcula"`. ~577 real attrs (+ ~3.7k `MARKDOWN_NAVIGATOR.*` noise). |
| UI theme | `src/intellij/src/main/resources/themes/HiberbeeDark.theme.json` | Separate from editor scheme; only touch when editor keys need UI siblings (scrollbars, etc.). |

### Why not Darcula / raw export?

- Exporting **Darcula** yields a near-empty file: it *is* the parent, so there are no overrides.
- Export only writes **deltas**. Islands/Dracula are not complete platform dictionaries either, but Dracula is a maintained multi-language override set — the practical expansion checklist.
- Runtime merge remains: `Darcula → language plugins → Hiberbee overrides`.

### Inventory (union of Dracula + Islands − Hiberbee)

| Bucket | Count | Status (2026-07-26) |
|---|---|---|
| Missing **colors** | **22** | **Applied** → `Dark.xml` now 113 colors |
| Missing **attributes** (fully absent) | **~275** | **Applied** → ~4556 attrs (was ~4280) |
| Present attributes missing **style properties** | **~64** | **Merged** per color map |
| Hiberbee already strong (keep / extend, don’t clobber) | C# `ReSharper.*` (28), PHP specialized (13), TS (8), many `DEFAULT_*` | Preserved |

**Apply / verify:**

```bash
python3 scripts/apply_color_map.py          # idempotent
python3 scripts/verify_scheme_applied.py    # Dark.xml matches map
python3 scripts/verify_color_map.py         # map uses Hiberbee-only colors
```

### Implementation rules

1. **Map values to the Hiberbee palette** (`dark*`, `light*`, `accent`/`yellow`, `green`, `blue`, `red`, `*Bg`) — do **not** paste Dracula/Islands hex.
2. Prefer thin **`baseAttributes="DEFAULT_*"`** (or other Hiberbee keys) so language plugins inherit Hiberbee identity. Only set explicit FG/BG when the token needs a distinct role (unsafe, lifetime, macro, smart cast, …).
3. **Empty stubs** (`<value/>`) are still useful: they pin inheritance and prevent surprise parent changes — include them when references do.
4. Skip bulk-adding `MARKDOWN_NAVIGATOR.*` unless we intentionally support that plugin; Hiberbee already has thousands of those keys.
5. After each phase: `runIde` / visual check in PhpStorm, WebStorm, RustRover, Rider as relevant.

---

## Priority roadmap

| Priority | Phase | Why |
|---|---|---|
| P0 | 0 — `DEFAULT_*` completeness | Everything inherits from these |
| P0 | 1 — Target languages: PHP, HTML, TS, Rust, C# | Screenshot / product focus |
| P1 | 2 — JS, RegExp, XML, CSS/SASS, Markdown | Web stack adjacency |
| P1 | 3 — Platform colors + editor UX attrs | Next Edit, VCS, inlays, search/caret |
| P2 | 4 — Go, Python, Ruby, Kotlin extras | High-traffic secondary languages |
| P2 | 5 — Data formats + console/log | JSON/YAML/TOML/Properties, Logcat |
| P3 | 6 — Long tail | Scala/Groovy/Swift, ObjC, Velocity, XPath, space-named keys, etc. |
| P3 | 7 — Partial property upgrades | Backgrounds, stripes, underlines on existing keys |
| P3 | 8 — Theme JSON polish + samples/screenshots | Capture pipeline |

---

## Phase 0 — Language Defaults (`DEFAULT_*`)  `P0`

Foundation for almost all plugin highlighters. Hiberbee already has a strong set; fill the gaps.

- [ ] `DEFAULT_BLOCK_COMMENT` — **critical**; many langs (Rust block comments, etc.) base to this. Hiberbee has line comments only.
- [ ] `DEFAULT_HIGHLIGHTED_REFERENCE` — soft underline for highlighted refs (`EFFECT_COLOR` + `EFFECT_TYPE=1`)
- [ ] `DEFAULT_SEMICOLON` — pin (can be empty value or FG = identifier/light)
- [ ] `DEFAULT_LOCAL_VARIABLE` — pin (Dracula uses empty stub; enables language `baseAttributes`)

**Already present (do not regress):** braces, brackets, parens, keyword, string, number, function call/decl, instance/static field/method, metadata, doc tags, reassigned local/param, etc.

---

## Phase 1 — Target languages  `P0`

### 1.1 Rust (`org.rust.*`) — 8 present → add **49**

Hiberbee today: `CRATE`, `DOC_EMPHASIS`, `DOC_STRONG`, `MODULE`, `PRIMITIVE_TYPE`, `STRUCT`, `TYPE_PARAMETER`, `UNSAFE_CODE`.

Add (prefer `baseAttributes` → Hiberbee `DEFAULT_*`):

- [ ] `org.rust.ASSOC_FUNCTION` → `DEFAULT_STATIC_METHOD`
- [ ] `org.rust.ASSOC_FUNCTION_CALL` → `DEFAULT_STATIC_METHOD`
- [ ] `org.rust.ATTRIBUTE` → `DEFAULT_METADATA`
- [ ] `org.rust.BLOCK_COMMENT` → `DEFAULT_BLOCK_COMMENT` *(needs Phase 0)*
- [ ] `org.rust.BRACES` → `DEFAULT_BRACES`
- [ ] `org.rust.BRACKETS` → `DEFAULT_BRACKETS`
- [ ] `org.rust.CHAR` → `DEFAULT_STRING`
- [ ] `org.rust.COMMA` → `DEFAULT_COMMA`
- [ ] `org.rust.CONSTANT` → `DEFAULT_CONSTANT`
- [ ] `org.rust.CONST_PARAMETER` → `DEFAULT_CONSTANT`
- [ ] `org.rust.DOC_CODE` → `DEFAULT_DOC_MARKUP`
- [ ] `org.rust.DOC_COMMENT` → `DEFAULT_DOC_COMMENT`
- [ ] `org.rust.DOC_HEADING` → `DEFAULT_DOC_COMMENT_TAG`
- [ ] `org.rust.DOC_LINK` → `DEFAULT_DOC_COMMENT_TAG_VALUE`
- [ ] `org.rust.DOT` → `DEFAULT_DOT`
- [ ] `org.rust.ENUM` → `DEFAULT_CLASS_NAME`
- [ ] `org.rust.ENUM_VARIANT` → `DEFAULT_STATIC_FIELD`
- [ ] `org.rust.EOL_COMMENT` → `DEFAULT_LINE_COMMENT`
- [ ] `org.rust.FIELD` → `DEFAULT_INSTANCE_FIELD`
- [ ] `org.rust.FORMAT_PARAMETER` → `DEFAULT_VALID_STRING_ESCAPE`
- [ ] `org.rust.FUNCTION` → `DEFAULT_FUNCTION_DECLARATION`
- [ ] `org.rust.FUNCTION_CALL` → `DEFAULT_FUNCTION_CALL`
- [ ] `org.rust.INVALID_STRING_ESCAPE` → `DEFAULT_INVALID_STRING_ESCAPE`
- [ ] `org.rust.KEYWORD` → `DEFAULT_KEYWORD`
- [ ] `org.rust.METHOD` → `DEFAULT_INSTANCE_METHOD`
- [ ] `org.rust.METHOD_CALL` → `DEFAULT_FUNCTION_CALL`
- [ ] `org.rust.MUT_BINDING` → `DEFAULT_IDENTIFIER`
- [ ] `org.rust.MUT_PARAMETER` → `DEFAULT_PARAMETER`
- [ ] `org.rust.MUT_STATIC` → `DEFAULT_IDENTIFIER`
- [ ] `org.rust.NUMBER` → `DEFAULT_NUMBER`
- [ ] `org.rust.OPERATORS` → `DEFAULT_OPERATION_SIGN`
- [ ] `org.rust.PARAMETER` → `DEFAULT_PARAMETER`
- [ ] `org.rust.PARENTHESES` → `DEFAULT_PARENTHS`
- [ ] `org.rust.Q_OPERATOR` → `DEFAULT_KEYWORD`
- [ ] `org.rust.SEMICOLON` → `DEFAULT_SEMICOLON`
- [ ] `org.rust.STATIC` → `DEFAULT_IDENTIFIER`
- [ ] `org.rust.STRING` → `DEFAULT_STRING`
- [ ] `org.rust.TRAIT` → `DEFAULT_INTERFACE_NAME`
- [ ] `org.rust.TYPE_ALIAS` → `DEFAULT_CLASS_NAME`
- [ ] `org.rust.UNION` → `DEFAULT_CLASS_NAME`
- [ ] `org.rust.VALID_STRING_ESCAPE` → `DEFAULT_VALID_STRING_ESCAPE`
- [ ] `org.rust.VARIABLE` → `DEFAULT_IDENTIFIER`

Distinct roles (explicit Hiberbee colors, not pure base):

- [ ] `org.rust.CFG_DISABLED_CODE` — muted (`light1`/`light2`)
- [ ] `org.rust.FORMAT_SPECIFIER` — accent-adjacent
- [ ] `org.rust.GENERATED_ITEM` — muted
- [ ] `org.rust.KEYWORD_UNSAFE` — keyword + bold
- [ ] `org.rust.LIFETIME` — violet/italic
- [ ] `org.rust.MACRO` — green + bold
- [ ] `org.rust.SELF_PARAMETER` — constant-like + italic
- [ ] `org.rust.UNSAFE_CODE` — add **BACKGROUND** (`redBg`/`violetBg` family) if empty today

### 1.2 HTML — 1 present → add **5**

Present: `HTML_TAG_NAME`.

- [ ] `HTML_TAG`
- [ ] `HTML_ATTRIBUTE_NAME`
- [ ] `HTML_ATTRIBUTE_VALUE` → `DEFAULT_STRING`
- [ ] `HTML_ENTITY_REFERENCE`
- [ ] `HTML_CUSTOM_TAG_NAME` (Islands; web components)
- [ ] `MATCHED_TAG_NAME` (matching tag pair highlight)

### 1.3 XML — 3 present → add **5**

Present: `XML_PROLOGUE`, `XML_TAG_DATA`, `XML_TAG_NAME`.

- [ ] `XML_TAG`
- [ ] `XML_ATTRIBUTE_NAME`
- [ ] `XML_ENTITY_REFERENCE`
- [ ] `XML_NS_PREFIX`
- [ ] `XML_CUSTOM_TAG_NAME`

### 1.4 PHP — 13 present → add **4** from Dracula

Keep existing specialized keys (`PHP_NAMED_ARGUMENT`, `PHP_HEREDOC_ID`, `PHP_THIS_VAR`, …). Add:

- [ ] `PHP_CONSTANT`
- [ ] `PHP_HEREDOC_CONTENT`
- [ ] `PHP_PARAMETER` → `DEFAULT_PARAMETER`
- [ ] `PHP_VAR` → `DEFAULT_LOCAL_VARIABLE`
- [ ] `PHP_SCRIPTING_BACKGROUND` — ensure **BACKGROUND** set (currently effect-only)

### 1.5 TypeScript — 8 present → add **1**

Present: `TS.ENUM`, `TS.ENUM_MEMBER`, `TS.MODULE_NAME`, `TS.PRIMITIVE.TYPES`, `TS.PRIVATE_PUBLIC`, `TS.TYPE.ALIAS`, `TS.TYPE_GUARD`, `TS.TYPE_PARAMETER`.

- [ ] `TS.GLOBAL_VARIABLE`
- [ ] Optional follow-up (not in Dracula/Islands): audit WebStorm Color Scheme tree for any newer `TS.*` keys after IDE update

### 1.6 C# / ReSharper — already **28** keys

Hiberbee is **ahead of Dracula** here (Dracula has zero Rider keys). Expansion work:

- [ ] Audit Rider Color Scheme → C# / ReSharper for keys **not** in the list below; add any missing
- [ ] Keep existing:

```
ReSharper.ASP_NET_* (attrs, blocks, MVC, Razor)
ReSharper.CSHARP_ATTRIBUTE_IDENTIFIER
ReSharper.CSHARP_DELEGATE_IDENTIFIER
ReSharper.CSHARP_EVENT_IDENTIFIER
ReSharper.CSHARP_NAMESPACE_IDENTIFIER
ReSharper.CSHARP_STATIC_FIELD_IDENTIFIER
ReSharper.CSHARP_STATIC_PROPERTY_IDENTIFIER
ReSharper.ENUM_IDENTIFIER
ReSharper.EVENT_IDENTIFIER
ReSharper.EXTENSION_METHOD_IDENTIFIER
ReSharper.HINT
ReSharper.LATE_BOUND_IDENTIFIER
ReSharper.MUTABLE_LOCAL_VARIABLE_IDENTIFIER
ReSharper.NAMESPACE_IDENTIFIER
ReSharper.STATIC_CLASS_IDENTIFIER
ReSharper.STRUCT_IDENTIFIER
ReSharper.TYPE_PARAMETER_IDENTIFIER
```

- [ ] Prefer `baseAttributes` to `DEFAULT_*` where a ReSharper key is only a synonym

### 1.7 JavaScript — merge Dracula + Islands (disjoint sets)

Hiberbee has: `JS.DEBUGGER_STMT`, `JS.DOC_TYPE`, `JS.FUNCTION`, `JS.MODULE_KEYWORD`, `JS.MODULE_NAME`, `JS.NULL_UNDEFINED`, `JS.REGEXP`, `JS.THIS_SUPER`.

Add from Dracula/Islands:

- [ ] `JS.GLOBAL_FUNCTION` → `DEFAULT_FUNCTION_DECLARATION`
- [ ] `JS.GLOBAL_VARIABLE`
- [ ] `JS.INSTANCE_MEMBER_FUNCTION`
- [ ] `JS.LOCAL_VARIABLE` → `DEFAULT_LOCAL_VARIABLE`
- [ ] `JS.EXPORTED.VARIABLE`
- [ ] `JS.KEYWORD`
- [ ] `JS.VALID_STRING_ESCAPE`
- [ ] `JS.INVALID_STRING_ESCAPE`
- [ ] `JS.JSX_CLIENT_COMPONENT` (Islands / React)

---

## Phase 2 — Web adjacency  `P1`

### 2.1 RegExp — 2 present → add **9**

Present: `REGEXP.CHAR_CLASS`, `REGEXP_MATCHED_GROUPS`.

- [ ] `REGEXP.BRACES` (base `DEFAULT_BRACES` or explicit)
- [ ] `REGEXP.BRACKETS`
- [ ] `REGEXP.PARENTHS`
- [ ] `REGEXP.META`
- [ ] `REGEXP.ESC_CHARACTER` → `DEFAULT_VALID_STRING_ESCAPE`
- [ ] `REGEXP.QUOTE_CHARACTER`
- [ ] `REGEXP.COMMA`
- [ ] `REGEXP.INVALID_STRING_ESCAPE`
- [ ] `REGEXP.REDUNDANT_ESCAPE`

### 2.2 CSS / SASS / LESS — add **6**

Present already includes several `CSS.*` + `LESS_*` + `SASS_MIXIN`.

- [ ] `CSS.HASH`
- [ ] `CSS.IDENT`
- [ ] `CSS.PROPERTY_VALUE`
- [ ] `SASS_COMMENT` → `CSS.COMMENT` (or line comment)
- [ ] `SASS_IDENTIFIER`
- [ ] `SASS_VARIABLE` → `DEFAULT_INSTANCE_FIELD`

### 2.3 Markdown (underscore API keys)

Hiberbee has dotted `MARKDOWN.*` plugin keys. Also add platform underscore IDs used in newer builds:

- [ ] `MARKDOWN_AUTO_LINK`
- [ ] `MARKDOWN_LINK_TEXT`
- [ ] `MARKDOWN_IMAGE` (stub OK)
- [ ] Verify no conflict with existing `MARKDOWN.AUTO_LINK` / `MARKDOWN.IMAGE` at runtime

### 2.4 Custom file types

Hiberbee has `CUSTOM_KEYWORD2/3/4` only.

- [ ] `CUSTOM_KEYWORD1_ATTRIBUTES`
- [ ] `CUSTOM_STRING_ATTRIBUTES` → `DEFAULT_STRING`
- [ ] `CUSTOM_VALID_STRING_ESCAPE_ATTRIBUTES`
- [ ] `CUSTOM_INVALID_STRING_ESCAPE_ATTRIBUTES`

### 2.5 JSP / Qute

- [ ] `JSP_DIRECTIVE_NAME`
- [ ] `JSP_ATTRIBUTE_NAME`
- [ ] `JSP_DIRECTIVE_BACKGROUND`
- [ ] `JSP_SCRIPTING_BACKGROUND` — add BACKGROUND if missing
- [ ] `QUTE_BACKGROUND`

---

## Phase 3 — Platform colors & editor UX  `P1`

### 3.1 Missing colors (22)

**VCS / file status**

- [ ] `ANNOTATIONS_LAST_COMMIT_COLOR` (Islands)
- [ ] `FILESTATUS_RENAMED` (Dracula + Islands)
- [ ] `FILESTATUS_addedOutside`
- [ ] `FILESTATUS_changelistConflict` — *or* ensure `FILESTATUS_CHANGELIST_CONFLICT` is enough; add camelCase if product still reads it
- [ ] `FILESTATUS_modifiedOutside` — same note vs `FILESTATUS_MODIFIED_OUTSIDE`
- [ ] `FILESTATUS_IDEA_SVN_FILESTATUS_OBSTRUCTED` (Dracula)
- [ ] `FILESTATUS_IDEA_SVN_REPLACED` (Dracula)

**Diff / gutter**

- [ ] `IGNORED_DELETED_LINES_BORDER_COLOR`
- [ ] `IGNORED_MODIFIED_LINES_BORDER_COLOR`
  (Hiberbee already has `IGNORED_ADDED_LINES_BORDER_COLOR`)

**Documentation**

- [ ] `DOC_COMMENT_GUIDE`
- [ ] `DOC_COMMENT_LINK`

**Folding / inline refactoring**

- [ ] `FOLDED_TEXT_BORDER_COLOR`
- [ ] `INLINE_REFACTORING_SETTINGS_DEFAULT`
- [ ] `INLINE_REFACTORING_SETTINGS_FOCUSED`
- [ ] `INLINE_REFACTORING_SETTINGS_HOVERED`

**Next Edit (AI suggestions)**

- [ ] `NEXT_EDIT.DIFF_AFTER_BACKGROUND` → `greenBg`-family
- [ ] `NEXT_EDIT.EDIT_RANGE.GUTTER_BACKGROUND` → `violetBg`-family
- [ ] `NEXT_EDIT.EDIT_RANGE.LINE_BACKGROUND`
- [ ] `NEXT_EDIT.INSIGHT_BACKGROUND`
- [ ] `NEXT_EDIT.REMOVAL_BACKGROUND` → `redBg`-family

**macOS scrollbars**

- [ ] `ScrollBar.Mac.thumbColor` (translucent)
- [ ] `ScrollBar.Mac.hoverThumbColor`

### 3.2 Doc / inlay attributes

- [ ] `DOC_CODE_BLOCK` (FG + BG + border)
- [ ] `DOC_CODE_INLINE` (FG + BG)
- [ ] `DOC_TIPS_SHORTCUT`
- [ ] `INLAY_DEFAULT` (FG + BG)
- [ ] `INLAY_TEXT_WITHOUT_BACKGROUND`
- [ ] `ANNOTATION_NAME_ATTRIBUTES` → `DEFAULT_METADATA` (or empty base pin)

---

## Phase 4 — Secondary languages  `P2`

### 4.1 Go — add **43** (`GO_*`)

Full Dracula/Colorful set, including:

- [ ] Keywords / builtins: `GO_KEYWORD`, `GO_BUILTIN_*`, `GO_PACKAGE`, `GO_LABEL`, `GO_IDENTIFIER`
- [ ] Types / structs / interfaces: `GO_*_STRUCT*`, `GO_*_INTERFACE*`, `GO_TYPE_*`
- [ ] Calls / params / receivers: `GO_*_FUNCTION_CALL`, `GO_FUNCTION_PARAMETER`, `GO_METHOD_RECEIVER`
- [ ] Literals: `GO_STRING`, `GO_NUMBER`, `GO_*_STRING_ESCAPE`, `GO_BLOCK_COMMENT`
- [ ] Semantics: `GO_SHADOWING_VARIABLE`, `GO_REASSIGNMENT_IN_SHORT_VAR_DECLARATION`, `GO_BAD_TOKEN`
- [ ] Punctuation stubs: `GO_COMMA`, `GO_DOT`, `GO_OPERATOR`, `GO_SEMICOLON`, `GO_COLON`
- [ ] `GO_STRUCT_LOCAL_MEMBER` (from Dracula Colorful)

### 4.2 Python — add **20** (`PY.*`)

Hiberbee has a few (`PY.ANNOTATION`, `PY.DECORATOR`, `PY.KEYWORD_ARGUMENT`, `PY.SELF_PARAMETER`, `PY.STRING`, `PY.STRING.B`).

- [ ] `PY.KEYWORD`, `PY.NUMBER`, `PY.OPERATION_SIGN`
- [ ] `PY.FUNCTION_CALL`, `PY.METHOD_CALL`, `PY.BUILTIN_NAME`
- [ ] `PY.CLASS_DEFINITION`, `PY.PREDEFINED_DEFINITION`, `PY.PREDEFINED_USAGE`
- [ ] `PY.DOC_COMMENT`, `PY.DOC_COMMENT_TAG`, `PY.LINE_COMMENT`
- [ ] `PY.FSTRING_FRAGMENT_BRACES`, `PY.FSTRING_FRAGMENT_COLON`
- [ ] `PY.STRING.U`
- [ ] Punctuation stubs: `PY.BRACES`, `PY.BRACKETS`, `PY.PARENTHS`, `PY.COMMA`, `PY.DOT`
- [ ] Enrich `PY.SELF_PARAMETER` with `FONT_TYPE` if desired

### 4.3 Ruby / HAML / RHTML — add **26**

- [ ] Core `RUBY_*` (comment, constant, method, number, symbol, ivar/cvar/gvar, escapes, heredoc, regexp, params, …)
- [ ] `HAML_COMMENT`, `HAML_ID`, `HAML_RUBY_CODE`, and enrich `HAML_TAG` if present
- [ ] `RHTML_*` scriptlet/expression markers

### 4.4 Kotlin extras — add **3** (+ partials later)

Hiberbee already has a large Kotlin set. Missing from refs:

- [ ] `KOTLIN_ARROW`
- [ ] `KOTLIN_ENUM_ENTRY`
- [ ] `KOTLIN_PACKAGE_PROPERTY`
- [ ] Fill empty `KOTLIN_LABEL` FOREGROUND
- [ ] Smart-cast **BACKGROUND**s + mutable variable `EFFECT_COLOR` (Phase 7)

---

## Phase 5 — Data formats & console  `P2`

### 5.1 JSON / YAML / TOML / Properties — add **11**

- [ ] `JSON.KEYWORD`, `JSON.NUMBER`, `JSON.PROPERTY_KEY`, `JSON.STRING`, `JSON.VALID_ESCAPE`
- [ ] `YAML_ANCHOR`, `YAML_TEXT`
- [ ] Enrich `YAML_SCALAR_LIST` / `YAML_SCALAR_VALUE` with BACKGROUND if useful
- [ ] `org.toml.KEY`, `org.toml.DATE`
- [ ] `PROPERTIES.INVALID_STRING_ESCAPE`, `PROPERTIES.VALID_STRING_ESCAPE`

### 5.2 Console / Logcat — add **7**

- [ ] `CONSOLE_SELECTED_PARAMETER`
- [ ] `LOGCAT_ASSERT_OUTPUT`, `LOGCAT_DEBUG_OUTPUT`, `LOGCAT_ERROR_OUTPUT`, `LOGCAT_INFO_OUTPUT`, `LOGCAT_VERBOSE_OUTPUT`, `LOGCAT_WARNING_OUTPUT`
  (Hiberbee already has several other `LOGCAT_*` / console keys — merge carefully)

---

## Phase 6 — Long tail  `P3`

Still in the Dracula∪Islands gap set; add for full expansion:

### 6.1 Java / constructors / interfaces

- [ ] `JAVA_KEYWORD`
- [ ] `CONSTRUCTOR_CALL_ATTRIBUTES`, `CONSTRUCTOR_DECLARATION_ATTRIBUTES`
- [ ] `INTERFACE_NAME_ATTRIBUTES`
- [ ] `STATIC_METHOD_ATTRIBUTES` → `DEFAULT_STATIC_METHOD`
- [ ] Space-named: `Abstract class name`, `Interface name`, `Method call`, `Annotation`, `Anotation attribute name` *(sic)*, `Number`, `String`, `Valid string escape`, `Standart Java Collection` *(sic)*

### 6.2 Scala / Groovy / Swift

- [ ] Scala: Abstract class, Predefined types, Type Alias, Type parameter, ScalaDoc @param value
- [ ] Groovy: constructor call, method declaration, parameter, reassigned parameter
- [ ] `SWIFT_ATTRIBUTE_NAME`, `SWIFT_MODULE_NAME`

### 6.3 ObjC

- [ ] `OC.DIRECTIVE`, `OC.METHOD_DECLARATION`
- [ ] Enrich `OC.CONDITIONALLY_NOT_COMPILED` FOREGROUND if empty

### 6.4 Templates / query / misc plugins

- [ ] Velocity: `VELOCITY_DIRECTIVE`, `VELOCITY_KEYWORD`, `VELOCITY_REFERENCE`, `VELOCITY_SCRIPTING_BACKGROUND`
- [ ] XPath: `XPATH.FUNCTION`, `XPATH.KEYWORD`, `XPATH.XPATH_VARIABLE`
- [ ] Protobuf: `PROTO_IDENTIFIER`, `PROTOTEXT_IDENTIFIER`
- [ ] CodeQL: `QL_ATTRIBUTE`, `QL_FUNCTION`, `QL_PARAMETER`
- [ ] `HTTP_REQUEST_MESSAGE_BODY`
- [ ] `JUPYTER_CELL_MARKER`
- [ ] `GRID_ERROR_VALUE`
- [ ] `MAKO.SUBSTITUTION`, `SPY-JS.EXCEPTION`, `SPY-JS.FUNCTION_SCOPE`
- [ ] `com.plan9.IDENTIFIER`, `com.plan9.LABEL`, `com.plan9.REGISTER`
- [ ] `Class` → `CLASS_NAME_ATTRIBUTES`, `Closure braces`, `Label`, `List/map to object conversion`, `TAG_ATTR_KEY`

### 6.5 Python-style access attributes (space names)

- [ ] `Static method access`
- [ ] `Static property reference ID`
- [ ] `Unresolved reference access`

---

## Phase 7 — Partial property upgrades  `P3`

Keys **already in Hiberbee** that refs style more completely. Prefer additive props; keep Hiberbee FG identity.

### 7.1 High impact

- [ ] `IDENTIFIER_UNDER_CARET_ATTRIBUTES` — BACKGROUND, ERROR_STRIPE, EFFECT_TYPE
- [ ] `WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES` — same
- [ ] `SEARCH_RESULT_ATTRIBUTES` / `TEXT_SEARCH_RESULT_ATTRIBUTES` / `WRITE_SEARCH_RESULT_ATTRIBUTES` — BACKGROUND + ERROR_STRIPE
- [ ] `FOLDED_TEXT_ATTRIBUTES` — BACKGROUND
- [ ] `INLINE_PARAMETER_HINT` / `_CURRENT` / `_HIGHLIGHTED` — BACKGROUND
- [ ] `INJECTED_LANGUAGE_FRAGMENT` — BACKGROUND
- [ ] `DEFAULT_TEMPLATE_LANGUAGE_COLOR` — BACKGROUND
- [ ] `DEFAULT_REASSIGNED_LOCAL_VARIABLE` / `DEFAULT_REASSIGNED_PARAMETER` — EFFECT_COLOR + EFFECT_TYPE
- [ ] `TEXT_STYLE_ERROR` / `TEXT_STYLE_WARNING` — fill empty stubs
- [ ] `CONSOLE_RANGE_TO_EXECUTE` — EFFECT_COLOR
- [ ] `KOTLIN_LABEL` — FOREGROUND
- [ ] `KOTLIN_SMART_CAST_*` — BACKGROUND
- [ ] `KOTLIN_MUTABLE_VARIABLE` — EFFECT_COLOR
- [ ] `NOT_TOP_FRAME_ATTRIBUTES` — BACKGROUND
- [ ] `TODO_DEFAULT_ATTRIBUTES` — FONT_TYPE + ERROR_STRIPE
- [ ] `BOOKMARKS_ATTRIBUTES` / `BREAKPOINT_ATTRIBUTES` — ERROR_STRIPE
- [ ] `org.rust.UNSAFE_CODE` — BACKGROUND
- [ ] `PHP_SCRIPTING_BACKGROUND` — BACKGROUND
- [ ] `DELETED_TEXT_ATTRIBUTES` — BACKGROUND

### 7.2 Medium / optional font & FG

- [ ] `BAD_CHARACTER`, `UNMATCHED_BRACE_ATTRIBUTES`, `WRONG_REFERENCES_ATTRIBUTES` — FOREGROUND
- [ ] `CTRL_CLICKABLE` — FOREGROUND + EFFECT_TYPE
- [ ] `DEFAULT_INVALID_STRING_ESCAPE` — FOREGROUND
- [ ] `MATCHED_BRACE_ATTRIBUTES` — FOREGROUND
- [ ] `INACTIVE_HYPERLINK_ATTRIBUTES` — FOREGROUND
- [ ] Font italics/bold (`FONT_TYPE`) on: constants, statics, doc comments, parameters, coverage lines, `CSS.IMPORTANT`, `CONSOLE_USER_INPUT`, `PY.SELF_PARAMETER`, `REGEXP.CHAR_CLASS`, etc.
- [ ] `CODE_LENS_BORDER_COLOR` — confirm whether platform wants EFFECT_COLOR vs BACKGROUND
- [ ] `ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES` — EFFECT_TYPE
- [ ] `PROPERTIES.KEY` — EFFECT_TYPE
- [ ] YAML scalar BACKGROUND, HAML_TAG BACKGROUND, JSP_SCRIPTING_BACKGROUND, STATIC_FINAL_FIELD_ATTRIBUTES EFFECT_TYPE, Scala collection EFFECT_TYPE

---

## Phase 8 — Theme JSON, samples, screenshots  `P3`

### 8.1 UI theme siblings

- [ ] `ScrollBar.thumbColor` (non-hover) in `HiberbeeDark.theme.json` — only `hoverThumbColor` today
- [ ] Align Mac editor scrollbar keys with UI ScrollBar tokens

### 8.2 Showcase samples (for previews + manual QA)

- [ ] `samples/php/Showcase.php` — tags, heredoc, attributes, named args, types
- [ ] `samples/html/Showcase.html` — tags, attrs, entities, custom elements
- [ ] `samples/typescript/Showcase.ts` — enums, type aliases, generics, guards, globals
- [ ] `samples/rust/Showcase.rs` — structs, traits, lifetimes, macros, unsafe, formats
- [ ] `samples/csharp/Showcase.cs` — namespaces, attributes, extension methods, generics
- [ ] Optional: `samples/go`, `python`, `ruby` after Phase 4

### 8.3 Screenshot generation

No official scheme→PNG tool. Practical pipeline:

1. Load theme in IDE (`./gradlew runIde` or installed plugin)
2. Open showcase file; Hide All Tool Windows; fixed font/zoom
3. Capture via OS screenshot or [ScreenCode](https://plugins.jetbrains.com/plugin/19546-screencode)
4. Output under `screenshots/{php,html,typescript,rust,csharp}.png`
5. PhpStorm → PHP/HTML · WebStorm → TS · RustRover → Rust · Rider → C#

- [ ] Document capture steps in README or CONTRIBUTING
- [ ] Produce five language screenshots for Marketplace / README

---

## Already covered (do not treat as gaps)

### Alias notes

| Islands / Dracula key | Hiberbee equivalent (already present) |
|---|---|
| `FILESTATUS_changelistConflict` | `FILESTATUS_CHANGELIST_CONFLICT` (add camelCase only if still required) |
| `FILESTATUS_modifiedOutside` | `FILESTATUS_MODIFIED_OUTSIDE` |
| `MARKDOWN_AUTO_LINK` / `MARKDOWN_IMAGE` | Also add underscore IDs; dotted `MARKDOWN.*` already exist |

### Hiberbee strengths vs Dracula

| Area | Hiberbee | Dracula |
|---|---|---|
| C# / ReSharper | **28** | 0 |
| PHP specialized | **13** | 8 |
| TypeScript | **8** | 3 |
| `DEFAULT_*` punctuation (braces etc.) | stronger explicit set | often inherited |
| Markdown Navigator | massive (optional noise) | none |

---

## Suggested implementation order (execution checklist)

1. [ ] **Phase 0** — `DEFAULT_BLOCK_COMMENT`, highlighted reference, semicolon, local variable
2. [ ] **Phase 1.1** — full Rust `baseAttributes` map + distinct roles
3. [ ] **Phase 1.2–1.3** — HTML/XML completeness
4. [ ] **Phase 1.4–1.7** — PHP gaps, TS.GLOBAL_VARIABLE, JS merge, C# audit
5. [ ] **Phase 2** — RegExp, CSS/SASS, Markdown, custom keywords, JSP/Qute
6. [ ] **Phase 3** — colors (VCS, Next Edit, scrollbars) + doc/inlays
7. [ ] **Phase 7.1** — search/caret/inlay backgrounds (high visual ROI)
8. [ ] **Phase 4–6** — Go/Python/Ruby + data/console + long tail
9. [ ] **Phase 7.2 + 8** — polish, samples, screenshots

### Mechanical approach for large batches

```text
For each missing key in Dracula:
  if baseAttributes is set:
    emit <option name="..." baseAttributes="..."/>  # retarget to Hiberbee DEFAULT_* names
  else if only FOREGROUND matching a DEFAULT role:
    convert to baseAttributes
  else:
    emit explicit value using Hiberbee hex from palette
```

A small script can generate the XML stubs from Dracula’s attribute list, then human-review explicit colors.

---

## Verification

After each phase:

- [ ] Scheme loads without errors (unknown keys are usually ignored; still prefer valid IDs)
- [ ] Language Defaults panel looks complete for block comments / refs
- [ ] PHP / HTML / TS / Rust / C# showcase files: no obvious Darcula leftovers
- [ ] VCS file colors: renamed, added-outside
- [ ] Search + identifier-under-caret backgrounds
- [ ] Next Edit ranges (IDE with AI features)
- [ ] macOS scrollbar thumb idle vs hover
- [ ] Quick Doc code chips / inlays

---

## Counts to beat

| Metric | Now (approx.) | After full expansion (target) |
|---|---|---|
| Real attrs (no MDN) | ~577 | **~850+** |
| `org.rust.*` | 8 | **~57** |
| HTML_* | 1 | **~6** |
| JS.* | 8 | **~17** |
| GO_* | 3 (templates only) | **~45** |
| Editor colors | 91 | **~110+** |

Keep identity: expand **coverage**, not recolor Hiberbee to Dracula/Islands.
)
