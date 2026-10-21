"""White Hot's site art (2026-10-21), from territory drawn by the game's own map code:
the game repo's ``scripts/brand/render-territory`` bakes ground through the app's
``HeatField`` (the map's heat overlay) with its borders, the way the map draws it.

    # in the game repo (Reverdure):
    swiftc -O -o /tmp/render-territory App/ReverdureApp/Map/HeatRamp.swift \
        App/ReverdureApp/Map/HeatField.swift App/ReverdureApp/Map/RoundedPath.swift \
        scripts/brand/render-territory/main.swift
    /tmp/render-territory 2400 1400 46 /tmp/territory-hero.png 7
    /tmp/render-territory 2400 1260 52 /tmp/territory-og.png 11
    # here:
    python3 tools/make_assets.py /tmp/territory-hero.png /tmp/territory-og.png

writes assets/territory.jpg (the hero's backdrop) and og-image.png (the link preview).
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUND = (10, 16, 23)        # the dark map's ground, as the app draws it


def font(size, weight):
    f = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)
    f.set_variation_by_name(weight)
    return f


def og_image(territory_path):
    w, h = 2400, 1260                    # supersampled 2x
    img = Image.open(territory_path).convert("RGB").resize((w, h), Image.LANCZOS)
    # The words sit on the cold side, left: fade the ground to the map's dark there.
    shade = Image.new("L", (w, h), 0)
    sd = ImageDraw.Draw(shade)
    for x in range(w):
        sd.line([(x, 0), (x, h)], fill=int(255 * max(0.0, 1 - x / (w * 0.6)) ** 1.3))
    img = Image.composite(Image.new("RGB", (w, h), GROUND), img, shade)
    d = ImageDraw.Draw(img)
    icon = Image.open(os.path.join(ROOT, "assets", "app-icon.png")).convert("RGB").resize((192, 192), Image.LANCZOS)
    m = Image.new("L", icon.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, *icon.size], radius=44, fill=255)
    img.paste(icon, (160, 300), m)
    d.text((160, 544), "White Hot", font=font(208, "Heavy"), fill=(246, 242, 236))
    d.text((168, 804), "Heat up your map.", font=font(88, "Semibold"), fill=(255, 140, 31))
    d.text((168, 932), "A territory game played with real workouts.", font=font(60, "Regular"),
           fill=(201, 196, 189))
    d.text((168, 1024), "iPhone + Apple Watch  \u00b7  Free beta", font=font(48, "Medium"), fill=(141, 135, 128))
    img.resize((1200, 630), Image.LANCZOS).save(os.path.join(ROOT, "og-image.png"), optimize=True)


def hero_backdrop(territory_path):
    img = Image.open(territory_path).convert("RGB")
    img.save(os.path.join(ROOT, "assets", "territory.jpg"), quality=82, optimize=True, progressive=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: make_assets.py <territory-hero.png> <territory-og.png>")
    hero_backdrop(sys.argv[1])
    og_image(sys.argv[2])
    print("wrote assets/territory.jpg and og-image.png")
