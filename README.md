# memi lisboa

A Lisbon memory card game built on [memi-engine](https://github.com/filias/memi-engine).

Live at [lx.memi.click](https://lx.memi.click). Pushes to `main` auto-deploy via GitHub webhook.

## Categories

- **Cultura: Metro** — stations of the Lisbon Metro
- **Cultura: Monumentos** — Lisbon monuments and landmarks
- **Geografia: Freguesias** — the 24 civil parishes of Lisbon
- **Geografia: Atrações** — neighbourhoods, squares, parks and museums

## In English

The game is also playable in English at [/en/](https://lx.memi.games/en/),
with a `pt | en` switch in the header (memi-engine 0.11.0's `languages`). The
English interface and about page are in `languages` in `memi_lx/app.py`;
answers and tags come from the `EN` dicts in `memi_lx/categories/`. Proper
names English keeps in Portuguese (Alfama, Praça do Comércio, the metro
stations and parishes) have no entry and show as they are.

## Setup

```bash
uv sync
uv run python -m memi_lx.app
```
