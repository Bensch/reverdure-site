# White Hot — marketing site

Static landing page for **White Hot** (the iOS + Apple Watch game; its codebase is
still called Reverdure). Plain HTML/CSS, no build step. Lives in its own public repo so
the game's source stays private. Served by GitHub Pages at
`https://reverdure.yourstrategy.co`.

## Files

| Path | What |
|---|---|
| `index.html` | The page |
| `styles.css` | All styling (mobile-first) — the game's own look: the dark map's ground, the heat ramp, the play button's ember, Liquid Glass panels |
| `assets/territory.jpg` | Hero and closing backdrop: territory baked by the game's own map code |
| `assets/screenshot.jpg` | In-phone gameplay screenshot shown in the hero |
| `assets/app-icon.png` | The app icon (also the share page's wordmark icon) |
| `og-image.png` | Link-preview / social share card |
| `tools/make_assets.py` | Builds `territory.jpg` and `og-image.png` from the game repo's renders |
| `.nojekyll` | Tells GitHub Pages to serve files as-is (no Jekyll) |

The share landing page the game server serves (`server/app/routes/share.py` in the game
repo) copies this site's colour tokens; change them together.

## Art

The territory art is rendered by the game repo's `scripts/brand/render-territory`, which
compiles the app's own `HeatField` (the map's heat overlay) — see the header of
`tools/make_assets.py` for the commands. The app icon comes from the game repo's
`scripts/brand/render-icon`.

## Local preview

```sh
python3 -m http.server 8099
# open http://localhost:8099
```
