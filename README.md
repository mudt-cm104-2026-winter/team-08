# Team project

<!-- Replace the title with your project name. -->

## What this is

<!-- One or two sentences: what does your app do, and who is it for?
Right now it is the example "Things to bring". Replace it with your topic. -->

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

- 2026-11-05: course sheet "assessment-1-team-project.md", used for the stage 1 requirements
- 2026-11-05: Teams video 07 "A pull request, start to finish", used for branches, pull requests and reviews

## Use of AI

- 2026-11-11: Claude, checked our repo against the checklist.
- 2026-11-12: Claude, step-by-step help renaming the app fields for PR #21 (#11).
- 2026-11-13: Claude, help with checking by reviewing the diffs and testing the page

