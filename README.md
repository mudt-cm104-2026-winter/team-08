# Reading List

## What this is

   A small web app for keeping a reading list. You enter a book's title and author, and the app shows all your books as a list.
   It is for students who want to keep track of the books they want to read.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

## Team

<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->

| GitHub | Role |
|---|---|
|DeryaG08|team member|
|amikristulii|team member|
| 64gwkfc9v9-ai | Board and issues |

## How we work

- Every piece of work starts as an issue and is a sub-issue of one of our three epics.
- One branch per issue, named after it, e.g. `8-how-we-work`.
- Every pull request says `closes #n` in its description, plus what changed and why.
- Nobody pushes to `main`: every pull request needs one approval from another team member.
- The author merges after the approval.
- Every pull request adds one line at the top of `## Unreleased` in CHANGELOG.md.

## Sources

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
