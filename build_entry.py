#!/usr/bin/env python3
"""Draw entry.png: one 1024x1024 image summing up 21 November 2026.

Pure PIL, deterministic (no timestamps, no randomness, no network).
Every panel is drawn from text and shapes only; no external assets.
Run: python3 build_entry.py  ->  writes entry.png next to this file.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024

PAPER = (246, 241, 231)      # warm paper
NAVY = (22, 35, 63)          # masthead + headlines
GOLD = (201, 162, 39)        # rules and accents
GOLD_LIGHT = (217, 184, 74)
INK = (26, 26, 26)
RED = (179, 38, 30)
GREEN = (30, 70, 52)
TEAL = (15, 76, 92)
WHITE = (255, 255, 255)
BORDER = (216, 210, 196)
MUTED = (90, 88, 80)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


TITLE_FONT = font("DejaVuSerif-Bold.ttf", 46)
DATE_FONT = font("DejaVuSans.ttf", 21)
KICKER_FONT = font("DejaVuSans-Bold.ttf", 20)
HEAD_FONT = font("DejaVuSans-Bold.ttf", 35)
PANEL_HEAD_FONT = font("DejaVuSans-Bold.ttf", 27)
BODY_FONT = font("DejaVuSans.ttf", 23)
PANEL_BODY_FONT = font("DejaVuSans.ttf", 21)
STAT_FONT = font("DejaVuSans-Bold.ttf", 34)
STAT_LABEL_FONT = font("DejaVuSans-Bold.ttf", 16)
FOOT_LABEL_FONT = font("DejaVuSans-Bold.ttf", 17)
FOOT_BODY_FONT = font("DejaVuSans.ttf", 18)
FOOTER_FONT = font("DejaVuSans.ttf", 16)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap to a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, text, cx, y, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 150], fill=NAVY)
    centered(d, "THE WORLD IN ONE IMAGE", W // 2, 26, TITLE_FONT, WHITE)
    d.rectangle([312, 100, 712, 103], fill=GOLD)
    centered(d, "SATURDAY, 21 NOVEMBER 2026", W // 2, 114, DATE_FONT,
             GOLD_LIGHT)

    # ---- Lead story ------------------------------------------------------
    d.rectangle([32, 170, 992, 545], fill=WHITE, outline=BORDER, width=2)
    d.text((56, 190), "LEAD  ·  WAR IN EUROPE", font=KICKER_FONT, fill=RED)
    head = wrap(d, "Russia's largest overnight assault: 400+ drones, "
                   "110 missiles hit Ukraine", HEAD_FONT, 904)
    draw_lines(d, head, 56, 224, HEAD_FONT, NAVY, 46)
    body = wrap(d, "Eight to nine people were killed in Kyiv and a bridge "
                   "was damaged. Two missiles and a drone fell in Poland — "
                   "Prime Minister Tusk called it a deliberate provocation.",
                BODY_FONT, 904)
    draw_lines(d, body, 56, 322, BODY_FONT, INK, 32)

    # Stat chips
    for x0, x1, num, label in (
            (56, 500, "400+", "DRONES LAUNCHED"),
            (524, 968, "110", "MISSILES LAUNCHED")):
        d.rectangle([x0, 452, x1, 524], fill=NAVY)
        centered(d, num, (x0 + x1) // 2, 460, STAT_FONT, WHITE)
        centered(d, label, (x0 + x1) // 2, 498, STAT_LABEL_FONT, GOLD_LIGHT)

    # ---- Middle row: two panels ------------------------------------------
    # Markets (left)
    d.rectangle([32, 565, 502, 810], fill=WHITE, outline=BORDER, width=2)
    d.rectangle([32, 565, 502, 606], fill=GREEN)
    d.text((52, 575), "MARKETS", font=KICKER_FONT, fill=WHITE)
    mhead = wrap(d, "AI sell-off deepens", PANEL_HEAD_FONT, 430)
    draw_lines(d, mhead, 52, 622, PANEL_HEAD_FONT, NAVY, 34)
    mbody = wrap(d, "S&P and Dow slide, down 3.7% on Friday — days after "
                    "Anthropic's $2 trillion IPO on Thursday.",
                 PANEL_BODY_FONT, 430)
    draw_lines(d, mbody, 52, 622 + len(mhead) * 34 + 12,
               PANEL_BODY_FONT, INK, 29)

    # UK-EU (right)
    d.rectangle([522, 565, 992, 810], fill=WHITE, outline=BORDER, width=2)
    d.rectangle([522, 565, 992, 606], fill=TEAL)
    d.text((542, 575), "UK–EU", font=KICKER_FONT, fill=WHITE)
    uhead = wrap(d, "Post-Brexit deal struck in Brussels",
                 PANEL_HEAD_FONT, 430)
    draw_lines(d, uhead, 542, 622, PANEL_HEAD_FONT, NAVY, 34)
    ubody = wrap(d, "PM Andy Burnham seals a new UK–EU agreement in "
                    "Brussels, opening a new chapter after Brexit.",
                 PANEL_BODY_FONT, 430)
    draw_lines(d, ubody, 542, 622 + len(uhead) * 34 + 12,
               PANEL_BODY_FONT, INK, 29)

    # ---- Footer: three briefs --------------------------------------------
    d.rectangle([32, 830, 992, 833], fill=GOLD)
    briefs = [
        (32, "PROTESTS", RED,
         "Gen Z protests sweep 25 European countries"),
        (357, "CLIMATE", TEAL,
         "COP31 climate talks open in Antalya"),
        (682, "HEALTH", GREEN,
         "Daraxonrasib: a new pill for pancreatic cancer"),
    ]
    for x, label, color, text in briefs:
        d.text((x, 848), label, font=FOOT_LABEL_FONT, fill=color)
        lines = wrap(d, text, FOOT_BODY_FONT, 290)
        draw_lines(d, lines, x, 876, FOOT_BODY_FONT, INK, 25)
    d.line([349, 848, 349, 950], fill=BORDER, width=2)
    d.line([674, 848, 674, 950], fill=BORDER, width=2)

    centered(d, "21 November 2026  ·  One day, one image  ·  make.fun",
             W // 2, 972, FOOTER_FONT, MUTED)

    img.save(OUT, format="PNG")
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
