# Hiberbee for Zed

Dark theme for [Zed](https://zed.dev), built from the Hiberbee palette (iTerm2 ANSI + JetBrains/Helix syntax roles).

## Install (local)

Copy the theme family into Zed’s themes directory:

```bash
mkdir -p ~/.config/zed/themes
cp themes/hiberbee.json ~/.config/zed/themes/hiberbee.json
```

Then open the command palette → **theme selector: Toggle** → pick **Hiberbee Dark**.

## Install (extension)

From a release asset (`hiberbee-zed-theme-*.zip`):

1. Unzip
2. In Zed: **zed: install dev extension** (or Extensions → Install Dev Extension) and select the unzipped folder (the one containing `extension.toml`)

Or clone this repo and point Install Dev Extension at `src/zed`.

## Mapping notes

| Source | Used for |
|---|---|
| `src/iterm/Hiberbee.itermcolors` | `terminal.ansi.*`, editor/terminal bg/fg, selection, cursor |
| JetBrains `DEFAULT_*` / Helix palette | `syntax.*` token roles |
| JetBrains UI tokens (`dark*`, `light*`, `*Bg`) | Chrome, panels, status, VCS tints |
