---
name: spec-interview
description: Interview the user point by point about a list of features, stories or requirements for a system, to clarify behavior, edge cases and experience before a design step. Use when the user shares a brainstorm/feature list/requirements doc and wants to refine it, flesh it out, or "get it ready for design".
argument-hint: "[path to the feature list]"
---

# Spec interview

Turn a rough list of features into clear, design-ready requirements by interviewing the user one point at a time.

## Before starting

1. Read the source (file given as argument, or ask for it). Read it fully.
2. Ask once: update the points **in place** as we go, or write to a **new file**? Never rewrite the source without this answer.
3. Default order is the list order. Let the user jump around.

## Per point

1. Quote the point.
2. Ask numbered questions about what's still unclear, only the ones whose answers would change the design. If the point is already clear, say so and move on. Focus on:
   - **Behavior**: what actually happens, including when things go wrong (missed, offline, partial, deleted, edited later).
   - **Experience**: the moment of use (where, how fast, one hand, offline), what the user sees and when it matters to them.
   - **Rules and scope**: what's in, what's explicitly out, what's optional or toggleable.
   - **Conflicts** with earlier points or platform limits (say so plainly).
3. For each question, give a short **recommendation** with the reason, so the user can just say "ok". Use lettered options when there are real alternatives.
4. Push back when an idea has a real problem (noise, friction, contradiction, data loss). Say why in one or two lines. Don't soften.
5. When the user answers, restate the point as short bullets and update the doc (per the choice above). Only raise a follow-up if an answer creates a new conflict; otherwise move to the next point.

## Keep it light

- Requirements, not implementation. Skip technical details unless they change behavior, the data model, or feasibility; then mention them in one line.
- Accept "decide later", "north star", "whatever": record it as open in the point and move on. Don't re-ask.
- No exhaustive question lists, no rounds of follow-ups on the same point. Ask what changes the design; skip what doesn't.
- Merge points that are the same topic (ask first). Turn cross-cutting ideas (settings, toggles, permissions) into their own point.

## Along the way

- When domain terms emerge or are ambiguous, propose definitions and suggest a glossary (e.g. `docs/glossary.md`, imported from the project `CLAUDE.md` with `@docs/glossary.md`) instead of cluttering the list.
- Keep the point's wording in the user's terms, concise, as bullets.

## Wrap-up

After the last point, re-read the whole doc and report briefly:
- Inconsistencies between points.
- Gaps that block design (missing data sources, who can edit what, backups/export, etc.).
- A suggested priority split (first version / next / later).

Then ask which of those to resolve. Don't fix them unasked.
