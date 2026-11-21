#!/usr/bin/env python3
"""Build a 1024x1024 front-page image summing up world news of Sat 21 Nov 2026.
Stories verified and supplied in DESIGN.md. Deterministic: fixed layout,
fixed text, no timestamps in output. All artwork drawn with PIL primitives
(text/lines/shapes) — no copyrighted assets."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint
INK = (18, 24, 38)        # near-black navy
NAVY = (24, 42, 84)
RED = (178, 34, 34)
GOLD = (198, 142, 32)
RULE = (120, 110, 90)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    for ln in wrap(draw, text, fnt, max_w):
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- outer frame ---
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=4)
d.rectangle([26, 26, W - 27, H - 27], outline=RULE, width=1)

# --- masthead ---
d.rectangle([26, 26, W - 27, 128], fill=NAVY)
d.text((512, 52), "THE WORLD IN ONE IMAGE", font=font(SERIF_B, 44),
       fill=(247, 243, 234), anchor="mt")
d.text((512, 104), "SATURDAY  •  21 NOVEMBER 2026", font=font(SANS_B, 22),
       fill=(212, 178, 90), anchor="mt")

# --- LEAD: Russia's mass attack on Ukraine ---
y = 150
d.text((52, y), "WAR  •  LEAD STORY", font=font(SANS_B, 24), fill=RED)
y += 34
y = para(d, 52, y, "Russia unleashes 400+ drones and 110 missiles on Ukraine",
         font(SERIF_B, 46), INK, 800, 54)
y += 10
y = para(d, 52, y,
         "At least 8\u20139 people are killed in Kyiv and a bridge is damaged in the "
         "biggest overnight barrage. Two Russian missiles and a drone fall in "
         "Poland; Prime Minister Tusk calls it a deliberate provocation.",
         font(SERIF, 24), INK, 800, 31)
# starburst glyph, right of lead
cx, cy = 905, 250
import math
for k in range(12):
    a = math.pi * k / 6
    x1 = cx + int(18 * math.cos(a))
    y1 = cy + int(18 * math.sin(a))
    x2 = cx + int(52 * math.cos(a))
    y2 = cy + int(52 * math.sin(a))
    d.line([(x1, y1), (x2, y2)], fill=GOLD, width=5)
d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=RED)

d.line([(52, 452), (972, 452)], fill=INK, width=3)

# --- Row 2: two tall panels ---
def panel(x0, y0, x1, y1, kicker, head, body, accent):
    d.rectangle([x0, y0, x1, y1], outline=INK, width=2)
    d.rectangle([x0, y0, x1, y0 + 40], fill=accent)
    d.text((x0 + 16, y0 + 8), kicker, font=font(SANS_B, 20), fill=(247, 243, 234))
    yy = para(d, x0 + 16, y0 + 56, head, font(SERIF_B, 30), INK, x1 - x0 - 32, 36)
    para(d, x0 + 16, yy + 8, body, font(SANS, 21), INK, x1 - x0 - 32, 27)


panel(52, 472, 500, 852, "MARKETS  •  AI SELL-OFF",
      "AI sell-off drags US stocks into correction",
      "The S&P 500 and Dow slide into correction as AI shares tumble; "
      "US stocks fall 3.7% on Friday \u2014 a day after Anthropic's IPO debuted "
      "at a $2 trillion valuation.",
      RED)
panel(524, 472, 972, 852, "UK\u2013EU  •  BRUSSELS",
      "UK and EU sign biggest post-Brexit deal",
      "Prime Minister Andy Burnham joins EU leaders in Brussels for a pact "
      "on food exports, carbon markets and youth mobility.",
      NAVY)

# small bar chart inside the markets panel (falling bars)
bx, by = 68, 812
heights = [58, 48, 38, 27, 17]
for i, h in enumerate(heights):
    d.rectangle([bx + i * 52, by - h, bx + i * 52 + 34, by], fill=RED)
d.line([(bx - 8, by), (bx + 5 * 52, by)], fill=INK, width=3)
d.text((bx, by + 12), "US STOCKS  \u22123.7%  FRIDAY", font=font(SANS_B, 18), fill=INK)

# small circle of stars inside the UK-EU panel
scx, scy = 748, 752
for k in range(12):
    a = math.pi * k / 6 - math.pi / 2
    sx = scx + int(55 * math.cos(a))
    sy = scy + int(55 * math.sin(a))
    d.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=GOLD)
d.text((748, 820), "SIGNED IN BRUSSELS", font=font(SANS_B, 18), fill=INK, anchor="mt")

# --- footer ---
d.line([(52, 872), (972, 872)], fill=INK, width=2)
d.text((512, 886), "ALSO: Gen Z protests sweep 25 European countries  •  COP31 in Antalya stalls over fossil fuels",
       font=font(SANS, 18), fill=INK, anchor="mt")
d.text((512, 914), "Pancreatic cancer drug daraxonrasib leaves tumours undetectable in 1 of 12 patients",
       font=font(SANS, 18), fill=INK, anchor="mt")
d.text((512, 952), "Sources: verified news reports of 21 November 2026  •  See DESIGN.md",
       font=font(SANS, 16), fill=RULE, anchor="mt")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png")
