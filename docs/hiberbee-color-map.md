# Hiberbee color map — expansion recommendations

**Purpose:** For every gap in [`todo.md`](../todo.md), pick the best **existing** Hiberbee color or `baseAttributes` target. Implementers should apply this map into `Dark.xml` / `HiberbeeDark.theme.json` without inventing new hex.

**Sources (closed set):**
- Palette tokens: `src/intellij/src/main/resources/themes/HiberbeeDark.theme.json` → `colors`
- Scheme anchors: hex / keys already in `src/intellij/src/main/resources/colors/Dark.xml`
- **Not used for hex:** Dracula, Islands (semantic role only)

**Machine-readable:** [`hiberbee-color-map.json`](hiberbee-color-map.json) · [`hiberbee-color-map.csv`](hiberbee-color-map.csv)

## Role anchors (Hiberbee identity)

| Role | Anchor | Hex / token |
|---|---|---|
| `DEFAULT_LINE_COMMENT` | scheme/palette | `acacac` |
| `DEFAULT_KEYWORD` | scheme/palette | `ee7762` |
| `DEFAULT_STRING` | scheme/palette | `ffd866` |
| `DEFAULT_NUMBER` | scheme/palette | `78d7` |
| `DEFAULT_FUNCTION_CALL` | scheme/palette | `92d923` |
| `DEFAULT_METADATA` | scheme/palette | `ffb900` |
| `DEFAULT_CONSTANT` | scheme/palette | `f25022` |
| `greenBg` | scheme/palette | `203020` |
| `redBg` | scheme/palette | `320f0f` |
| `violetBg` | scheme/palette | `302030` |
| `blueBg` | scheme/palette | `253047` |
| `orangeBg` | scheme/palette | `403018` |
| `dark8` | scheme/palette | `424140` |
| `dark10` | scheme/palette | `525150` |
| `light1` | scheme/palette | `6f6e6d` |
| `light3` | scheme/palette | `8f8e8d` |
| `FILESTATUS_ADDED` | scheme/palette | `a9dc76` |
| `FILESTATUS_MODIFIED` | scheme/palette | `78dce8` |
| `FILESTATUS_CHANGELIST_CONFLICT` | scheme/palette | `f65f87` |

### Semantic → Hiberbee

| Semantic intent | Use |
|---|---|
| Keyword | `DEFAULT_KEYWORD` `#ee7762` |
| String | `DEFAULT_STRING` `#ffd866` (Python exception: `PY.STRING` `#a9dc76`) |
| Number | `DEFAULT_NUMBER` |
| Function call / macro | `DEFAULT_FUNCTION_CALL` / green `#92d923` |
| Function declaration | `DEFAULT_FUNCTION_DECLARATION` `#b7e66e` |
| Metadata / annotation / accent | `DEFAULT_METADATA` / `accent` `#ffb900` |
| Constant / error-ish red | `DEFAULT_CONSTANT` `#f25022` |
| Comment / muted | `DEFAULT_LINE_COMMENT` `#acacac` or `light1`–`light3` |
| Class / type cyan | `DEFAULT_CLASS_NAME` `#57d1eb` |
| Interface / custom tag | `DEFAULT_INTERFACE_NAME` / `blue` `#409cff` |
| Violet static / lifetime | `DEFAULT_STATIC_FIELD` `#9896ff` |
| Tag pink | `DEFAULT_TAG` / `CSS.TAG_NAME` `#ff6188` |
| Soft UI chrome | `dark8`–`dark10` |
| Success / insert bg | `greenBg` `#203020` |
| Danger / removal bg | `redBg` `#320f0f` |
| Insight / unsafe tint | `violetBg` `#302030` |
| Info / injection bg | `blueBg` `#253047` |
| Write-occurrence bg | `orangeBg` `#403018` |
| VCS added | `FILESTATUS_ADDED` `#a9dc76` |
| VCS modified | `FILESTATUS_MODIFIED` `#78dce8` |
| VCS conflict | `FILESTATUS_CHANGELIST_CONFLICT` `#f65f87` |

## Recommendation kinds

| kind | Meaning |
|---|---|
| `baseAttributes` | Emit `<option name="…" baseAttributes="DEFAULT_…"/>` only |
| `explicit` | Set FOREGROUND/BACKGROUND/EFFECT_* using listed hex (all Hiberbee-native) |
| `color` | Editor scheme `<colors><option value="…"/>` |
| `pin_empty` | Emit empty `<value/>` to pin inheritance |
| `theme_json` | UI theme key, not Dark.xml |
| `process` | Non-color work (audit, samples, verify) |

## Counts

- Total mapped entries: **385**
- `baseAttributes`: 187
- `color`: 22
- `explicit`: 134
- `pin_empty`: 19
- `process`: 22
- `theme_json`: 1
- Missing attrs from Dracula∪Islands: **275/275**
- Missing colors: **22/22**

## Human visual QA

Items flagged `qa: true` should be eyeballed after apply:

- `DEFAULT_HIGHLIGHTED_REFERENCE` — Soft underline with light3 (muted chrome); avoids competing with caret/selection accent
- `org.rust.KEYWORD_UNSAFE` — Unsafe keyword = keyword color + bold
- `org.rust.LIFETIME` — Lifetimes are type-ish violet (static_field 9896ff) + italic
- `org.rust.MACRO` — Macros ≈ function call green + bold (Hiberbee call = 92d923)
- `org.rust.UNSAFE_CODE` — Unsafe region tint violetBg (302030); softer than redBg so not error-like
- `HTML_CUSTOM_TAG_NAME` — Custom elements ≈ interface blue 409cff (distinct from native tags)
- `MATCHED_TAG_NAME` — Matching tag pair subtle fill dark8 (424140)
- `PHP_SCRIPTING_BACKGROUND` — PHP island background dark4 (222120) subtle lift; keep existing EFFECT_TYPE if any
- `JS.JSX_CLIENT_COMPONENT` — Client components distinct violet 9896ff (not string green)
- `NEXT_EDIT.DIFF_AFTER_BACKGROUND` — Next Edit insertion tint greenBg
- `NEXT_EDIT.EDIT_RANGE.GUTTER_BACKGROUND` — Next Edit range gutter violetBg
- `NEXT_EDIT.EDIT_RANGE.LINE_BACKGROUND` — Next Edit line wash dark3 (deeper than gutter)
- `NEXT_EDIT.INSIGHT_BACKGROUND` — Insight panel violetBg
- `NEXT_EDIT.REMOVAL_BACKGROUND` — Removal suggestion redBg
- `ScrollBar.Mac.thumbColor` — Idle Mac thumb dark8 solid (scheme may accept 6-digit); optional alpha via yellowDark pattern only if needed
- `ScrollBar.Mac.hoverThumbColor` — Hover Mac thumb dark10 (matches ui.ScrollBar.hoverThumbColor token)
- `DOC_CODE_BLOCK` — Quick Doc code block: light text on dark4, border dark8
- `INLAY_DEFAULT` — Default inlay = hint gray on dark8
- `IDENTIFIER_UNDER_CARET_ATTRIBUTES` — Read occurrences: greenBg + green stripe; keep cyan effect
- `WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES` — Write occurrences: orangeBg tint
- `SEARCH_RESULT_ATTRIBUTES` — Search hits greenBg family
- `TEXT_SEARCH_RESULT_ATTRIBUTES` — Text search blueBg
- `WRITE_SEARCH_RESULT_ATTRIBUTES` — Write search violetBg
- `INLINE_PARAMETER_HINT_CURRENT` — Current param blueBg
- `INJECTED_LANGUAGE_FRAGMENT` — Injection host blueBg wash
- `KOTLIN_SMART_CAST_RECEIVER` — Smart-cast receiver greenBg
- `KOTLIN_SMART_CAST_VALUE` — Smart-cast value violetBg
- `KOTLIN_SMART_CONSTANT` — Smart-cast const redBg light
- `CODE_LENS_BORDER_COLOR` — Set both BG and EFFECT_COLOR to dark10 for platform variance
- `ScrollBar.thumbColor` — UI thumb dark8 to pair with hoverThumbColor dark10

## Phase 0 — Language Defaults

| Key | Recommendation | Rationale |
|---|---|---|
| `DEFAULT_BLOCK_COMMENT` | explicit: `FOREGROUND=acacac` | Match DEFAULT_LINE_COMMENT acacac so block/line comments share Hiberbee muted gray |
| `DEFAULT_HIGHLIGHTED_REFERENCE` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1` ⚠QA | Soft underline with light3 (muted chrome); avoids competing with caret/selection accent |
| `DEFAULT_LOCAL_VARIABLE` | `pin_empty` (inherit) | Pin empty; enables language baseAttributes→DEFAULT_LOCAL_VARIABLE without forcing a color (identifier default) |
| `DEFAULT_SEMICOLON` | `pin_empty` (inherit) | Pin empty so punctuation inherits platform; optional later FG=light6 if desired |

## Phase 1.1 — Rust

| Key | Recommendation | Rationale |
|---|---|---|
| `org.rust.ASSOC_FUNCTION` | `baseAttributes` → `DEFAULT_STATIC_METHOD` | Rust plugin synonym → DEFAULT_STATIC_METHOD |
| `org.rust.ASSOC_FUNCTION_CALL` | `baseAttributes` → `DEFAULT_STATIC_METHOD` | Rust plugin synonym → DEFAULT_STATIC_METHOD |
| `org.rust.ATTRIBUTE` | `baseAttributes` → `DEFAULT_METADATA` | Rust plugin synonym → DEFAULT_METADATA |
| `org.rust.BLOCK_COMMENT` | `baseAttributes` → `DEFAULT_BLOCK_COMMENT` | Rust plugin synonym → DEFAULT_BLOCK_COMMENT |
| `org.rust.BRACES` | `baseAttributes` → `DEFAULT_BRACES` | Rust plugin synonym → DEFAULT_BRACES |
| `org.rust.BRACKETS` | `baseAttributes` → `DEFAULT_BRACKETS` | Rust plugin synonym → DEFAULT_BRACKETS |
| `org.rust.CFG_DISABLED_CODE` | explicit: `FOREGROUND=6f6e6d` | Muted disabled/cfg-out code ≈ line-number gray light1 |
| `org.rust.CHAR` | `baseAttributes` → `DEFAULT_STRING` | Rust plugin synonym → DEFAULT_STRING |
| `org.rust.COMMA` | `baseAttributes` → `DEFAULT_COMMA` | Rust plugin synonym → DEFAULT_COMMA |
| `org.rust.CONSTANT` | `baseAttributes` → `DEFAULT_CONSTANT` | Rust plugin synonym → DEFAULT_CONSTANT |
| `org.rust.CONST_PARAMETER` | `baseAttributes` → `DEFAULT_CONSTANT` | Rust plugin synonym → DEFAULT_CONSTANT |
| `org.rust.DOC_CODE` | `baseAttributes` → `DEFAULT_DOC_MARKUP` | Rust plugin synonym → DEFAULT_DOC_MARKUP |
| `org.rust.DOC_COMMENT` | `baseAttributes` → `DEFAULT_DOC_COMMENT` | Rust plugin synonym → DEFAULT_DOC_COMMENT |
| `org.rust.DOC_HEADING` | `baseAttributes` → `DEFAULT_DOC_COMMENT_TAG` | Rust plugin synonym → DEFAULT_DOC_COMMENT_TAG |
| `org.rust.DOC_LINK` | `baseAttributes` → `DEFAULT_DOC_COMMENT_TAG_VALUE` | Rust plugin synonym → DEFAULT_DOC_COMMENT_TAG_VALUE |
| `org.rust.DOT` | `baseAttributes` → `DEFAULT_DOT` | Rust plugin synonym → DEFAULT_DOT |
| `org.rust.ENUM` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Rust plugin synonym → DEFAULT_CLASS_NAME |
| `org.rust.ENUM_VARIANT` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Rust plugin synonym → DEFAULT_STATIC_FIELD |
| `org.rust.EOL_COMMENT` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | Rust plugin synonym → DEFAULT_LINE_COMMENT |
| `org.rust.FIELD` | `baseAttributes` → `DEFAULT_INSTANCE_FIELD` | Rust plugin synonym → DEFAULT_INSTANCE_FIELD |
| `org.rust.FORMAT_PARAMETER` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Rust plugin synonym → DEFAULT_VALID_STRING_ESCAPE |
| `org.rust.FORMAT_SPECIFIER` | explicit: `FOREGROUND=ffb900` | Format specs are metadata-like; use DEFAULT_METADATA/accent ffb900 |
| `org.rust.FUNCTION` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | Rust plugin synonym → DEFAULT_FUNCTION_DECLARATION |
| `org.rust.FUNCTION_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Rust plugin synonym → DEFAULT_FUNCTION_CALL |
| `org.rust.GENERATED_ITEM` | explicit: `FOREGROUND=7f7e7d` | Generated/muted code ≈ light2 (folded text family) |
| `org.rust.INVALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Rust plugin synonym → DEFAULT_INVALID_STRING_ESCAPE |
| `org.rust.KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | Rust plugin synonym → DEFAULT_KEYWORD |
| `org.rust.KEYWORD_UNSAFE` | explicit: `FONT_TYPE=1`, `FOREGROUND=ee7762` ⚠QA | Unsafe keyword = keyword color + bold |
| `org.rust.LIFETIME` | explicit: `FONT_TYPE=2`, `FOREGROUND=9896ff` ⚠QA | Lifetimes are type-ish violet (static_field 9896ff) + italic |
| `org.rust.MACRO` | explicit: `FONT_TYPE=1`, `FOREGROUND=92d923` ⚠QA | Macros ≈ function call green + bold (Hiberbee call = 92d923) |
| `org.rust.METHOD` | `baseAttributes` → `DEFAULT_INSTANCE_METHOD` | Rust plugin synonym → DEFAULT_INSTANCE_METHOD |
| `org.rust.METHOD_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Rust plugin synonym → DEFAULT_FUNCTION_CALL |
| `org.rust.MUT_BINDING` | `baseAttributes` → `DEFAULT_IDENTIFIER` | Rust plugin synonym → DEFAULT_IDENTIFIER |
| `org.rust.MUT_PARAMETER` | `baseAttributes` → `DEFAULT_PARAMETER` | Rust plugin synonym → DEFAULT_PARAMETER |
| `org.rust.MUT_STATIC` | `baseAttributes` → `DEFAULT_IDENTIFIER` | Rust plugin synonym → DEFAULT_IDENTIFIER |
| `org.rust.NUMBER` | `baseAttributes` → `DEFAULT_NUMBER` | Rust plugin synonym → DEFAULT_NUMBER |
| `org.rust.OPERATORS` | `baseAttributes` → `DEFAULT_OPERATION_SIGN` | Rust plugin synonym → DEFAULT_OPERATION_SIGN |
| `org.rust.PARAMETER` | `baseAttributes` → `DEFAULT_PARAMETER` | Rust plugin synonym → DEFAULT_PARAMETER |
| `org.rust.PARENTHESES` | `baseAttributes` → `DEFAULT_PARENTHS` | Rust plugin synonym → DEFAULT_PARENTHS |
| `org.rust.Q_OPERATOR` | `baseAttributes` → `DEFAULT_KEYWORD` | Rust plugin synonym → DEFAULT_KEYWORD |
| `org.rust.SELF_PARAMETER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ff638a` | self ≈ predefined/self pink-red (ed005c/ff638a family); use predefined ff638a + italic like PY.SELF |
| `org.rust.SEMICOLON` | `baseAttributes` → `DEFAULT_SEMICOLON` | Rust plugin synonym → DEFAULT_SEMICOLON |
| `org.rust.STATIC` | `baseAttributes` → `DEFAULT_IDENTIFIER` | Rust plugin synonym → DEFAULT_IDENTIFIER |
| `org.rust.STRING` | `baseAttributes` → `DEFAULT_STRING` | Rust plugin synonym → DEFAULT_STRING |
| `org.rust.TRAIT` | `baseAttributes` → `DEFAULT_INTERFACE_NAME` | Rust plugin synonym → DEFAULT_INTERFACE_NAME |
| `org.rust.TYPE_ALIAS` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Rust plugin synonym → DEFAULT_CLASS_NAME |
| `org.rust.UNION` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Rust plugin synonym → DEFAULT_CLASS_NAME |
| `org.rust.UNSAFE_CODE` | explicit: `BACKGROUND=302030` ⚠QA | Unsafe region tint violetBg (302030); softer than redBg so not error-like |
| `org.rust.VALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Rust plugin synonym → DEFAULT_VALID_STRING_ESCAPE |
| `org.rust.VARIABLE` | `baseAttributes` → `DEFAULT_IDENTIFIER` | Rust plugin synonym → DEFAULT_IDENTIFIER |

## Phase 1.2 — HTML

| Key | Recommendation | Rationale |
|---|---|---|
| `HTML_ATTRIBUTE_NAME` | explicit: `FOREGROUND=a9dc76` | Attr names green a9dc76 (align CSS.CLASS_NAME / CUSTOM_KEYWORD2) |
| `HTML_ATTRIBUTE_VALUE` | `baseAttributes` → `DEFAULT_STRING` | Attribute values are strings |
| `HTML_CUSTOM_TAG_NAME` | explicit: `FOREGROUND=409cff` ⚠QA | Custom elements ≈ interface blue 409cff (distinct from native tags) |
| `HTML_ENTITY_REFERENCE` | `baseAttributes` → `DEFAULT_ENTITY` | HTML entities → DEFAULT_ENTITY |
| `HTML_TAG` | explicit: `FOREGROUND=ff6188` | HTML tags use tag pink ff6188 (CSS.TAG_NAME / DEFAULT_TAG) |
| `MATCHED_TAG_NAME` | explicit: `BACKGROUND=424140` ⚠QA | Matching tag pair subtle fill dark8 (424140) |

## Phase 1.3 — XML

| Key | Recommendation | Rationale |
|---|---|---|
| `XML_ATTRIBUTE_NAME` | explicit: `FOREGROUND=bfbebd` | XML attrs secondary light6 (bfbebd); less loud than HTML attrs |
| `XML_CUSTOM_TAG_NAME` | explicit: `FOREGROUND=409cff` | Custom XML tags ≈ interface blue |
| `XML_ENTITY_REFERENCE` | `baseAttributes` → `DEFAULT_ENTITY` | XML entities → DEFAULT_ENTITY |
| `XML_NS_PREFIX` | explicit: `FOREGROUND=57d1eb` | Namespace prefix cyan class-like 57d1eb |
| `XML_TAG` | explicit: `FOREGROUND=a9dc76` | Match existing XML_TAG_NAME a9dc76 |

## Phase 1.4 — PHP

| Key | Recommendation | Rationale |
|---|---|---|
| `PHP_CONSTANT` | `baseAttributes` → `DEFAULT_CONSTANT` | PHP constants → DEFAULT_CONSTANT |
| `PHP_HEREDOC_CONTENT` | explicit: `FOREGROUND=ccbfaf` | Heredoc body muted doc-like ccbfaf (align PHP_HEREDOC_ID family) |
| `PHP_PARAMETER` | `baseAttributes` → `DEFAULT_PARAMETER` | PHP params → DEFAULT_PARAMETER |
| `PHP_SCRIPTING_BACKGROUND` | explicit: `BACKGROUND=222120` ⚠QA | PHP island background dark4 (222120) subtle lift; keep existing EFFECT_TYPE if any |
| `PHP_VAR` | `baseAttributes` → `DEFAULT_LOCAL_VARIABLE` | PHP vars → DEFAULT_LOCAL_VARIABLE (pin empty → identifier) |

## Phase 1.5 — TypeScript

| Key | Recommendation | Rationale |
|---|---|---|
| `TS.GLOBAL_VARIABLE` | `baseAttributes` → `DEFAULT_GLOBAL_VARIABLE` | TS globals → DEFAULT_GLOBAL_VARIABLE |
| `TS_AUDIT_FOLLOWUP` | _process:_ Process: audit WebStorm TS.* tree after IDE update; not a color key | Process: audit WebStorm TS.* tree after IDE update; not a color key |

## Phase 1.7 — JavaScript

| Key | Recommendation | Rationale |
|---|---|---|
| `JS.EXPORTED.VARIABLE` | `baseAttributes` → `DEFAULT_GLOBAL_VARIABLE` | Exported vars ≈ global |
| `JS.GLOBAL_FUNCTION` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | JS global fn → function decl |
| `JS.GLOBAL_VARIABLE` | `baseAttributes` → `DEFAULT_GLOBAL_VARIABLE` | JS global var → global variable |
| `JS.INSTANCE_MEMBER_FUNCTION` | `baseAttributes` → `DEFAULT_INSTANCE_METHOD` | JS methods → instance method |
| `JS.INVALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | JS bad escapes → invalid escape |
| `JS.JSX_CLIENT_COMPONENT` | explicit: `FOREGROUND=9896ff` ⚠QA | Client components distinct violet 9896ff (not string green) |
| `JS.KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | JS keywords → DEFAULT_KEYWORD |
| `JS.LOCAL_VARIABLE` | `baseAttributes` → `DEFAULT_LOCAL_VARIABLE` | JS locals → local variable pin |
| `JS.VALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | JS escapes → valid escape |

## Phase 2.1 — RegExp

| Key | Recommendation | Rationale |
|---|---|---|
| `REGEXP.BRACES` | `baseAttributes` → `DEFAULT_BRACES` | Regexp braces → braces |
| `REGEXP.BRACKETS` | `baseAttributes` → `DEFAULT_BRACKETS` | Regexp brackets → brackets |
| `REGEXP.COMMA` | `baseAttributes` → `DEFAULT_COMMA` | Regexp comma → comma |
| `REGEXP.ESC_CHARACTER` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Regexp escapes → valid escape |
| `REGEXP.INVALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Regexp invalid escape |
| `REGEXP.META` | `baseAttributes` → `DEFAULT_KEYWORD` | Regexp meta → keyword |
| `REGEXP.PARENTHS` | `baseAttributes` → `DEFAULT_PARENTHS` | Regexp parens → parens |
| `REGEXP.QUOTE_CHARACTER` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Regexp quotes → escape family |
| `REGEXP.REDUNDANT_ESCAPE` | explicit: `FONT_TYPE=1`, `FOREGROUND=6f6e6d` | Redundant escape muted light1 + bold |

## Phase 2.2 — CSS/SASS

| Key | Recommendation | Rationale |
|---|---|---|
| `CSS.HASH` | explicit: `FOREGROUND=fd971f` | Color hashes = CSS.COLOR orange fd971f |
| `CSS.IDENT` | explicit: `FOREGROUND=a9dc76` | CSS idents ≈ class names a9dc76 |
| `CSS.PROPERTY_VALUE` | explicit: `FOREGROUND=ee9b70` | Property values warm parameter ee9b70 |
| `SASS_COMMENT` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | SASS comments → line comment (no CSS.COMMENT key in HB) |
| `SASS_IDENTIFIER` | `pin_empty` (inherit) | Pin empty; inherit / DEFAULT_IDENTIFIER |
| `SASS_VARIABLE` | `baseAttributes` → `DEFAULT_INSTANCE_FIELD` | SASS vars → instance field |

## Phase 2.3 — Markdown

| Key | Recommendation | Rationale |
|---|---|---|
| `MARKDOWN_AUTO_LINK` | explicit: `EFFECT_COLOR=f65f87`, `EFFECT_TYPE=1`, `FOREGROUND=f65f87` | Mirror existing MARKDOWN.AUTO_LINK |
| `MARKDOWN_IMAGE` | explicit: `FOREGROUND=f65f87` | Mirror MARKDOWN.IMAGE f65f87 |
| `MARKDOWN_LINK_TEXT` | explicit: `EFFECT_TYPE=1`, `FOREGROUND=78dce8` | Link text cyan 78dce8 like EXPLICIT_LINK |

## Phase 2.4 — Custom file types

| Key | Recommendation | Rationale |
|---|---|---|
| `CUSTOM_INVALID_STRING_ESCAPE_ATTRIBUTES` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Custom invalid escapes |
| `CUSTOM_KEYWORD1_ATTRIBUTES` | explicit: `FOREGROUND=ee7762` | KW1 = keyword coral ee7762 (KW2 green, KW3 string, KW4 violet already) |
| `CUSTOM_STRING_ATTRIBUTES` | `baseAttributes` → `DEFAULT_STRING` | Custom strings → string |
| `CUSTOM_VALID_STRING_ESCAPE_ATTRIBUTES` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Custom escapes → valid |

## Phase 2.5 — JSP/Qute

| Key | Recommendation | Rationale |
|---|---|---|
| `JSP_ATTRIBUTE_NAME` | `baseAttributes` → `DEFAULT_ATTRIBUTE` | JSP attrs → DEFAULT_ATTRIBUTE |
| `JSP_DIRECTIVE_BACKGROUND` | explicit: `BACKGROUND=222120` | Directive region dark4 |
| `JSP_DIRECTIVE_NAME` | `baseAttributes` → `DEFAULT_METADATA` | JSP directives ≈ metadata/annotations |
| `JSP_SCRIPTING_BACKGROUND` | explicit: `BACKGROUND=222120` | Scripting island dark4 like PHP scripting |
| `QUTE_BACKGROUND` | explicit: `BACKGROUND=272625` | Qute injection dark5 gutter-adjacent |

## Phase 3.1 — Editor colors

| Key | Recommendation | Rationale |
|---|---|---|
| `ANNOTATIONS_LAST_COMMIT_COLOR` | color value `dfdedd` (light8) | Last-commit author text ≈ light8 near caret/annotations readability |
| `DOC_COMMENT_GUIDE` | color value `424140` (dark8) | Doc vertical guide subtle dark8 |
| `DOC_COMMENT_LINK` | color value `409cff` (blue) | Doc links = blue 409cff |
| `FILESTATUS_IDEA_SVN_FILESTATUS_OBSTRUCTED` | color value `ffd866` (— FILESTATUS_UNKNOWN) | Obstructed ≈ unknown yellow ffd866 |
| `FILESTATUS_IDEA_SVN_REPLACED` | color value `a9dc76` (— FILESTATUS_ADDED) | Replaced ≈ added green |
| `FILESTATUS_RENAMED` | color value `78dce8` (— FILESTATUS_MODIFIED) | Renamed ≈ modified cyan 78dce8 |
| `FILESTATUS_addedOutside` | color value `a9dc76` (— FILESTATUS_ADDED) | Added-outside ≈ added green a9dc76 |
| `FILESTATUS_changelistConflict` | color value `f65f87` (— FILESTATUS_CHANGELIST_CONFLICT) | Alias of CHANGELIST_CONFLICT f65f87; add if camelCase still read |
| `FILESTATUS_modifiedOutside` | color value `78dce8` (— FILESTATUS_MODIFIED_OUTSIDE) | Alias of MODIFIED_OUTSIDE 78dce8 |
| `FOLDED_TEXT_BORDER_COLOR` | color value `424140` (dark8) | Fold border dark8 |
| `IGNORED_DELETED_LINES_BORDER_COLOR` | color value `727072` (— FILESTATUS_DELETED) | Ignored-deleted border muted 727072 |
| `IGNORED_MODIFIED_LINES_BORDER_COLOR` | color value `78dce8` (— FILESTATUS_MODIFIED) | Ignored-modified border cyan 78dce8 (parallel to modified) |
| `INLINE_REFACTORING_SETTINGS_DEFAULT` | color value `424140` (dark8) | Inline refactor chrome dark8 |
| `INLINE_REFACTORING_SETTINGS_FOCUSED` | color value `525150` (dark10) | Focused refactor control dark10 |
| `INLINE_REFACTORING_SETTINGS_HOVERED` | color value `474645` (dark9) | Hover refactor control dark9 |
| `NEXT_EDIT.DIFF_AFTER_BACKGROUND` | color value `203020` (greenBg) ⚠QA | Next Edit insertion tint greenBg |
| `NEXT_EDIT.EDIT_RANGE.GUTTER_BACKGROUND` | color value `302030` (violetBg) ⚠QA | Next Edit range gutter violetBg |
| `NEXT_EDIT.EDIT_RANGE.LINE_BACKGROUND` | color value `171615` (dark3) ⚠QA | Next Edit line wash dark3 (deeper than gutter) |
| `NEXT_EDIT.INSIGHT_BACKGROUND` | color value `302030` (violetBg) ⚠QA | Insight panel violetBg |
| `NEXT_EDIT.REMOVAL_BACKGROUND` | color value `320f0f` (redBg) ⚠QA | Removal suggestion redBg |
| `ScrollBar.Mac.hoverThumbColor` | color value `525150` (dark10) ⚠QA | Hover Mac thumb dark10 (matches ui.ScrollBar.hoverThumbColor token) |
| `ScrollBar.Mac.thumbColor` | color value `424140` (dark8) ⚠QA | Idle Mac thumb dark8 solid (scheme may accept 6-digit); optional alpha via yellowDark pattern only if needed |

## Phase 3.2 — Doc attributes

| Key | Recommendation | Rationale |
|---|---|---|
| `DOC_CODE_BLOCK` | explicit: `BACKGROUND=222120`, `EFFECT_COLOR=424140`, `FOREGROUND=dfdedd` ⚠QA | Quick Doc code block: light text on dark4, border dark8 |
| `DOC_CODE_INLINE` | explicit: `BACKGROUND=373635`, `FOREGROUND=dfdedd` | Inline code chip light8 on dark7 |
| `DOC_TIPS_SHORTCUT` | explicit: `EFFECT_COLOR=6f6e6d`, `FOREGROUND=dfdedd` | Shortcut tips light8 with light1 outline |

## Phase 3.2 — Inlays

| Key | Recommendation | Rationale |
|---|---|---|
| `INLAY_DEFAULT` | explicit: `BACKGROUND=424140`, `FOREGROUND=7f7e7d` ⚠QA | Default inlay = hint gray on dark8 |
| `INLAY_TEXT_WITHOUT_BACKGROUND` | explicit: `FOREGROUND=7f7e7d` | Bare inlay text light2 |

## Phase 4.1 — Go

| Key | Recommendation | Rationale |
|---|---|---|
| `GO_BAD_TOKEN` | explicit: `EFFECT_COLOR=f25022`, `EFFECT_TYPE=2` | Bad token wave error red f25022 |
| `GO_BLOCK_COMMENT` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | Go comments |
| `GO_BUILTIN_CONSTANT` | `baseAttributes` → `DEFAULT_CONSTANT` | Go builtin const/var → constant |
| `GO_BUILTIN_FUNCTION` | explicit: `FOREGROUND=ee9b70` | Builtin fn names warm parameter (distinct from calls) |
| `GO_BUILTIN_FUNCTION_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Go calls → function call |
| `GO_BUILTIN_TYPE_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_BUILTIN_VARIABLE` | `baseAttributes` → `DEFAULT_CONSTANT` | Go builtin const/var → constant |
| `GO_COLON` | explicit: `EFFECT_TYPE=5`, `FOREGROUND=dfdedd` | Colon light8 (no dark bg — keep FG only) |
| `GO_COMMA` | `pin_empty` (inherit) | Pin empty punctuation |
| `GO_COMMENT_KEYWORD` | explicit: `EFFECT_COLOR=ffb900`, `EFFECT_TYPE=1`, `FOREGROUND=ffb900` | Comment keywords like doc tags |
| `GO_COMMENT_REFERENCE` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | Go comments |
| `GO_DOT` | `pin_empty` (inherit) | Pin empty punctuation |
| `GO_EXPORTED_FUNCTION_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Go calls → function call |
| `GO_EXPORTED_INTERFACE_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_EXPORTED_STRUCT_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_FUNCTION_PARAMETER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ee9b70` | Params/receivers/local members parameter + italic |
| `GO_IDENTIFIER` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_INVALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Go invalid escape |
| `GO_KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | Go keyword |
| `GO_LABEL` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_LOCAL_FUNCTION_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Go calls → function call |
| `GO_LOCAL_INTERFACE_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_LOCAL_STRUCT_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_METHOD_RECEIVER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ee9b70` | Params/receivers/local members parameter + italic |
| `GO_NUMBER` | `baseAttributes` → `DEFAULT_NUMBER` | Go number |
| `GO_OPERATOR` | `pin_empty` (inherit) | Pin empty punctuation |
| `GO_PACKAGE` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Package path ≈ static field violet |
| `GO_PACKAGE_EXPORTED_INTERFACE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_PACKAGE_EXPORTED_STRUCT` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_PACKAGE_EXPORTED_VARIABLE` | `pin_empty` (inherit) | Pin empty exported member |
| `GO_PACKAGE_EXPORTED_VARIABLE_CALL` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Package path ≈ static field violet |
| `GO_PACKAGE_LOCAL_INTERFACE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_PACKAGE_LOCAL_STRUCT` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_PACKAGE_LOCAL_VARIABLE_CALL` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Package path ≈ static field violet |
| `GO_REASSIGNMENT_IN_SHORT_VAR_DECLARATION` | explicit: `EFFECT_COLOR=8e8cb7`, `EFFECT_TYPE=1`, `FOREGROUND=8e8cb7` | Reassignment underline like reassigned local |
| `GO_SEMICOLON` | `pin_empty` (inherit) | Pin empty punctuation |
| `GO_SHADOWING_VARIABLE` | explicit: `FOREGROUND=dfdedd` | Shadowing var slightly bright light8 |
| `GO_STRING` | `baseAttributes` → `DEFAULT_STRING` | Go string |
| `GO_STRUCT_EXPORTED_MEMBER` | `pin_empty` (inherit) | Pin empty exported member |
| `GO_STRUCT_LOCAL_MEMBER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ee9b70` | Params/receivers/local members parameter + italic |
| `GO_TYPE_REFERENCE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_TYPE_SPECIFICATION` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Go types/structs/interfaces → class cyan |
| `GO_VALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Go valid escape |

## Phase 4.2 — Python

| Key | Recommendation | Rationale |
|---|---|---|
| `PY.BRACES` | `pin_empty` (inherit) | Pin empty Python punctuation |
| `PY.BRACKETS` | `pin_empty` (inherit) | Pin empty Python punctuation |
| `PY.BUILTIN_NAME` | `baseAttributes` → `DEFAULT_PREDEFINED_SYMBOL` | Builtins → predefined |
| `PY.CLASS_DEFINITION` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Python → DEFAULT_CLASS_NAME |
| `PY.COMMA` | `pin_empty` (inherit) | Pin empty Python punctuation |
| `PY.DOC_COMMENT` | `baseAttributes` → `DEFAULT_DOC_COMMENT` | Python → DEFAULT_DOC_COMMENT |
| `PY.DOC_COMMENT_TAG` | `baseAttributes` → `DEFAULT_DOC_COMMENT_TAG` | Python → DEFAULT_DOC_COMMENT_TAG |
| `PY.DOT` | `pin_empty` (inherit) | Pin empty Python punctuation |
| `PY.FSTRING_FRAGMENT_BRACES` | explicit: `FOREGROUND=ee9b70` | f-string braces warm parameter |
| `PY.FSTRING_FRAGMENT_COLON` | explicit: `FOREGROUND=ee9b70` | f-string format colon parameter |
| `PY.FUNCTION_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Python → DEFAULT_FUNCTION_CALL |
| `PY.KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | Python → DEFAULT_KEYWORD |
| `PY.LINE_COMMENT` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | Python → DEFAULT_LINE_COMMENT |
| `PY.METHOD_CALL` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Python → DEFAULT_FUNCTION_CALL |
| `PY.NUMBER` | `baseAttributes` → `DEFAULT_NUMBER` | Python → DEFAULT_NUMBER |
| `PY.OPERATION_SIGN` | `baseAttributes` → `DEFAULT_OPERATION_SIGN` | Python → DEFAULT_OPERATION_SIGN |
| `PY.PARENTHS` | `pin_empty` (inherit) | Pin empty Python punctuation |
| `PY.PREDEFINED_DEFINITION` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Python → DEFAULT_CLASS_NAME |
| `PY.PREDEFINED_USAGE` | `baseAttributes` → `DEFAULT_CLASS_REFERENCE` | Python → DEFAULT_CLASS_REFERENCE |
| `PY.SELF_PARAMETER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ed005c` | Keep existing ed005c; add italic FONT_TYPE=2 only |
| `PY.STRING.U` | explicit: `FOREGROUND=a9dc76` | Match existing PY.STRING a9dc76 (Hiberbee Python strings are green) |
| `Static method access` | explicit: `FONT_TYPE=2`, `FOREGROUND=9896ff` | Python static method access |
| `Static property reference ID` | explicit: `FONT_TYPE=2`, `FOREGROUND=9896ff` | Python static property |
| `Unresolved reference access` | explicit: `EFFECT_COLOR=7f7e7d`, `EFFECT_TYPE=5`, `FOREGROUND=6f6e6d` | Unresolved muted + dotted |

## Phase 4.3 — Ruby/HAML/RHTML

| Key | Recommendation | Rationale |
|---|---|---|
| `HAML_COMMENT` | `baseAttributes` → `DEFAULT_DOC_COMMENT` | Ruby/HAML → DEFAULT_DOC_COMMENT |
| `HAML_ID` | explicit: `FOREGROUND=92d923` | HAML id green |
| `HAML_RUBY_CODE` | `baseAttributes` → `INJECTED_LANGUAGE_FRAGMENT` | Ruby/HAML → INJECTED_LANGUAGE_FRAGMENT |
| `RHTML_COMMENT_ID` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | RHTML comment (HTML_COMMENT may not exist; use line comment) |
| `RHTML_EXPRESSION_END_ID` | `baseAttributes` → `XML_TAG_NAME` | RHTML_EXPRESSION_END_ID → XML_TAG_NAME |
| `RHTML_SCRIPTLET_END_ID` | `baseAttributes` → `XML_TAG_NAME` | RHTML_SCRIPTLET_END_ID → XML_TAG_NAME |
| `RHTML_SCRIPTLET_START_ID` | `baseAttributes` → `XML_TAG_NAME` | RHTML_SCRIPTLET_START_ID → XML_TAG_NAME |
| `RUBY_BAD_CHARACTER` | explicit: `EFFECT_COLOR=f65f87`, `EFFECT_TYPE=2` | Bad char wave |
| `RUBY_COMMENT` | `baseAttributes` → `DEFAULT_LINE_COMMENT` | Ruby comment |
| `RUBY_CONSTANT` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Ruby constant ≈ class |
| `RUBY_CONSTANT_DECLARATION` | `baseAttributes` → `DEFAULT_CONSTANT` | Ruby const decl → constant |
| `RUBY_CVAR` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Class var → static field |
| `RUBY_ESCAPE_SEQUENCE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Ruby escape |
| `RUBY_GVAR` | `baseAttributes` → `DEFAULT_GLOBAL_VARIABLE` | Global var |
| `RUBY_HASH_ASSOC` | explicit: `FOREGROUND=dfdedd` | Hash rocket light8 |
| `RUBY_HEREDOC_CONTENT` | explicit: `FOREGROUND=ffd866` | Heredoc content string yellow (RUBY_HEREDOC_ID already muted) |
| `RUBY_INTERPOLATED_STRING` | `baseAttributes` → `DEFAULT_STRING` | Interpolated string |
| `RUBY_INVALID_ESCAPE_SEQUENCE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Ruby bad escape |
| `RUBY_IVAR` | `baseAttributes` → `DEFAULT_INSTANCE_FIELD` | Instance var → field |
| `RUBY_LINE_CONTINUATION` | `pin_empty` (inherit) | Pin empty |
| `RUBY_LOCAL_VAR_ID` | `baseAttributes` → `DEFAULT_LOCAL_VARIABLE` | Ruby/HAML → DEFAULT_LOCAL_VARIABLE |
| `RUBY_METHOD_NAME` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | Method name → function decl |
| `RUBY_NUMBER` | `baseAttributes` → `DEFAULT_NUMBER` | Ruby number |
| `RUBY_PARAMETER_ID` | `baseAttributes` → `DEFAULT_PARAMETER` | Ruby/HAML → DEFAULT_PARAMETER |
| `RUBY_REGEXP` | explicit: `BACKGROUND=222120` | Regexp region dark4 |
| `RUBY_SYMBOL` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Symbol ≈ static field violet |

## Phase 4.4 — Kotlin

| Key | Recommendation | Rationale |
|---|---|---|
| `KOTLIN_ARROW` | `pin_empty` (inherit) | Pin empty arrow |
| `KOTLIN_ENUM_ENTRY` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Enum entry → static field |
| `KOTLIN_LABEL` | explicit: `FOREGROUND=57d1eb` | Labels cyan class-like 57d1eb |
| `KOTLIN_PACKAGE_PROPERTY` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Package property → static field |

## Phase 5.1 — JSON

| Key | Recommendation | Rationale |
|---|---|---|
| `JSON.KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | JSON true/false/null → keyword |
| `JSON.NUMBER` | `baseAttributes` → `DEFAULT_NUMBER` | JSON number |
| `JSON.PROPERTY_KEY` | explicit: `FOREGROUND=9380ff` | Keys violet 9380ff like YAML_SCALAR_KEY |
| `JSON.STRING` | `baseAttributes` → `DEFAULT_STRING` | JSON string |
| `JSON.VALID_ESCAPE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | JSON escape |

## Phase 5.1 — YAML

| Key | Recommendation | Rationale |
|---|---|---|
| `YAML_ANCHOR` | explicit: `FOREGROUND=ee9b70` | YAML anchors parameter warm |
| `YAML_TEXT` | `baseAttributes` → `DEFAULT_STRING` | YAML text ≈ string |

## Phase 5.1 — TOML

| Key | Recommendation | Rationale |
|---|---|---|
| `org.toml.DATE` | explicit: `FOREGROUND=ee9b70` | TOML dates parameter |
| `org.toml.KEY` | explicit: `FOREGROUND=57d1eb` | TOML keys cyan class |

## Phase 5.1 — Properties

| Key | Recommendation | Rationale |
|---|---|---|
| `PROPERTIES.INVALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_INVALID_STRING_ESCAPE` | Properties invalid escape |
| `PROPERTIES.VALID_STRING_ESCAPE` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Properties valid escape |

## Phase 5.2 — Console

| Key | Recommendation | Rationale |
|---|---|---|
| `CONSOLE_SELECTED_PARAMETER` | explicit: `BACKGROUND=222120`, `FOREGROUND=9896ff` | Selected console param |

## Phase 5.2 — Logcat

| Key | Recommendation | Rationale |
|---|---|---|
| `LOGCAT_ASSERT_OUTPUT` | explicit: `FOREGROUND=9380ff` | Mirror LOGCAT_V2_LEVEL_ASSERT |
| `LOGCAT_DEBUG_OUTPUT` | explicit: `FOREGROUND=57d1eb` | Mirror LOGCAT_V2_LEVEL_DEBUG |
| `LOGCAT_ERROR_OUTPUT` | explicit: `FOREGROUND=f25022` | Mirror LOGCAT_V2_LEVEL_ERROR |
| `LOGCAT_INFO_OUTPUT` | explicit: `FOREGROUND=92d923` | Mirror LOGCAT_V2_LEVEL_INFO |
| `LOGCAT_VERBOSE_OUTPUT` | explicit: `FOREGROUND=acacac` | Mirror LOGCAT_V2_LEVEL_VERBOSE |
| `LOGCAT_WARNING_OUTPUT` | explicit: `FOREGROUND=ffb900` | Mirror LOGCAT_V2_LEVEL_WARNING |

## Phase 7 — Partial upgrades

| Key | Recommendation | Rationale |
|---|---|---|
| `ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES` | explicit: `EFFECT_TYPE=1`, `FOREGROUND=b7c3` | Add underline EFFECT_TYPE |
| `BAD_CHARACTER` | explicit: `EFFECT_COLOR=f65f87`, `EFFECT_TYPE=2`, `FOREGROUND=f65f87` | Add FG matching wave |
| `BOOKMARKS_ATTRIBUTES` | explicit: `BACKGROUND=222120`, `ERROR_STRIPE_COLOR=f5d277`, `FOREGROUND=bfbebd` | Bookmark stripe yellowLight |
| `BREAKPOINT_ATTRIBUTES` | explicit: `BACKGROUND=320a19`, `ERROR_STRIPE_COLOR=f65f87` | Breakpoint stripe pink-red |
| `CODE_LENS_BORDER_COLOR` | explicit: `BACKGROUND=525150`, `EFFECT_COLOR=525150` ⚠QA | Set both BG and EFFECT_COLOR to dark10 for platform variance |
| `CONSOLE_RANGE_TO_EXECUTE` | explicit: `EFFECT_COLOR=92d923` | Range-to-execute green outline |
| `CONSOLE_USER_INPUT` | explicit: `FONT_TYPE=2`, `FOREGROUND=b4da82` | User input italic |
| `CSS.IMPORTANT` | explicit: `FONT_TYPE=1`, `FOREGROUND=f25022` | !important bold |
| `CTRL_CLICKABLE` | explicit: `EFFECT_COLOR=409cff`, `EFFECT_TYPE=1`, `FOREGROUND=409cff` | Hyperlink blue underline |
| `DEBUGGER_INLINED_VALUES_EXECUTION_LINE` | explicit: `FONT_TYPE=2`, `FOREGROUND=ff638a` | Debugger inline italic |
| `DEFAULT_CONSTANT` | explicit: `FONT_TYPE=2`, `FOREGROUND=f25022` | Constants italic optional |
| `DEFAULT_DOC_COMMENT` | explicit: `FONT_TYPE=2`, `FOREGROUND=ccbfaf` | Doc comments italic optional |
| `DEFAULT_DOC_COMMENT_TAG_VALUE` | explicit: `FONT_TYPE=2`, `FOREGROUND=ee9b70` | Doc tag value italic |
| `DEFAULT_GLOBAL_VARIABLE` | explicit: `EFFECT_TYPE=5`, `FONT_TYPE=1`, `FOREGROUND=ff8c00` | Global bold optional |
| `DEFAULT_INVALID_STRING_ESCAPE` | explicit: `EFFECT_COLOR=f25022`, `EFFECT_TYPE=2`, `FOREGROUND=ee9b70` | Add FG parameter warm |
| `DEFAULT_METADATA` | explicit: `FONT_TYPE=2`, `FOREGROUND=ffb900` | Metadata italic optional |
| `DEFAULT_PARAMETER` | explicit: `FONT_TYPE=2`, `FOREGROUND=ee9b70` | Params italic optional |
| `DEFAULT_REASSIGNED_LOCAL_VARIABLE` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1`, `FOREGROUND=8e8cb7` | Reassigned local underline light3 |
| `DEFAULT_REASSIGNED_PARAMETER` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1`, `FONT_TYPE=2`, `FOREGROUND=edc777` | Keep FG; add underline |
| `DEFAULT_STATIC_FIELD` | explicit: `FONT_TYPE=2`, `FOREGROUND=9896ff` | Static fields italic optional |
| `DEFAULT_STATIC_METHOD` | explicit: `FONT_TYPE=2`, `FOREGROUND=b7e66e` | Static methods italic optional |
| `DEFAULT_TEMPLATE_LANGUAGE_COLOR` | explicit: `BACKGROUND=272625`, `EFFECT_TYPE=5` | Template language region dark5 |
| `DELETED_TEXT_ATTRIBUTES` | explicit: `BACKGROUND=261b1a`, `EFFECT_COLOR=525150`, `EFFECT_TYPE=3`, `FOREGROUND=afaead` | Deleted text use diff deleted bg |
| `FOLDED_TEXT_ATTRIBUTES` | explicit: `BACKGROUND=424140`, `FOREGROUND=7f7e7d` | Folded region dark8 bg |
| `HAML_TAG` | explicit: `BACKGROUND=171615`, `EFFECT_TYPE=5`, `FOREGROUND=ff6188` | HAML tag dark3 |
| `IDENTIFIER_UNDER_CARET_ATTRIBUTES` | explicit: `BACKGROUND=203020`, `EFFECT_COLOR=78dce8`, `EFFECT_TYPE=1`, `ERROR_STRIPE_COLOR=92d923` ⚠QA | Read occurrences: greenBg + green stripe; keep cyan effect |
| `IMPLICIT_ANONYMOUS_CLASS_PARAMETER_ATTRIBUTES` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1`, `FOREGROUND=9380ff` | Underline implicit param |
| `INACTIVE_HYPERLINK_ATTRIBUTES` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1`, `FOREGROUND=9896ff` | Inactive link violet |
| `INJECTED_LANGUAGE_FRAGMENT` | explicit: `BACKGROUND=253047`, `EFFECT_COLOR=525150` ⚠QA | Injection host blueBg wash |
| `INLINE_PARAMETER_HINT` | explicit: `BACKGROUND=424140`, `FOREGROUND=969696` | Param hint chip dark8 |
| `INLINE_PARAMETER_HINT_CURRENT` | explicit: `BACKGROUND=253047`, `FOREGROUND=fff1c9` ⚠QA | Current param blueBg |
| `INLINE_PARAMETER_HINT_HIGHLIGHTED` | explicit: `BACKGROUND=525150`, `FOREGROUND=fcfcfa` | Highlighted param dark10 |
| `KOTLIN_MUTABLE_VARIABLE` | explicit: `EFFECT_COLOR=8f8e8d`, `EFFECT_TYPE=1` | Mutable var underline light3 |
| `KOTLIN_SMART_CAST_RECEIVER` | explicit: `BACKGROUND=203020`, `FOREGROUND=b7e66e` ⚠QA | Smart-cast receiver greenBg |
| `KOTLIN_SMART_CAST_VALUE` | explicit: `BACKGROUND=302030`, `FOREGROUND=c9bfff` ⚠QA | Smart-cast value violetBg |
| `KOTLIN_SMART_CONSTANT` | explicit: `BACKGROUND=320f0f`, `FOREGROUND=ed005c` ⚠QA | Smart-cast const redBg light |
| `LINE_FULL_COVERAGE` | explicit: `EFFECT_TYPE=2`, `FONT_TYPE=1`, `FOREGROUND=9adf66` | Coverage bold |
| `LINE_NONE_COVERAGE` | explicit: `EFFECT_TYPE=3`, `FONT_TYPE=1`, `FOREGROUND=f9d878` | Coverage bold |
| `LINE_PARTIAL_COVERAGE` | explicit: `FONT_TYPE=1`, `FOREGROUND=ef9c70` | Coverage bold |
| `MATCHED_BRACE_ATTRIBUTES` | explicit: `BACKGROUND=3b514d`, `FONT_TYPE=1`, `FOREGROUND=ffb900` | Matched brace accent FG |
| `NOT_TOP_FRAME_ATTRIBUTES` | explicit: `BACKGROUND=253047`, `FOREGROUND=f7cd46` | Non-top frame blueBg |
| `PROPERTIES.KEY` | explicit: `EFFECT_TYPE=1`, `FOREGROUND=9380ff` | Add underline on keys |
| `REGEXP.CHAR_CLASS` | explicit: `EFFECT_TYPE=5`, `FONT_TYPE=1`, `FOREGROUND=ed005c` | Char class bold |
| `SEARCH_RESULT_ATTRIBUTES` | explicit: `BACKGROUND=203020`, `EFFECT_COLOR=525150`, `ERROR_STRIPE_COLOR=92d923`, `FONT_TYPE=1`, `FOREGROUND=ffffff` ⚠QA | Search hits greenBg family |
| `STATIC_FINAL_FIELD_ATTRIBUTES` | explicit: `EFFECT_TYPE=1`, `FOREGROUND=ff8c00` | Final static underline |
| `Scala Immutable Collection` | explicit: `EFFECT_TYPE=5`, `FOREGROUND=b7c3` | Dotted underline |
| `Scala Mutable Collection` | explicit: `EFFECT_TYPE=5`, `FOREGROUND=78dce8` | Dotted underline |
| `TEXT_SEARCH_RESULT_ATTRIBUTES` | explicit: `BACKGROUND=253047`, `EFFECT_COLOR=424140`, `ERROR_STRIPE_COLOR=409cff` ⚠QA | Text search blueBg |
| `TEXT_STYLE_ERROR` | explicit: `EFFECT_COLOR=f25022`, `EFFECT_TYPE=5` | Error style dotted red |
| `TEXT_STYLE_WARNING` | explicit: `EFFECT_COLOR=ffb900`, `EFFECT_TYPE=5` | Warning style dotted accent |
| `TODO_DEFAULT_ATTRIBUTES` | explicit: `ERROR_STRIPE_COLOR=92d923`, `FONT_TYPE=2`, `FOREGROUND=ffbdce` | TODO italic + green stripe |
| `UNMATCHED_BRACE_ATTRIBUTES` | explicit: `EFFECT_COLOR=ed005c`, `FONT_TYPE=1`, `FOREGROUND=f65f87` | Add FG pink-red |
| `WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES` | explicit: `BACKGROUND=403018`, `EFFECT_COLOR=afaead`, `EFFECT_TYPE=1`, `ERROR_STRIPE_COLOR=ee9b70` ⚠QA | Write occurrences: orangeBg tint |
| `WRITE_SEARCH_RESULT_ATTRIBUTES` | explicit: `BACKGROUND=302030`, `ERROR_STRIPE_COLOR=f65f87` ⚠QA | Write search violetBg |
| `WRONG_REFERENCES_ATTRIBUTES` | explicit: `EFFECT_COLOR=e81123`, `EFFECT_TYPE=2`, `ERROR_STRIPE_COLOR=ed005c`, `FOREGROUND=f65f87` | Add FG |
| `YAML_SCALAR_LIST` | explicit: `BACKGROUND=171615`, `EFFECT_TYPE=5`, `FOREGROUND=ccbfaf` | Block scalar dark3 wash |
| `YAML_SCALAR_VALUE` | explicit: `BACKGROUND=171615`, `EFFECT_TYPE=5`, `FOREGROUND=ccbfaf` | Scalar value dark3 wash |

## Phase 8 — Theme JSON

| Key | Recommendation | Rationale |
|---|---|---|
| `ScrollBar.thumbColor` | theme.json: `{"ui.ScrollBar.thumbColor": "dark8"}` ⚠QA | UI thumb dark8 to pair with hoverThumbColor dark10 |
| `ScrollBar_Mac_ALIGN` | _process:_ Align Mac scheme thumbs with theme_json ScrollBar tokens (dark8/dark10) | Align Mac scheme thumbs with theme_json ScrollBar tokens (dark8/dark10) |

## Remaining families (compact)

### C# (3)

| Key | Recommendation | Rationale |
|---|---|---|
| `CSHARP_AUDIT_FOLLOWUP` | _process:_ Process: audit Rider ReSharper keys; Hiberbee already has 28 | Process: audit Rider ReSharper keys; Hiberbee already has 28 |
| `CSHARP_BASEATTR_WHERE_SYNONYM` | _process:_ Where ReSharper key is synonym, prefer baseAttributes to DEFAULT_* | Where ReSharper key is synonym, prefer baseAttributes to DEFAULT_* |
| `CSHARP_KEEP_EXISTING` | _process:_ Keep existing ReSharper.* colors unchanged | Keep existing ReSharper.* colors unchanged |

### CodeQL (3)

| Key | Recommendation | Rationale |
|---|---|---|
| `QL_ATTRIBUTE` | `pin_empty` (inherit) | Pin empty CodeQL attribute |
| `QL_FUNCTION` | `baseAttributes` → `DEFAULT_CLASS_NAME` | CodeQL function |
| `QL_PARAMETER` | explicit: `FOREGROUND=dfdedd` | CodeQL param light8 |

### Grid (1)

| Key | Recommendation | Rationale |
|---|---|---|
| `GRID_ERROR_VALUE` | explicit: `EFFECT_COLOR=f65f87`, `EFFECT_TYPE=2`, `ERROR_STRIPE_COLOR=f25022` | Grid error wave |

### Groovy (4)

| Key | Recommendation | Rationale |
|---|---|---|
| `Groovy constructor call` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Groovy ctor |
| `Groovy method declaration` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | Groovy method |
| `Groovy parameter` | `baseAttributes` → `DEFAULT_PARAMETER` | Groovy param |
| `Groovy reassigned parameter` | `baseAttributes` → `DEFAULT_REASSIGNED_PARAMETER` | Groovy reassigned param |

### HTTP (1)

| Key | Recommendation | Rationale |
|---|---|---|
| `HTTP_REQUEST_MESSAGE_BODY` | `baseAttributes` → `DEFAULT_PARAMETER` | HTTP body warm parameter |

### Java (6)

| Key | Recommendation | Rationale |
|---|---|---|
| `ANNOTATION_NAME_ATTRIBUTES` | `baseAttributes` → `DEFAULT_METADATA` | Annotation names → metadata/accent |
| `CONSTRUCTOR_CALL_ATTRIBUTES` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Ctor call ≈ class |
| `CONSTRUCTOR_DECLARATION_ATTRIBUTES` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Ctor decl ≈ class |
| `INTERFACE_NAME_ATTRIBUTES` | `baseAttributes` → `DEFAULT_INTERFACE_NAME` | Interface name |
| `JAVA_KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | Java keyword |
| `STATIC_METHOD_ATTRIBUTES` | `baseAttributes` → `DEFAULT_STATIC_METHOD` | Static method |

### Jupyter (1)

| Key | Recommendation | Rationale |
|---|---|---|
| `JUPYTER_CELL_MARKER` | `baseAttributes` → `DEFAULT_KEYWORD` | Jupyter cell marker keyword-colored |

### Mako (1)

| Key | Recommendation | Rationale |
|---|---|---|
| `MAKO.SUBSTITUTION` | `pin_empty` (inherit) | Pin empty |

### ObjC (3)

| Key | Recommendation | Rationale |
|---|---|---|
| `OC.CONDITIONALLY_NOT_COMPILED` | explicit: `FOREGROUND=6f6e6d` | Conditionally off code muted light1 |
| `OC.DIRECTIVE` | `baseAttributes` → `DEFAULT_METADATA` | ObjC directive ≈ metadata |
| `OC.METHOD_DECLARATION` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | ObjC method |

### Plan9 (3)

| Key | Recommendation | Rationale |
|---|---|---|
| `com.plan9.IDENTIFIER` | `baseAttributes` → `DEFAULT_IDENTIFIER` | Plan9 id |
| `com.plan9.LABEL` | `baseAttributes` → `DEFAULT_LABEL` | Plan9 label |
| `com.plan9.REGISTER` | `baseAttributes` → `DEFAULT_PARAMETER` | Plan9 register |

### Proto (2)

| Key | Recommendation | Rationale |
|---|---|---|
| `PROTOTEXT_IDENTIFIER` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Prototext id |
| `PROTO_IDENTIFIER` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Protobuf id |

### Scala (5)

| Key | Recommendation | Rationale |
|---|---|---|
| `Scala Abstract class` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Scala abstract class |
| `Scala Predefined types` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Scala predefined types |
| `Scala Type Alias` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Type alias violet |
| `Scala Type parameter` | `baseAttributes` → `DEFAULT_STATIC_FIELD` | Type param violet |
| `ScalaDoc @param value` | `baseAttributes` → `DEFAULT_DOC_COMMENT_TAG_VALUE` | ScalaDoc param value |

### Space-named (15)

| Key | Recommendation | Rationale |
|---|---|---|
| `Abstract class name` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Abstract class |
| `Annotation` | `baseAttributes` → `DEFAULT_METADATA` | Annotation |
| `Anotation attribute name` | `baseAttributes` → `DEFAULT_PARAMETER` | Annotation attr (sic spelling) |
| `Class` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Class space-name → class (or CLASS_NAME_ATTRIBUTES if exists) |
| `Closure braces` | `baseAttributes` → `DEFAULT_BRACES` | Closure braces → braces |
| `Interface name` | `baseAttributes` → `DEFAULT_INTERFACE_NAME` | Interface |
| `Label` | `baseAttributes` → `DEFAULT_LABEL` | Label |
| `List/map to object conversion` | `pin_empty` (inherit) | Pin empty |
| `Method call` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Method call |
| `Method declaration` | `baseAttributes` → `DEFAULT_FUNCTION_DECLARATION` | Method decl if present as space name |
| `Number` | `baseAttributes` → `DEFAULT_NUMBER` | Number |
| `Standart Java Collection` | explicit: `EFFECT_TYPE=5` | Collection type dotted underline only |
| `String` | `baseAttributes` → `DEFAULT_STRING` | String |
| `TAG_ATTR_KEY` | `baseAttributes` → `DEFAULT_ATTRIBUTE` | Tag attr key |
| `Valid string escape` | `baseAttributes` → `DEFAULT_VALID_STRING_ESCAPE` | Escape |

### SpyJS (2)

| Key | Recommendation | Rationale |
|---|---|---|
| `SPY-JS.EXCEPTION` | explicit: `EFFECT_TYPE=2` | Spy-js exception underline |
| `SPY-JS.FUNCTION_SCOPE` | explicit: `EFFECT_TYPE=2` | Spy-js scope underline |

### Swift (2)

| Key | Recommendation | Rationale |
|---|---|---|
| `SWIFT_ATTRIBUTE_NAME` | `baseAttributes` → `DEFAULT_METADATA` | Swift attribute |
| `SWIFT_MODULE_NAME` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Swift module |

### Velocity (4)

| Key | Recommendation | Rationale |
|---|---|---|
| `VELOCITY_DIRECTIVE` | `baseAttributes` → `DEFAULT_CLASS_NAME` | Velocity directive |
| `VELOCITY_KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | Velocity keyword |
| `VELOCITY_REFERENCE` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | Velocity ref ≈ call |
| `VELOCITY_SCRIPTING_BACKGROUND` | explicit: `BACKGROUND=222120`, `FOREGROUND=dfdedd` | Velocity scripting island |

### XPath (3)

| Key | Recommendation | Rationale |
|---|---|---|
| `XPATH.FUNCTION` | `baseAttributes` → `DEFAULT_FUNCTION_CALL` | XPath function |
| `XPATH.KEYWORD` | `baseAttributes` → `DEFAULT_KEYWORD` | XPath keyword |
| `XPATH.XPATH_VARIABLE` | `baseAttributes` → `DEFAULT_LOCAL_VARIABLE` | XPath variable |

### samples (6)

| Key | Recommendation | Rationale |
|---|---|---|
| `samples/csharp/Showcase.cs` | _process:_ Sample file authoring — no color | Sample file authoring — no color |
| `samples/html/Showcase.html` | _process:_ Sample file authoring — no color | Sample file authoring — no color |
| `samples/optional_go_python_ruby` | _process:_ Sample file authoring — no color | Sample file authoring — no color |
| `samples/php/Showcase.php` | _process:_ Sample file authoring — no color | Sample file authoring — no color |
| `samples/rust/Showcase.rs` | _process:_ Sample file authoring — no color | Sample file authoring — no color |
| `samples/typescript/Showcase.ts` | _process:_ Sample file authoring — no color | Sample file authoring — no color |

### screenshots (2)

| Key | Recommendation | Rationale |
|---|---|---|
| `screenshot_docs` | _process:_ Document capture steps | Document capture steps |
| `screenshot_produce` | _process:_ Produce 5 language screenshots | Produce 5 language screenshots |

### verify (8)

| Key | Recommendation | Rationale |
|---|---|---|
| `verify_defaults_panel` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_next_edit` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_quickdoc` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_scheme_loads` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_scrollbar` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_search_caret` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_showcases` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |
| `verify_vcs` | _process:_ Verification step — not a scheme key | Verification step — not a scheme key |

## Implementation snippet patterns

```xml
<!-- baseAttributes -->
<option name="org.rust.FUNCTION" baseAttributes="DEFAULT_FUNCTION_DECLARATION" />

<!-- explicit -->
<option name="org.rust.LIFETIME">
  <value>
    <option name="FOREGROUND" value="9896ff" />
    <option name="FONT_TYPE" value="2" />
  </value>
</option>

<!-- color -->
<option name="FILESTATUS_RENAMED" value="78dce8" />
```

## Notes

1. **`DEFAULT_BLOCK_COMMENT`** must land before Rust/others that base to it; use the same FG as `DEFAULT_LINE_COMMENT` (`acacac`).
2. **C#**: no new colors recommended; audit only. Existing `ReSharper.*` hexes stay.
3. **Partials** keep existing FG where listed “keep”; only add BACKGROUND / EFFECT / FONT_TYPE.
4. **ScrollBar.Mac.***: solid `dark8` / `dark10` rather than inventing new alpha hex; theme.json `ScrollBar.thumbColor` → `dark8`.
5. Apply in phase order from `todo.md`; re-run visual QA flags after each language batch.
