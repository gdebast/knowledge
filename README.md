# Knowledge repo

My notes on software engineering (React, TypeScript, Playwright, AI-assisted
development), plus the tooling that turns them into a learning loop with
Claude Code: when I analyse another React / TypeScript code base, Claude
explains it **with the concepts I already know** (linking to my own chapters)
and gives me **small runnable examples** for the ones I don't.

## Repository layout

```
README.md                          this file
skills/
  learn-analyze/                   Claude Code skill /learn-analyze
    SKILL.md                       the skill instructions
    lab-template/                  starter copied to SoftwareEngineer/_lab on first use
SoftwareEngineer/
  React/React.md                   notes (one file per topic, images next to it)
  Typescript/Typescript.md
  Playwright/Playwright.md
  AI/...
  _index/
    build_index.py                 generates concepts.md from the notes' headings
    concepts.md                    GENERATED concept index - do not edit
    aliases.json                   extra search terms per heading (hand-written)
    gaps.md                        concepts met but not yet in my notes
  _lab/                            Vite + React + TS playground (created on first use)
```

Folders starting with `_` are tooling, not notes: the index generator skips them.

## Writing notes

The index is built from the **headings** of every `.md` file under
`SoftwareEngineer/`, so the headings are what makes a concept findable.

- One concept per `##` / `###` heading, with a name that says what it is
  (`useEffect clean up function`, not `Part 2`).
- Put code examples in fenced blocks with their `import` lines: imported
  packages and symbols (`useQuery`, `ReactNode`, ...) and hook names become
  keywords of the section automatically.
- When the code I meet uses another name than my heading (e.g. *discriminated
  union* vs my *discriminating union*), add it to `_index/aliases.json`:

  ```json
  "Typescript/Typescript.md": {
    "discriminating union": ["discriminated union", "tagged union"]
  }
  ```

  Keys are the file path relative to `SoftwareEngineer/` and the heading text as
  shown in `concepts.md` (case-insensitive). An alias pointing to a heading
  that no longer exists is reported as a warning.

## The concept index

```
py SoftwareEngineer/_index/build_index.py          # regenerate concepts.md
py SoftwareEngineer/_index/build_index.py --check  # exit code 1 if concepts.md is stale
```

`concepts.md` has one row per heading: concept, parent chapters, keywords
(aliases in italics) and a link to the exact line. It is only standard-library
Python (3.9+). The `/learn-analyze` skill regenerates it at the start of each
run, so it is never stale during an analysis; regenerate it yourself after
editing notes if you browse it directly.

## The /learn-analyze skill

### One-time setup

The skill lives in this repo and is linked into Claude Code's user skills
folder, so it is available in every repository:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\learn-analyze" `
  -Target "E:\Development\GDB\Knowledge_gdb_ghe\main\skills\learn-analyze"
```

Replace the `-Target` with wherever this repo is checked out. A junction needs
no admin rights and edits in this repo apply immediately. The skill finds the
repo by resolving the junction, so no path is hard-coded: if the repo moves,
only the junction needs to be recreated (`Remove-Item` it, then run the
command again with the new target).

### Running an analysis

In a Claude Code session opened on the **other** repository:

```
/add-dir E:\Development\GDB\Knowledge_gdb_ghe\main
/learn-analyze how is the bucket-horizon-id component rendered?
```

To avoid `/add-dir` every session, add the path to that repo's
`.claude/settings.local.json` (local, not committed):

```json
{ "permissions": { "additionalDirectories": ["E:\\Development\\GDB\\Knowledge_gdb_ghe\\main"] } }
```

The answer explains the code step by step and tags each concept:

| Status | Meaning | What I get |
|---|---|---|
| **Known** | a chapter of my notes covers it | link to my chapter |
| **Partial** | my chapter covers the basis, the code goes further | link + explanation of the new part |
| **Unknown** | not in my notes | short explanation + a lab file + a row in `gaps.md` |

It ends with a concept table and next steps. The skill never edits my notes
(writing them is the learning) and never modifies the analysed repo.

### The lab

Unknown concepts get a small file in `SoftwareEngineer/_lab/src/concepts/`:

- `name.tsx` - React demo; run `npm run dev` in `_lab` and pick it in the menu.
- `name.ts` - plain TypeScript; run `npx tsx src/concepts/name.ts`.

Each file has `// TRY:` experiments: predict the result, then run. The first
time, run `npm install` in `SoftwareEngineer/_lab`. On this machine npm uses the
company feed (`cdn-feeds.omp.com`), so I must be authenticated to it first.

## The learning loop

1. `/learn-analyze <question>` in the other repo.
2. Play with the lab files of the unknown concepts.
3. Write the chapter in the notes file suggested in `gaps.md`.
4. Add the names used in the analysed code to `aliases.json`.
5. `py SoftwareEngineer/_index/build_index.py`, then set the gap to `done`.

Next analysis, the concept is **Known** and links to my own chapter.
