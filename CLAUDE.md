# Plaza Commercial Center — Website Project Guide

This file orients any agent (Claude Code or otherwise) picking up this project cold.

## What this is

The marketing website for **Plaza Commercial Center**, a midcentury-modern commercial flex complex in Santa Barbara, CA's Lagoon District, managed by Stephanie McGowan (management@plazacommercialcenter.com, (805) 681-2878). The complex has 15 flex units (industrial/retail/office) spanning three street frontages — East Cota Street, Garden Street, and Santa Barbara Street. Live at [plazacommercialcenter.com](https://plazacommercialcenter.com).

The site is static HTML/CSS with light inline JS (photo lightbox gallery, mobile hamburger menu, tenant photo carousels) — no framework, no build step. Each `.html` file is fully self-contained with its own `<style>` block; there is no shared stylesheet.

**As of September 14, 2026, this folder IS a git repo**, cloned from and tracking `github.com/dee-peppard/plazacommercialcenter` (branch `main`, deployed via GitHub Pages to plazacommercialcenter.com — custom domain configured via the `CNAME` file at the root, which points to `www.plazacommercialcenter.com`; don't delete that file). This replaces the old workflow, where the user manually dragged this whole folder into GitHub's web upload UI — that upload-only mechanism doesn't delete files that are no longer present locally, which is exactly what caused this migration (a folder reorganization left ~50 stale duplicate files sitting in the deployed repo alongside the new organized folders, and had to be cleaned up by hand).

**Going forward, commit and push through git** (`git add`, `git commit`, `git push origin main`) rather than the GitHub web upload page — this keeps history, and deletions/renames propagate correctly instead of silently leaving orphaned files behind. GitHub auth is handled via the `gh` CLI (installed to `~/.local/bin/gh`, not on the system PATH by default — prepend `export PATH="$HOME/.local/bin:$PATH"` or call it by full path) with a device-flow login token stored in the macOS keychain; `git push`/`pull` use it automatically via `gh auth setup-git`. If auth ever needs refreshing, run `gh auth status` to check, or `gh auth login --hostname github.com --git-protocol https --web` to reauthenticate (gives a one-time code + a github.com/login/device URL — no password needed, just a click to authorize since the user is normally already logged into GitHub in their own browser).

## Folder structure

As of September 2026 this folder was reorganized from ~50 flat files at the root into subfolders. **Every image/PDF reference in `index.html` and `design-community.html` uses these paths — if you add a new asset, drop it in the matching folder and reference it the same way (`./folder/filename`), don't add new files to the root.**

| Folder | Contents |
|---|---|
| `site/` | Site-wide assets used across pages: hero photo (`plazacommercial-2.jpg`), neighborhood map (`plazamap2.png`) |
| `docs/` | `Plaza-Commercial-Center-Brochure.pdf` — the old leasing brochure PDF. **No longer linked from anywhere** (Sept 2026): every "Download Brochure" / "Property Brochure" button now points to the Canva flyer, `https://canva.link/plaza-commercial-flyers` (3 buttons on `index.html`, 1 per unit page via `tools/build_unit_pages.py`). To change the flyer link, update those places; the PDF can be deleted once the owner confirms it's not needed |
| `units/210/`, `units/218/`, `units/220/` | Interior photos, concept renderings, and floor plans specific to each available unit |
| `units/shared/` | Assets shared by two units — the 218/220 bathroom finish photo and their combined floor plan |
| `tenants/` | Real current-tenant photos used in `design-community.html`'s "Meet Your Future Neighbors" section (Wilco Group, Global Lifestyle, Bowlus, HiFi Club, Jeff Clark Photography, Clear Construction) |
| `design/` | Mood board images used in `design-community.html`'s "The Palette" section |
| `210ecota/`, `218ecota/`, `220ecota/`, `218-220ecota/` | One `index.html` each — the per-unit landing pages (see "Unit landing pages" below). Served at `/210ecota`, `/218ecota`, `/220ecota`, `/218-220ecota` |
| `tools/` | `build_unit_pages.py` — generator for the four unit landing pages |
| root (`index.html`, `design-community.html`, `CLAUDE.md`) | The pages themselves and this doc |

**File naming inside the new folders was also cleaned up** — a few files that had spaces in their names (e.g. the old `210 Rendering-studio.jpeg`, `218 Rendering.jpeg`) were renamed to use hyphens instead (`210-Rendering-studio.jpeg`, `218-Rendering.jpeg`) so paths never need `%20` encoding. If you add a new file, keep using hyphens instead of spaces for the same reason.

### Unreferenced/duplicate files live OUTSIDE this folder, in a sibling `Plaza Archive (unused originals)/` folder

That sibling folder (next to `Plaza Website/`, not inside it) holds: duplicate/uncompressed originals (large `.png` versions of images now used as smaller `.jpg`s, e.g. `208ECota-HiFiClub.png`+`.jpg`, `218-A.png`+`.jpg`, `530SB-JeffClarkPhotography.png`+`.jpg`), an old floor plan version, a couple of dropped placeholder/rendering images, and two files (`PCC Map.png`, `plazacommercial.png`) that turned out to be orphaned on GitHub only — present in the repo but never in this local folder, and unreferenced by any page. Nothing was deleted — it was moved there (Sept 2026) specifically because GitHub's browser drag-and-drop uploader (back when that was still the deploy method — see above, this folder is a git repo now) rejected a commit for having files too large, and that archive folder (~48MB of dead weight not referenced by any page) was the prime suspect. **This sibling folder is intentionally outside the git repo — never `git add` it or otherwise push it.** If you need to reference or restore something from it, check there first before assuming it's gone.

## Files at the root

| File | Purpose |
|---|---|
| `index.html` | Homepage — the main site, live at the root domain |
| `design-community.html` | Secondary landing page pitching the complex to designers/architects/contractors/showrooms |
| `CNAME` | GitHub Pages custom domain config — contains `www.plazacommercialcenter.com`. Required for the custom domain to keep working; never delete it |
| `.gitignore` | Just excludes `.DS_Store` (macOS Finder metadata) from being tracked |

## Design system

- **Palette (midcentury modern, warm/terracotta):**
  - `--cream: #F6F1E9` · `--cream-dark: #EDE8DE` · `--warm-white: #FAF8F4` (backgrounds)
  - `--dark: #252220` · `--dark-mid: #3A3530` (dark sections, nav, footer)
  - `--terracotta: #B86245` (primary accent — links, buttons, badges) · `--terra-light: #D4896E`
  - `--sage: #6B7B5E` (secondary accent, occasional feature tile)
  - `--sand: #C4B49A` (muted text/borders/dividers)
- **Headline font:** `Cormorant Garamond` (serif, weights 300/400/500/600, italic 300/400 for emphasis spans)
- **Body font:** `DM Sans` (sans, weights 300/400/500)
- **Fonts loaded per-page:** `family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500`
- **Layout:** full-width sections with `padding: 104px 52px` (`.section`), no `max-width` wrapper container (unlike some other sites we've built — this one runs edge-to-edge with generous side padding instead of a centered `.wrap`)
- **Nav:** fixed, dark (`rgba(37,34,32,0.96)` + backdrop blur), hamburger + full-screen dark overlay menu below 960px, plain `onclick` toggling a `.open` class (no JS framework)
- **Mobile breakpoints:** `@media (min-width: 641px) and (max-width: 960px)` for tablet, `@media (max-width: 960px)` for general mobile, `@media (max-width: 640px)` for phone-specific tweaks — all at the bottom of each page's `<style>` block

### Recurring components (copy-pasted per page, not shared)

- **`.hero`** — full-bleed background photo (not an illustration/line-art like other sites — real photography), dark gradient + warm radial-tint overlay, arch-motif decorative border element referencing the building's arched entrances, content bottom-left, address bottom-right (hidden on mobile).
- **`.stats-bar`** — solid terracotta band of stat tiles (unit count, ceiling height, street frontages, etc.) directly under the hero. `index.html` only.
- **`.avail-card` / `.avail-grid`** — the three highlighted "Available Units" cards on `index.html` (`#available`). Each has a badge, unit label, big square-footage number, a feature list, a "Photos & Floor Plan" gallery button (`onclick="openGallery('unitId')"`), a brochure/flyer link (to the Canva flyer), and a `mailto:` inquire link. **`design-community.html` has its own copy of these units as a static teaser** (`.units-teaser` section, "Space ready for your studio": four cards — 210, 218, 220 and the combined 218 + 220 space — each with a "Full Listing →" link to that unit's landing page, no gallery button; 4 across on wide screens, 2×2 between 961–1360px, 1 column on phones) — badges must be updated in both places when availability changes.
- **`.unit-card` / `.units-grid`** — the full "All Units" table (`#units`) on `index.html`, grouped by street via `.street-block`, with `.badge-available` / `.badge-soon` / `.badge-leased` status pills.
- **Photo gallery lightbox** — full-screen modal (`#galleryModal`) driven by a `UNITS` JS object keyed by unit id, each with a `photos` array and a `floorplan` filename. Arrow nav, dot indicators, keyboard (←/→/Esc), touch swipe. Only on `index.html`; `design-community.html` uses plain inline images instead (no lightbox).
- **`.tenant-card` / `.tenant-photos`** — on `design-community.html` only. Real current tenants (Wilco Group, Global Lifestyle, Bowlus, HiFi Club, Jeff Clark Photography, Clear Construction) with a small photo carousel (`cycleTenantPhoto()` JS, prev/next + dots) per card.
- **`.gallery-card`** on `design-community.html`'s "Picture It" section — AI/concept renderings of units 210/218/220 styled as different studio use-cases (product design studio, gallery, architecture studio). Each card shows only the image, a "Unit … · Concept Rendering" tag and a short title — the descriptive sentences under the titles were removed at the owner's request (Sept 2026); don't add them back.
- **Contact pattern:** every "Schedule a Tour" / "Inquire" / "Request a Tour" CTA site-wide is a `mailto:management@plazacommercialcenter.com?subject=...` link — **not** an on-page form. This is the opposite convention from some other sites we've built (which route CTAs to an on-page Formspree form) — don't try to add a contact form here unless asked; the established pattern is mailto links with a pre-filled subject line per context (e.g. `?subject=Leasing Inquiry: Unit 210`, `?subject=Design Community Inquiry`, `?subject=Tour Request`).

## Page inventory

| Page | File | Notes |
|---|---|---|
| Homepage | `index.html` | Promo banner (links to Design Community) → Nav → Hero → Stats → About → Available Units → All Units → Neighborhood → Contact → Footer → gallery lightbox |
| Design Community | `design-community.html` | Hero → Palette (mood boards) → Who's Already Here (field types) → Picture It (concept renderings) → Available Now (static teaser) → Meet Your Future Neighbors (real tenants) → Final CTA → Footer |
| Unit landing pages (4) | `210ecota/index.html`, `218ecota/index.html`, `220ecota/index.html`, `218-220ecota/index.html` | Per-unit leasing pages, added Sept 2026. Linked from the "View Unit Page" button on each Available Units card in `index.html` (210/218/220 only — the combined 218-220 page is reachable via the unit switcher on the unit pages), and from each other; they link back to `/` and `/design-community.html` |

Nav order (`index.html` and `design-community.html`, identical): **Available → All Units → Neighborhood → Design Community → Contact**. `design-community.html`'s internal section links point back to `index.html` (e.g. `index.html#available`) since those sections don't exist on that page.

## Unit landing pages (`/210ecota`, `/218ecota`, `/220ecota`, `/218-220ecota`)

Added September 2026 as standalone leasing pages for each available unit (plus one for the combined 218 + 220 space, 4,747 SF), meant to be shared directly (LoopNet, email, QR codes). Each page has: hero + availability badge, a sticky **unit switcher** (links to all four pages), stats bar, unit summary + highlights, photo gallery with lightbox (real photos separated from labeled "Concept Renderings"), floor plan with download, an "Also available" card row linking to the other three pages, a link tile to the main site and one to Design Community, a contact section, and a footer with nav links.

- **These four files are generated — don't hand-edit them.** `tools/build_unit_pages.py` holds all per-unit content (`PAGES` dict), the shared CSS/JS, and the HTML template. Edit it and run `python3 tools/build_unit_pages.py` from the repo root to rewrite all four `index.html` files, then commit. (Deliberate exception to the site's otherwise hand-authored/no-build convention: four near-identical pages drift apart fast when edited by hand.)
- **Paths are root-relative** (`/units/210/...`, `/design-community.html`, `/`), unlike `index.html`/`design-community.html` which use `./` paths — the pages live one folder deep. Because of that they only render correctly when served from the domain root (run a local server such as `python3 -m http.server` from the repo root to preview; opening the file directly via `file://` will break images).
- **Directory-style URLs**: each page is `<slug>/index.html` so GitHub Pages serves `/210ecota` (it 301s to `/210ecota/`). The combined page's slug is `218-220ecota`.
- **Availability text lives in the `PAGES` dict** (`avail`, `avail_short`, `stats`, and the sentences in `overview`/`tagline`). The "Also available" cards deliberately show only size and a blurb — no status — so a status change touches fewer places. When a unit's status changes, update it in the generator (unit's own page **and** the combined 218-220 page for 218/220), regenerate, *and* still update `index.html` and `design-community.html` as described under "Current unit status".
- **Meta/SEO**: each page has its own `<title>`, description, canonical URL (`https://www.plazacommercialcenter.com/<slug>/`) and Open Graph tags (hero image as `og:image`).
- CTAs follow the site convention: `mailto:` links with a pre-filled subject (`Leasing Inquiry: Unit 210`, `Leasing Inquiry: Units 218 & 220`).
- **AI-enhanced images are labeled.** `units/218/218-A.jpg` and `218-B.jpg` carry a Gemini sparkle watermark in the bottom-right corner, i.e. they are AI-generated/edited rather than straight photographs. Per the owner's call, every place they appear shows a small "AI enhanced" tag in the image's bottom-right corner (mirroring the baked-in "this is a rendering" text on the concept renderings): unit-page gallery thumbnails, the unit-page lightbox, the 218 hero, the 218 card in "Also available", and the main site's `openGallery` lightbox (the `AI_ENHANCED` array near the top of `index.html`'s script). In the generator, flag an image with a trailing `True` in its `PAGES` photo tuple (or `hero_tag="AI enhanced"` / `thumb_tag="AI enhanced"`). **Any new AI-generated/edited image must be added to both places.** Do not crop the watermark out. The 218 page's `og:image` deliberately uses the self-labeled rendering instead of an AI-enhanced photo.
- `units/210/210ECotaFloorPlan.png` is the *previous tenant's furnished layout* (it says "Welcome to AV!"), captioned "Existing furnished layout shown for reference". The owner is fine leaving it as is for now, and may supply a clean plan later.
- **210 hero is a concept rendering** (`units/210/210Rendering.jpeg`, the gallery walkway), chosen by the owner, and carries a small "Concept rendering" tag on the hero (the image's own baked-in "this is a rendering" text is at the very bottom edge and gets cropped in a wide hero). Any hero can show a tag via `hero_tag`, and any "Also available" card preview via `thumb_tag` (the 210 card preview is also the walkway rendering, tagged). The 210 share preview (`og`) stays a real photo. The concept-renderings section has no disclaimer sentence (owner: "people know what a concept rendering is"), and the entry-facade sketch was removed from the 210 renderings list — the file `units/210/210Cota-EntranceRendering.jpg` stays because `design-community.html` uses it as a background.
- **Copy rules from owner review (Sept 2026):** don't call any suite the "largest" (218 + 220 can be leased together as 4,747 SF, which is bigger than any single unit); don't describe where roll-up doors or entrances sit on the floor plans (floor-plan blurbs just state the sizes); the combined page's hero tagline leads with "4,747 SF of space". The bottom link tile to `/` is titled "Explore the Plaza" (nav/footer links to `/` still say "Main Site").
- **Lease terms wording (owner-approved):** unit pages say the lease is triple net (NNN), that NNN charges cover the property's operating costs (taxes, insurance, common-area maintenance), and that utilities, gas and cable are not included and are billed separately. **No lease rate is published anywhere** — the pages say the rate is available upon request (mailto link). Don't add rates unless asked. (The main site's cards still just say "NNN / Triple Net lease" with no utilities note.)

## Current unit status

15 units total. As of this writing:

| Unit | SF | Status |
|---|---|---|
| 202 E. Cota | 2,496 | Leased |
| 208 E. Cota | 2,452 | Leased |
| **210 E. Cota** | **2,300** | **Available Now** |
| 214 E. Cota | 3,169 | Leased |
| 216 E. Cota | 3,167 | Leased |
| **218 E. Cota** | **1,894** | **Available October 1st** |
| **220 E. Cota** | **2,853** | **Available 30-60 Days Notice** |
| 228 E. Cota | 2,012 | Leased |
| 230 E. Cota | 3,989 | Leased |
| 523 Garden St | 1,615 | Leased |
| 525 Garden St | 1,732 | Leased |
| 527 Garden St | 1,555 | Leased |
| 528 Santa Barbara St | 1,988 | Leased |
| 530 Santa Barbara St | 971 | Leased |
| 532A Santa Barbara St | 1,819 | Leased |

Units 218 + 220 can combine for 4,747sf contiguous. All leases are NNN/Triple Net.

⚠️ **A status change to an available unit must be updated in up to three places on the main pages — plus the unit landing pages (see "Unit landing pages" above), which are regenerated from `tools/build_unit_pages.py`:** the `.avail-card` in `index.html`'s Available Units section, the `.badge` in `index.html`'s All Units table, and the static teaser cards in `design-community.html`'s "Space ready for your studio" section (including the combined 218 + 220 card's badge, "218: Oct. 1st · 220: 30-60 Days") (that one is plain hardcoded text, not shared data — it will silently go stale if forgotten).

## Known open items / things a future agent should know

- **HubSpot contact form is at the bottom of every page** (added Sept 25, 2026), in a `<section class="info-form" id="request-info">` just above the footer: HubSpot's `hs-form-frame` embed (portal 247525464, form `5f4c8fb4-82ec-47ab-98fc-2749bed5d398`, region na2) inside a white card, with intro copy on the left ("Learn more about the Plaza" on the homepage and Design Community; "Interested in Unit 210?" etc. on the unit pages) and a call/email fallback. It replaces nothing — the existing mailto "Schedule a Tour" CTAs and homepage contact cards stay. The form renders in an **iframe**, so its inner look (fonts, its own "Contact Us" heading, coral Submit button, the "Create your own free forms" HubSpot footer on the free plan) is controlled only in HubSpot's form editor (Style tab), not by this site's CSS; site CSS only styles the card around it. **Any new HTML page needs this section (CSS + markup) as well as the tracking code.** The unit pages get it from `tools/build_unit_pages.py`. Don't submit test entries on the live site — they create real HubSpot contacts. HubSpot records which page each submission came from, so the unit pages double as source tracking.
- **HubSpot tracking code is on every page** (added Sept 25, 2026): the standard `<!-- Start of HubSpot Embed Code -->` snippet (`//js-na2.hs-scripts.com/247525464.js`, portal 247525464) sits just before `</body>` in `index.html`, `design-community.html`, and the shared template in `tools/build_unit_pages.py` (so it's included in all four unit pages when regenerated). **Any new HTML page must include it too.** It's the site's only third-party script; HubSpot sets cookies, so a cookie-consent setting may be needed in HubSpot's account settings if that's a concern.
- **Homepage header structure (Sept 2026):** on `index.html` the promo banner ("Now home to a growing design community…") and the `<nav>` are stacked inside one `<div class="site-top">` that is `position: fixed` at the top; the banner and nav themselves are normal-flow inside it. This replaced two separately fixed elements with a hard-coded `top: 44px` on the nav, which made the nav overlap the banner on phones (the banner wraps to 2–3 lines). Don't re-introduce a fixed `top` offset on the nav. The nav logo is `nowrap` and 19px at ≤640px on `index.html`, `design-community.html` and the unit pages. (`design-community.html` has no banner.)
- **Mobile-menu bug fixed (Sept 2026):** `index.html` had stray backslashes (`\!important`, `<\!--`) from a shell-escaping accident that broke the mobile menu's "Schedule a Tour" button styling and left a stray comment rendering as text. Removed. Watch for it if editing files through shell heredocs.
- **This folder is a git repo now (since Sept 14, 2026) — use `git add`/`commit`/`push`, not GitHub's web upload page.** Before that date it was upload-only with no git history, which is exactly what caused a cleanup headache once (see the folder-reorg note above): the web uploader only adds/updates, it never deletes, so a local reorg silently left ~50 stale files on GitHub until they were found and manually removed via a fresh clone + rsync mirror + commit. That risk goes away now that this folder tracks the remote properly — a normal `git push` correctly reflects deletions and renames.
- **`gh` (GitHub CLI) is installed at `~/.local/bin/gh`, not the system PATH** — prepend `export PATH="$HOME/.local/bin:$PATH"` before calling it, or use the full path. Auth token lives in the macOS keychain; check with `gh auth status`.
- **GitHub still rejects individual files over 25MB via its API/web layers** (this is why the `Plaza Archive (unused originals)/` sibling folder — see above — stays outside the repo; it's not referenced by any page and its largest files pushed toward that ceiling). A plain `git push` doesn't have that 25MB wall (git's own soft/hard limits are much higher, ~50-100MB), so this is now unlikely to resurface, but if a push is ever rejected for size, check `find . -type f -size +20M` inside `Plaza Website/` for the offending file.
- **This site's CTA convention is `mailto:` links, not a contact form** — this is a deliberate difference from other sites in this portfolio, not an inconsistency to "fix."
- **`design-community.html` duplicates unit availability as static text.** Any availability change on `index.html` needs a matching manual edit there.
- **Concept renderings on `design-community.html` are AI-generated/illustrative**, not photos of actual completed build-outs — labeled "Concept Rendering" in their captions. Don't present them as real installed tenant improvements.
- **The phone number `(805) 681-2878` is live and current** on both `index.html`'s contact section and `design-community.html`'s final CTA.
- **This project is unrelated to the Kora Commercial LLC site** — separate business, separate design system, separate folder. Don't cross-reference asset paths, brand colors, or component conventions between the two; they happen to share an agent history, not a codebase.
