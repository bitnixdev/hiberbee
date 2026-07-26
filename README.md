# Hiberbee (fork)

Private fork of [hiberbee/themes](https://github.com/hiberbee/themes). Prefer upstream for docs, other platform themes, and Marketplace releases.

## JetBrains plugin (this fork)

Custom plugin repository (updates from GitHub Releases):

```
https://github.com/bitnixdev/hiberbee/releases/latest/download/updatePlugins.xml
```

`Settings → Plugins → ⚙ → Manage Plugin Repositories…` → add the URL → install **Hiberbee (bitnix)**.

Plugin id is `dev.bitnix.hiberbee` so it does **not** replace the upstream Marketplace plugin (`com.hiberbee.intellij.hiberbee-theme`). If an older fork build already overwrote upstream, uninstall **Hiberbee (bitnix)**, reinstall upstream from Marketplace if needed, then install this fork again.

Or install the zip from [releases](https://github.com/bitnixdev/hiberbee/releases/latest) via **Install Plugin from Disk…**.

Pushes to `master` auto-release as `vYYYY.MM.DD.<commit-count>` via `.github/workflows/ci.yml`.

## Zed theme

Theme extension lives in `src/zed/`. Each release also attaches:

| Asset | Use |
|---|---|
| `hiberbee-zed-theme-<ver>.zip` | Zed **Install Dev Extension** (folder with `extension.toml`) |
| `hiberbee-zed-theme-<ver>.json` | Drop into `~/.config/zed/themes/` |

Local install:

```bash
mkdir -p ~/.config/zed/themes
cp src/zed/themes/hiberbee.json ~/.config/zed/themes/hiberbee.json
```

Then **theme selector: Toggle** → **Hiberbee Dark**.

## iTerm2

Preset: `src/iterm/Hiberbee.itermcolors` (also attached on releases as `Hiberbee.itermcolors`).

Import: iTerm2 → **Profiles → Colors → Color Presets… → Import**.

Modern keys included: ANSI 0–15, fg/bg, bold, cursor (+ guide/text), selection (+ selected text), link, badge, **tab**, **underline**, **match background** — palette aligned with Windows Terminal / JetBrains Hiberbee tokens.
