# Design — The World in One Image, 21 November 2026

## Idea
A newspaper front page, drawn entirely with PIL shapes and text: one image
that a reader can scan in seconds and still walk away with the day's three
big stories plus three briefs.

## Layout (1024 × 1024)
- **Masthead (0–150):** navy band, serif title "THE WORLD IN ONE IMAGE",
  gold rule, gold dateline "SATURDAY, 21 NOVEMBER 2026".
- **Lead (170–545):** white card, red kicker "LEAD · WAR IN EUROPE",
  two-line headline on Russia's overnight assault, a three-line body
  (Kyiv deaths and bridge damage; missiles and a drone down in Poland;
  PM Tusk's "deliberate provocation"), and two navy stat chips —
  "400+ drones launched" and "110 missiles launched".
- **Middle row (565–810):** two cards side by side.
  - Left, green header "MARKETS": "AI sell-off deepens" — S&P and Dow
    down 3.7% on Friday, days after Anthropic's $2 trillion IPO.
  - Right, teal header "UK–EU": "Post-Brexit deal struck in Brussels" —
    PM Andy Burnham seals a new UK–EU agreement.
- **Footer (830–1000):** gold rule, then three briefs in columns —
  PROTESTS (Gen Z protests in 25 European countries), CLIMATE (COP31
  opens in Antalya), HEALTH (daraxonrasib, a new pancreatic-cancer pill) —
  and a muted credit line at the bottom.

## Palette and type
- Warm paper background, navy ink, gold rules, one red reserved for the
  lead kicker and one accent colour per panel (green, teal) so each story
  is findable at a glance.
- DejaVu Serif Bold for the masthead (newspaper feel), DejaVu Sans for
  everything else — both are system fonts, no downloads, no assets.

## Rules the build follows
- Pure PIL, deterministic: no timestamps, no randomness, no network.
  Running `build_entry.py` twice produces byte-identical `entry.png`.
- No copyrighted assets: every element is a rectangle, line, or text
  drawn by the script.
- `main.py` only copies the built `entry.png` to `/output/entry.png`
  (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
