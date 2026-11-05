# workspace

My personal Claude Code configuration, version-controlled.

## Contents

- `CLAUDE.md` — global instructions (who I am, environment, how I like Claude to work)
- `settings.json` — Claude Code settings + permission allowlist
- `memory/` — persistent memory facts (`MEMORY.md` is the index)

## How it works

These files live here but are **symlinked** into `~/.claude/`, which is where
Claude Code actually reads them. Editing them here updates the live config.

## Setup on a new machine

```sh
git clone <this-repo> ~/projects/workspace
~/projects/workspace/setup.sh
```

`setup.sh` symlinks `CLAUDE.md`, `settings.json`, and `memory/` into `~/.claude`.
It's idempotent (safe to re-run) and backs up any existing real files it would
replace. The memory target path is derived from the repo's parent directory.
