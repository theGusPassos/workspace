---
name: learning-plan
description: Turn a learning request into a study plan saved in the plan tracker (~/selfhost/plan-tracker). Use when the user asks for resources to learn something, wants to learn a new topic or skill, asks for a roadmap/study plan, or says "make this a plan" about resources already discussed.
---

# Learning plan

Make a plan from what's already known, save it to the tracker, done. Keep it light.

## Steps

1. **Gather from the conversation.** Use resources, goals, level and time budget already mentioned. Don't do web research. Add a few well-known resources only if needed, and only URLs you're confident exist (official docs, well-known books/courses). Ask one short question only if the topic itself is unclear; otherwise assume sensible defaults and state them in the description.
2. **Write the markdown** to a file in the scratchpad (format below).
3. **Save:** `node ~/.claude/skills/learning-plan/save-plan.mjs <file.md>`. It never overwrites an existing plan (adds `-2`, `-3`...).
4. **Reply** with the plan title, the saved path, and a 2-3 line outline. Don't paste the whole plan.

If the user wants to add to an *existing* plan instead, edit `~/selfhost/plan-tracker/data/plans/<id>.json` (or under `$PLAN_TRACKER` if set) directly (new items: `{"id": <8 random hex chars>, "kind": ..., "title": ..., "done": false}`), but only when they ask.

## Format (parsed by the tracker's importer)

```markdown
# <Plan title>

<1-2 sentences: goal, assumed level, hours/week.>

## Phase 1: <name> (<N> weeks)
Optional one-line description.

### 1.1 <Module name> (week 1)
- [Resource title](https://url): why it matters. **must-read**

## Books
| Level | Book | Notes |
|---|---|---|
| Beginner | *Title*, Author | why |

## People / feeds to follow
- [Name](https://url): what you get
```

Rules:
- **Resources only.** Every item is something to read, watch or use (doc, article, video, course, book). No tasks, builds, capstones, exercises or "do X" items unless the user explicitly asks for them.
- **Every item in a phase needs a link**, because the importer turns link-less bullets into tasks. If you're not sure of a URL: for a video or talk, link a YouTube search (`https://www.youtube.com/results?search_query=<title+speaker>`); for a book, put it in the Books table instead.
- Size to the request: a small skill can be 1 phase with 2-3 modules; skip Books/People sections if there's nothing real to put there.
- 2-5 resources per module; mark only the essentials **must-read**.
- `## ` headings containing Books, Library, Reading, People, Feeds or Resources become reference sections (not counted in progress), so don't use those words in phase names.
