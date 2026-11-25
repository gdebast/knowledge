---
name: learn-analyze
description: Answer a question about a React / TypeScript code base while teaching the user. Every concept used in the answer is checked against the user's own knowledge notes (concept index), linked to the user's chapter when known, and turned into a runnable lab example when unknown. Use when the user types /learn-analyze <question>, or asks to analyse/explain code "with my knowledge repo" or "so I learn".
argument-hint: <question about the current repository>
---

# learn-analyze

The user is learning React and TypeScript. Answer their question about the
**current repository** (the "target repo"), and use the answer as a lesson
grounded in **their own notes** (the "knowledge repo").

## Paths

- `KNOWLEDGE_ROOT` = the root of the knowledge repo = two levels above this
  skill's **real** folder (this file is `KNOWLEDGE_ROOT/skills/learn-analyze/SKILL.md`).
  The skill is usually loaded through a junction/symlink in `~/.claude/skills/`,
  so the base directory you are given is NOT inside the repo: resolve it first
  (`realpath` before going up, otherwise `..` stays in `~/.claude`):

  ```
  py -c "import os,sys; print(os.path.normpath(os.path.join(os.path.realpath(sys.argv[1]), '..', '..')))" "<skill base directory>"
  ```

  (fall back to `python` / `python3` if `py` is missing). Use the printed path
  as `KNOWLEDGE_ROOT` everywhere below, with forward slashes.
- Notes: `KNOWLEDGE_ROOT/SoftwareEngineer/**/*.md`
- Concept index (generated, read-only): `KNOWLEDGE_ROOT/SoftwareEngineer/_index/concepts.md`
- Index generator: `KNOWLEDGE_ROOT/SoftwareEngineer/_index/build_index.py`
- Gaps log: `KNOWLEDGE_ROOT/SoftwareEngineer/_index/gaps.md`
- Lab project: `KNOWLEDGE_ROOT/SoftwareEngineer/_lab/`
- Lab template (bundled with this skill): `lab-template/` next to this file

If the resolved `KNOWLEDGE_ROOT` does not contain `SoftwareEngineer/_index/`,
the skill is not linked from the knowledge repo: stop and tell the user to
recreate the junction (see the knowledge repo's README.md, "One-time setup").

## Step 0 - Preconditions

1. Resolve `KNOWLEDGE_ROOT` (see *Paths*). Check that
   `KNOWLEDGE_ROOT/SoftwareEngineer/_index/concepts.md` is readable.
   If not, stop and tell the user to run `/add-dir <KNOWLEDGE_ROOT>` with the
   resolved path (or add it to `permissions.additionalDirectories` in this
   repo's `.claude/settings.local.json`).
2. Refresh the index so it matches the notes: run
   `py "KNOWLEDGE_ROOT/SoftwareEngineer/_index/build_index.py"`
   (fall back to `python` / `python3` if `py` is missing). Show any warning it
   prints. Never edit `concepts.md` by hand.
3. If `$ARGUMENTS` is empty, ask the user for their question and stop.

## Step 1 - Investigate the target repo

Answer the question from the actual code: find the files involved, follow
imports, props, hooks, state and data flow until you can explain the behaviour
precisely. Note `file:line` for every claim. Do not guess; if something cannot
be determined from the code, say so.

## Step 2 - List the concepts the answer depends on

Collect the React, TypeScript, JavaScript and library concepts that the user
must understand to follow the answer (e.g. `useEffect` cleanup, discriminated
union, `forwardRef`, TanStack Query `useQuery`, generics with `extends`,
custom hook, context provider). Keep it to the concepts that matter for this
answer, typically 3-12. Skip trivia (variables, `if`, basic JSX) unless the
question is about it.

## Step 3 - Classify each concept against the user's notes

For each concept:

1. Search `concepts.md` (Grep, case-insensitive) on the concept name, its API
   names and synonyms. Matches can be in the *Concept*, *Chapter*,
   *Keywords* or *aliases* (italic) columns.
2. For each candidate row, open the chapter at its line (Read with `offset` at
   that line, `limit` ~80) to see what the user actually wrote. A keyword match
   alone is not proof of knowledge.
3. Classify:
   - **Known** - the chapter explains the concept as used in the target code.
   - **Partial** - the chapter covers the basis, but the target code uses
     something the chapter does not explain (state precisely what is new).
   - **Unknown** - no chapter covers it.

## Step 4 - Write the answer

Structure:

### Answer
Explain the behaviour step by step, following the code, with `file:line`
links into the target repo. Tag every concept the first time it appears:

- Known: `useEffect cleanup` → [your notes: React.md L1151](<link>)
- Partial: same link + one or two sentences on the part that is new.
- Unknown: a short plain explanation + "→ lab: `<lab file>`".

When a concept is known, reuse the user's own wording/example from the chapter
when it helps ("as in your ProgressBar example...") rather than a generic
explanation.

Links to the notes use the resolved absolute `KNOWLEDGE_ROOT` with forward
slashes, e.g. `[React.md L1151](<KNOWLEDGE_ROOT>/SoftwareEngineer/React/React.md#L1151)`.

### Concepts
A table ending the answer:

| Concept | Status | Your notes | Lab | Where in target repo |
|---|---|---|---|---|

## Step 5 - Unknown concepts: lab example + gap entry

Do this for every **Unknown** concept (not for Known; for Partial only if the
new part cannot be explained in two sentences).

### 5a. Lab project
If `SoftwareEngineer/_lab/` does not exist, copy every file of `lab-template/`
into it (keeping the folder structure), then tell the user to run
`npm install` in `_lab` once. Do not run `npm install` yourself unless asked.

### 5b. Lab file
Create one file per concept in `_lab/src/concepts/`, kebab-case name:

- React concept → `<name>.tsx`, `export default function Demo()`; the lab app
  lists it automatically (`npm run dev`).
- Pure TypeScript concept → `<name>.ts`, runnable with `npx tsx src/concepts/<name>.ts`;
  use `console.log` and type errors the user can trigger.

Rules for the file:
- 15-40 lines of code, self-contained, no dependency on the target repo.
- Header comment: concept name, one-paragraph explanation, where it is used in
  the target repo (`repo-name/path:line`), and how to run it.
- Two or three `// TRY:` comments with small experiments, each with the
  question to answer ("what happens if you remove the cleanup? predict, then
  run"). At least one should break something on purpose.
- If the concept needs a library (e.g. `@tanstack/react-query`), tell the user
  which `npm install` to run in `_lab`; do not add it silently.
- If a lab file for the concept already exists, reuse it and do not overwrite
  it (the user may have edited it).

### 5c. Gaps log
Append a row to `SoftwareEngineer/_index/gaps.md` (create it from the header
below if missing; do not duplicate a concept that already has an open row -
add the new "seen in" location to it instead):

```
| Date | Concept | Seen in | Lab file | Suggested chapter | Status |
|---|---|---|---|---|---|
```

- *Suggested chapter*: the notes file and parent heading where a new chapter
  would fit (e.g. `React.md > Working with Refs and Portals`).
- *Status*: `open`.

## Step 6 - Close with next steps

End with a short list:
- lab files to try first (most important concept first);
- for each unknown concept: where to write the chapter, and the alias(es) to
  add to `SoftwareEngineer/_index/aliases.json` (the names used in the target
  code that the chapter title will not contain);
- reminder: after writing the chapter, run `build_index.py` and set the gap
  status to `done`.

## Rules

- Never write or edit chapters in the user's notes: writing them is how the
  user learns. Only `_lab/`, `gaps.md` are written by this skill.
- Never modify the target repo.
- Be honest in the classification: when in doubt between Known and Partial,
  choose Partial and say what is missing.
