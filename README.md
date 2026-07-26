# Hiberbee Themes

Dark theme collection. The JetBrains plugin ships from this repository via **GitHub Releases** (custom plugin repository), same pattern as [BrainlessEnv](https://github.com/bitnixdev/BrainlessEnv).

## JetBrains IDE

### Install (updates from GitHub)

1. `Settings → Plugins → ⚙ → Manage Plugin Repositories… → +`
2. Add:
   ```
   https://github.com/bitnixdev/hiberbee/releases/latest/download/updatePlugins.xml
   ```
3. Search the Plugins marketplace tab for **Hiberbee Theme** and install.
4. Restart when prompted. Future releases update through that repository URL.

### Install from disk (one-off)

1. Download `hiberbee-theme-<version>.zip` from the [latest release](https://github.com/bitnixdev/hiberbee/releases/latest), or build locally:
   ```sh
   cd src/intellij
   ./gradlew buildPlugin
   # → build/distributions/hiberbee-theme-<version>.zip
   ```
2. `Settings → Plugins → ⚙ → Install Plugin from Disk…` and pick the zip.

### Release

One workflow (`.github/workflows/ci.yml`):

- **PR** — builds the plugin zip (artifact only)
- **push to `master`** (or **workflow_dispatch**) — builds, tags, and publishes a GitHub Release

Tag / version format (CalVer + git commit count):

```text
vYYYY.MM.DD.<rev-list --count HEAD>
# example: v2026.07.26.1842
```

Release assets: `hiberbee-theme-<version>.zip`, `.sha256`, `updatePlugins.xml` (IDE updates via the custom repository URL above).

```sh
# local check
cd src/intellij
./gradlew buildPlugin generateUpdatePluginsXml
```


### Screenshots

![IDE](screenshots/ide.png)

![Code](screenshots/code.png)

## Other platforms

Terminals, VS Code, Insomnia, etc. live under `src/`. See each subdirectory for install notes.

## Resources

- [Figma palette](https://www.figma.com/file/2oyhOnKUdLZCDQEkH2klNT/Hiberbee-Theme)
- Marketplace listing (legacy): [Hiberbee Theme](https://plugins.jetbrains.com/plugin/12118-hiberbee-theme)
