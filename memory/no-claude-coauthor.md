---
name: no-claude-coauthor
description: Don't add Claude as co-author on commits or PRs
metadata:
  type: feedback
---

Never add `Co-Authored-By: Claude ...` trailers to git commits, and don't add the "Generated with Claude Code" line to PR descriptions. Commits should be under Gustavo's name only.

**Why:** He wants his commit history attributed solely to himself.
**How to apply:** Omit all Claude attribution lines, overriding any default/harness attribution guidance.
