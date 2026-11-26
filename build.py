"""Draws the front page for Wednesday 25 November 2026 and saves entry.png.

Run on the build machine (needs Pillow): python3 build.py
main.py, which the grader runs, only copies the finished entry.png.
"""
from PIL import Image, ImageDraw, ImageFont

from stories import DAY, LEADS, CARDS, BRIEFS, DATE_CHECK, REGION_COLORS

W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/noto/"
INK = (22, 24, 30)
PAPER = (247, 243, 233)
CARD = (255, 255, 255)
GREY = (95, 98, 105)
LABEL_COLORS = {"OFFICIAL": (20, 120, 70), "REPORTED": (60, 80, 150), "CLAIM": (180, 90, 0)}


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name + ".ttf", size)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, width, fill, gap=2, max_lines=9):
    x, y = xy
    step = fnt.size + gap
    for line in wrap(draw, text, fnt, width)[:max_lines]:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def tag(draw, x, y, text, color, fnt):
    w = int(draw.textlength(text, font=fnt)) + 10
    draw.rectangle([x, y, x + w, y + fnt.size + 5], fill=color)
    draw.text((x + 5, y + 1), text, font=fnt, fill=(255, 255, 255))
    return x + w + 4


# ---- small drawn scenes -------------------------------------------------
def scene(draw, kind, box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    w, h = x1 - x0, y1 - y0
    if kind == "rocket":
        draw.rectangle(box, fill=(18, 26, 60))
        for i, (sx, sy) in enumerate([(12, 14), (40, 30), (70, 10), (88, 44), (25, 60), (60, 70), (82, 80)]):
            px, py = x0 + w * sx // 100, y0 + h * sy // 100
            draw.ellipse([px, py, px + 2, py + 2], fill=(255, 255, 255))
        # station: body with two solar wings
        draw.rectangle([x0 + w * 55 // 100, cy - 8, x0 + w * 80 // 100, cy + 8], fill=(210, 214, 222))
        draw.rectangle([x0 + w * 82 // 100, cy - 20, x0 + w * 95 // 100, cy + 20], fill=(70, 120, 200))
        draw.rectangle([x0 + w * 60 // 100, cy - 30, x0 + w * 75 // 100, cy - 10], fill=(70, 120, 200))
        # capsule approaching
        draw.polygon([(x0 + w * 20 // 100, cy), (x0 + w * 32 // 100, cy - 12), (x0 + w * 46 // 100, cy - 12),
                      (x0 + w * 46 // 100, cy + 12), (x0 + w * 32 // 100, cy + 12)], fill=(240, 240, 240))
        draw.polygon([(x0 + w * 6 // 100, cy), (x0 + w * 20 // 100, cy - 7), (x0 + w * 20 // 100, cy + 7)],
                     fill=(255, 170, 40))
        draw.line([x0 + w * 46 // 100, cy, x0 + w * 55 // 100, cy], fill=(255, 220, 90), width=2)
    elif kind == "tariff":
        draw.rectangle(box, fill=(232, 226, 240))
        cols = [(200, 60, 50), (40, 90, 170), (214, 130, 30), (30, 130, 80), (0, 140, 150)]
        n = 14
        bw = (w - 20) // n
        for i in range(n):
            bh = h * (35 + (i * 37) % 45) // 100
            bx = x0 + 10 + i * bw
            draw.rectangle([bx, y1 - 8 - bh, bx + bw - 3, y1 - 8], fill=cols[i % 5])
        draw.line([x0 + 6, y0 + h * 30 // 100, x1 - 6, y0 + h * 30 // 100], fill=color, width=3)
    elif kind == "chart":
        draw.rectangle(box, fill=(250, 232, 230))
        pts = [(0, 22), (14, 26), (28, 20), (42, 34), (56, 40), (70, 62), (84, 70), (100, 86)]
        line = [(x0 + 8 + (w - 16) * px // 100, y0 + h * py // 100) for px, py in pts]
        draw.line(line, fill=(190, 30, 30), width=5)
        ex, ey = line[-1]
        draw.polygon([(ex, ey + 8), (ex - 14, ey - 6), (ex + 4, ey - 12)], fill=(190, 30, 30))
    else:
        draw.rectangle(box, fill=tuple(min(255, c + 150) for c in color))
        r = min(w, h) // 2 - 6
        if kind == "ship":
            draw.polygon([(cx - r, cy + 2), (cx + r, cy + 2), (cx + r - 8, cy + 12), (cx - r + 8, cy + 12)], fill=INK)
            draw.rectangle([cx - 6, cy - 8, cx + 8, cy + 2], fill=INK)
            draw.polygon([(cx - 2, cy - 10), (cx + 4, cy - r), (cx + 10, cy - 10)], fill=(220, 80, 20))
        elif kind == "pen":
            draw.rectangle([cx - r, cy - r + 4, cx + r - 6, cy + r - 2], fill=CARD, outline=INK)
            for k in range(3):
                draw.line([cx - r + 5, cy - r + 11 + k * 6, cx + r - 12, cy - r + 11 + k * 6], fill=GREY, width=1)
            draw.line([cx + 2, cy + 6, cx + r, cy - r + 6], fill=color, width=4)
        elif kind == "door":
            draw.rectangle([cx - 10, cy - r, cx + 10, cy + r], fill=CARD, outline=INK, width=2)
            draw.polygon([(cx + 14, cy), (cx + r, cy), (cx + r - 7, cy - 6), (cx + r, cy), (cx + r - 7, cy + 6)],
                         outline=color, fill=color)
            draw.line([cx + 12, cy, cx + r, cy], fill=color, width=3)
        elif kind == "flame":
            draw.rectangle([cx - r, cy + 4, cx + r, cy + r], fill=GREY)
            draw.rectangle([cx - 4, cy - 6, cx + 4, cy + 4], fill=GREY)
            draw.polygon([(cx - 8, cy - 6), (cx, cy - r - 2), (cx + 8, cy - 6)], fill=(230, 90, 20))
        elif kind == "blast":
            pts = []
            for k in range(12):
                rr = r if k % 2 == 0 else r // 2
                import math
                a = k * math.pi / 6
                pts.append((cx + int(rr * math.cos(a)), cy + int(rr * math.sin(a))))
            draw.polygon(pts, fill=(60, 60, 66))
        elif kind == "up":
            draw.line([cx - r, cy + r - 4, cx - 4, cy + 2, cx + 4, cy + 8, cx + r - 2, cy - r + 6], fill=color, width=4)
            draw.polygon([(cx + r, cy - r + 2), (cx + r - 12, cy - r + 4), (cx + r - 2, cy - r + 14)], fill=color)
        elif kind == "vote":
            draw.rectangle([cx - r, cy, cx + r, cy + r], fill=color)
            draw.rectangle([cx - 8, cy - r, cx + 8, cy + 2], fill=CARD, outline=INK)
        elif kind == "gavel":
            draw.rectangle([cx - r, cy - r + 2, cx, cy - 4], fill=INK)
            draw.line([cx - 6, cy - 6, cx + r - 2, cy + r - 6], fill=INK, width=4)
            draw.rectangle([cx - r, cy + r - 6, cx + r, cy + r - 1], fill=color)
        elif kind == "cross":
            draw.rectangle([cx - 5, cy - r, cx + 5, cy + r], fill=(200, 30, 30))
            draw.rectangle([cx - r, cy - 5, cx + r, cy + 5], fill=(200, 30, 30))
        elif kind == "ball":
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CARD, outline=INK, width=2)
            draw.regular_polygon((cx, cy, r // 2), 5, fill=INK)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    f_mast = font("NotoSans-CondensedBlack", 60)
    f_sub = font("NotoSans-CondensedBold", 19)
    f_lead = font("NotoSans-CondensedBlack", 25)
    f_body = font("NotoSans-Condensed", 16)
    f_num = font("NotoSans-CondensedBlack", 34)
    f_tag = font("NotoSans-CondensedBold", 12)
    f_card = font("NotoSans-CondensedBold", 16)
    f_cnum = font("NotoSans-CondensedBlack", 21)
    f_brief = font("NotoSans-CondensedSemiBold", 14)
    f_small = font("NotoSans-Condensed", 12)

    # masthead
    d.rectangle([0, 0, W, 104], fill=INK)
    # the date is the most important thing on the page: fit it to the full width
    size = 90
    while d.textlength(DAY, font=font("NotoSans-CondensedBlack", size)) > W - 28:
        size -= 1
    f_mast = font("NotoSans-CondensedBlack", size)
    d.text((14, 74 - size - size // 8), DAY, font=f_mast, fill=(255, 255, 255))
    total = len(LEADS) + len(CARDS) + len(BRIEFS)
    counts = {}
    for s in LEADS + CARDS + BRIEFS:
        counts[s[0]] = counts.get(s[0], 0) + 1
    d.text((16, 76), "WORLD NEWS IN ONE IMAGE: %d STORIES, %d REGIONS · every item happened or was first reported on 25 Nov 2026 · times in UTC"
           % (total, len(counts)), font=f_sub, fill=(255, 214, 90))

    n = 0
    # three lead stories
    lw, ly, lh = 330, 112, 282
    for i, (reg, lab, head, detail, num, src, kind) in enumerate(LEADS):
        n += 1
        x = 12 + i * (lw + 5)
        col = REGION_COLORS[reg]
        d.rectangle([x, ly, x + lw, ly + lh], fill=CARD, outline=INK, width=2)
        scene(d, kind, (x + 2, ly + 2, x + lw - 2, ly + 92), col)
        d.rectangle([x + 2, ly + 2, x + 34, ly + 34], fill=col)
        d.text((x + 9, ly - 2), str(n), font=f_lead, fill=(255, 255, 255))
        d.text((x + lw - 8 - d.textlength(num, font=f_num), ly + 48), num, font=f_num, fill=(255, 255, 255),
               stroke_width=3, stroke_fill=INK)
        y = text_block(d, (x + 9, ly + 96), head, f_lead, lw - 18, INK, gap=0, max_lines=3)
        y = text_block(d, (x + 9, y + 6), detail, f_body, lw - 18, (50, 52, 60), gap=2, max_lines=4)
        tx = tag(d, x + 9, ly + lh - 23, reg, col, f_tag)
        tx = tag(d, tx, ly + lh - 23, lab, LABEL_COLORS[lab], f_tag)
        d.text((tx + 2, ly + lh - 23), "Source: " + src, font=f_small, fill=GREY)

    # ten mid cards, 5 x 2
    cw, ch, cy0 = 197, 132, 400
    for i, (reg, lab, head, num, src, kind) in enumerate(CARDS):
        n += 1
        x = 12 + (i % 5) * (cw + 4)
        y = cy0 + (i // 5) * (ch + 4)
        col = REGION_COLORS[reg]
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=INK, width=1)
        d.rectangle([x, y, x + cw, y + 5], fill=col)
        scene(d, kind, (x + 6, y + 11, x + 50, y + 51), col)
        d.text((x + 56, y + 6), str(n), font=f_small, fill=GREY)
        d.text((x + 56, y + 19), num, font=f_cnum, fill=col)
        text_block(d, (x + 6, y + 53), head, f_card, cw - 12, INK, gap=0, max_lines=3)
        tx = tag(d, x + 6, y + ch - 20, lab, LABEL_COLORS[lab], f_tag)
        d.text((tx + 2, y + ch - 20), reg + " · " + src, font=f_small, fill=GREY)

    # briefs, two columns
    by = 676
    d.rectangle([12, by, 700, by + 22], fill=INK)
    d.text((18, by + 1), "ALSO ON 25 NOVEMBER", font=f_sub, fill=(255, 255, 255))
    half = (len(BRIEFS) + 1) // 2
    for i, (reg, lab, head, src) in enumerate(BRIEFS):
        n += 1
        x = 12 + (i // half) * 346
        y = by + 28 + (i % half) * 31
        col = REGION_COLORS[reg]
        d.rectangle([x, y, x + 22, y + 26], fill=col)
        d.text((x + 11 - d.textlength(str(n), font=f_tag) / 2, y + 5), str(n), font=f_tag, fill=(255, 255, 255))
        line = wrap(d, head, f_brief, 314)[0]
        d.text((x + 27, y - 3), line, font=f_brief, fill=INK)
        d.text((x + 27, y + 13), reg + " · " + lab + " · " + src, font=f_small, fill=LABEL_COLORS[lab])

    # right column: region tally and date check
    rx = 712
    d.rectangle([rx, by, W - 12, by + 22], fill=INK)
    d.text((rx + 6, by + 1), "STORIES BY REGION", font=f_sub, fill=(255, 255, 255))
    y = by + 28
    top = max(counts.values())
    for reg in ["ASIA", "EUROPE", "AFRICA", "MIDEAST", "AMERICAS", "OCEANIA"]:
        c = counts.get(reg, 0)
        d.text((rx, y - 2), reg, font=f_tag, fill=INK)
        d.rectangle([rx + 66, y, rx + 66 + 190 * c // top, y + 13], fill=REGION_COLORS[reg])
        d.text((rx + 72 + 190 * c // top, y - 3), str(c), font=f_brief, fill=INK)
        y += 19
    y += 4
    d.rectangle([rx, y, W - 12, H - 62], fill=(255, 246, 214), outline=(180, 90, 0), width=2)
    d.text((rx + 8, y + 3), "DATE CHECK: LEFT OUT", font=f_sub, fill=(150, 70, 0))
    yy = y + 28
    for item in DATE_CHECK:
        d.text((rx + 8, yy), "x  " + item, font=f_brief, fill=INK)
        yy += 19

    # footer
    d.rectangle([0, H - 56, W, H], fill=INK)
    d.text((14, H - 54), "OFFICIAL = government, court, statistics body or final score   REPORTED = outlet's own reporting   "
           "CLAIM = one side's statement, unconfirmed", font=f_small, fill=(255, 255, 255))
    d.text((14, H - 37), "Sources: Reuters, AP, UEFA, Australian Bureau of Statistics, Politico, Euronews, Bloomberg, "
           "European Parliament. Nothing here is from before 25 November 2026.", font=f_small, fill=(255, 214, 90))
    d.text((14, H - 20), "World news of Wednesday 25 November 2026, drawn by code (build.py).", font=f_small,
           fill=(200, 200, 205))
    return img


if __name__ == "__main__":
    build().save("entry.png", optimize=True)
