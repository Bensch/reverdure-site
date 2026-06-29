# Reverdure — marketing site

Static landing page for **Reverdure** (the iOS + Apple Watch game). Plain HTML/CSS,
no build step. Lives in its own public repo so the game's source stays private.

## Files

| Path | What |
|---|---|
| `index.html` | The page |
| `styles.css` | All styling (mobile-first) |
| `assets/hexfield.svg` | Generated hero background (grey → green reclamation) |
| `assets/screenshot-map.jpg` | In-phone gameplay screenshot shown in the hero |
| `og-image.png` | Link-preview / social share card |
| `.nojekyll` | Tells GitHub Pages to serve files as-is (no Jekyll) |

## Hosting (GitHub Pages)

1. Push to a **public** repo (Pages on a private repo needs a paid GitHub plan).
2. Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / `/ (root)`.
3. Site goes live at `https://<user>.github.io/<repo>/` within a minute or two.

### Custom domain (free, with HTTPS)

- **Subdomain** (e.g. `reverdure.yourstrategy.co`): add a DNS `CNAME` record pointing
  to `<user>.github.io`, then set the domain under Settings → Pages. GitHub commits a
  `CNAME` file and provisions HTTPS automatically.
- **Apex** (e.g. `reverdure.com`): point `A` records at GitHub's IPs
  (`185.199.108–111.153`) and set the domain under Settings → Pages.

## Updating the beta link

The "Join the beta" buttons point at a placeholder. Replace every
`https://testflight.apple.com/join/PLACEHOLDER` in `index.html` with the real
TestFlight public link.

## Local preview

```sh
python3 -m http.server 8099
# open http://localhost:8099
```
