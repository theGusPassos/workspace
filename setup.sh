#!/usr/bin/env bash
# Symlink this workspace's config into ~/.claude so Claude Code picks it up.
# Idempotent: safe to re-run. Backs up any existing real files it would replace.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"

# Memory is scoped to a project path, encoded by replacing each "/" with "-".
PROJECTS_DIR="$(cd "$REPO/.." && pwd)"
MEM_SCOPE="${PROJECTS_DIR//\//-}"
MEM_TARGET="$CLAUDE_DIR/projects/$MEM_SCOPE/memory"

link() {
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  # Already the correct symlink? nothing to do.
  if [ -L "$dst" ] && [ "$(readlink -f "$dst")" = "$(readlink -f "$src")" ]; then
    echo "ok   $dst"
    return
  fi
  # Something else is there: back it up (symlinks are just removed).
  if [ -e "$dst" ] || [ -L "$dst" ]; then
    if [ -L "$dst" ]; then
      rm "$dst"
    else
      mv "$dst" "$dst.bak.$(date +%Y%m%d%H%M%S)"
      echo "     backed up existing $dst"
    fi
  fi
  ln -sfn "$src" "$dst"
  echo "link $dst -> $src"
}

link "$REPO/CLAUDE.md"     "$CLAUDE_DIR/CLAUDE.md"
link "$REPO/settings.json" "$CLAUDE_DIR/settings.json"
link "$REPO/memory"        "$MEM_TARGET"

# Skills are linked one by one: ~/.claude/skills may hold other (synced) skills.
for skill in "$REPO"/skills/*/; do
  [ -d "$skill" ] || continue
  link "${skill%/}" "$CLAUDE_DIR/skills/$(basename "$skill")"
done

echo "Done."
