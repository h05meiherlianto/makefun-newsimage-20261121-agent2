# news-image-20261121 — DESIGN.md

Bounty: "Sum up 21 November's world news in one image", $100,
deadline **2026-11-23T00:00:00Z = Senin 23 Nov 2026 07:00 WIB**.
Deliverable: public GitHub repo (owner h05meiherlianto, created after the
competition opened 21 Nov 2026 07:00 WIB, MIT licence) with main.py
(Python 3.13) at root writing /output/entry.png; the simplest allowed
program copies the stored image. Image: PNG, max 1 MiB, max 1024x1024,
no network, program run twice must write identical bytes.

## Stories (verified, supplied by parent — see task brief)
1. LEAD — Russia launches a mass overnight attack on Ukraine: 400+
   drones and 110 missiles, at least 8–9 killed in Kyiv, a bridge damaged.
   Two Russian missiles and one drone fall in Poland; Polish PM Tusk calls
   it a deliberate provocation.
2. MARKETS — AI stock sell-off pushes the S&P 500 and Dow into correction;
   US stocks down 3.7% on Friday (context: Anthropic IPO debuted Thursday
   at a $2 trillion valuation).
3. UK–EU — Britain and the EU sign the biggest post-Brexit deal in
   Brussels; PM Andy Burnham + EU leaders; food exports, carbon markets,
   youth mobility.
4. Footer — Gen Z protests in 25 European countries; COP31 climate summit
   in Antalya stalls over fossil fuels; daraxonrasib pancreatic-cancer
   drug — tumours undetectable in 1 of 12 patients.
   (Deliberately NOT leading with the ICJ Myanmar genocide ruling — that
   was yesterday's image.)

## Layout (1024x1024, newsprint front page, PIL + DejaVu system fonts)
- Masthead: navy band, "THE WORLD IN ONE IMAGE" + "SATURDAY • 21 NOVEMBER 2026".
- Lead story across the full width with a drawn starburst glyph (no
  copyrighted assets — all panels drawn from text/lines).
- Two side-by-side panels: MARKETS (with a small drawn bar chart) and
  UK–EU (with a small drawn circle of stars).
- Footer strip with the three short items above, over two lines.
- Text sized to stay legible at ~300px judging size; all copy wrapped
  to fit its panel, no overflow.

## Build
- `build_entry.py` draws entry.png deterministically (fixed layout/text,
  no timestamps). Run twice; md5 must match.
- `main.py` copies entry.png to /output/entry.png. Run twice; output
  bytes must match.
- Kit init, LICENSE MIT, README with the three live make.fun badges.
