---
name: md-preview
description: Serve a directory's Markdown files rendered as HTML in the browser (GitHub style, dark mode, mermaid, working cross-links) via a local Python server. Use when the user wants to view, preview, read or browse .md files rendered in a browser.
argument-hint: "[directory, default: current project] [port, default: 8765]"
---

# Markdown preview

Script: `~/.claude/skills/md-preview/mdserve.py` (Python 3 stdlib only; rendering libs load from CDNs in the browser).

1. Directory = first argument, else the current working directory. Port = second argument, else 8765.
2. If something already answers on the port (`curl -s -o /dev/null -w '%{http_code}' localhost:PORT/`), check whether it's this server for the same directory; if not, pick the next free port.
3. Start it with Bash `run_in_background: true`:
   `python3 ~/.claude/skills/md-preview/mdserve.py <dir> <port>`
4. Verify: `curl -s -o /dev/null -w '%{http_code}' localhost:<port>/` returns 200.
5. Open it: `xdg-open http://localhost:<port>/ >/dev/null 2>&1 &`
6. Tell the user the URL in one or two lines: index lists all `.md` files, refresh to see edits, bound to 127.0.0.1 only, runs until the session ends or they ask to stop it.

To stop: stop the background task (TaskStop), or `pkill -f 'md-preview/mdserve.py'`.

Don't write anything into the served directory.
