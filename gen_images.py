#!/usr/bin/env python3
"""Generate themed slot thumbnail images for all slots, live games, etc."""
from PIL import Image, ImageDraw, ImageFont
import os, math, random

random.seed(42)  # Reproducible

W, H = 400, 300
IMG_DIR = "/home/claude/slotoro-site/img"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def make_gradient(draw, w, h, c1, c2, c3):
    """Draw a 3-color diagonal gradient."""
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.6 + y / h * 0.4)
            if t < 0.5:
                c = lerp_color(c1, c2, t * 2)
            else:
                c = lerp_color(c2, c3, (t - 0.5) * 2)
            draw.point((x, y), fill=c)

def add_decorations(draw, w, h, accent):
    """Add subtle geometric decorations."""
    # Circles
    for _ in range(5):
        cx = random.randint(0, w)
        cy = random.randint(0, h)
        r = random.randint(20, 80)
        alpha_col = tuple(min(255, c + 30) for c in accent)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(*alpha_col, 25), width=1)

    # Diamond shapes
    for _ in range(3):
        cx = random.randint(0, w)
        cy = random.randint(0, h)
        s = random.randint(10, 30)
        pts = [(cx, cy-s), (cx+s, cy), (cx, cy+s), (cx-s, cy)]
        draw.polygon(pts, outline=(*accent, 35))

    # Top light reflection
    for y in range(int(h * 0.4)):
        alpha = int(15 * (1 - y / (h * 0.4)))
        draw.line([(0, y), (w, y)], fill=(255, 255, 255, alpha))

def generate_card(name, subtitle, emoji, colors, filename, subdir="slots"):
    """Generate a single card image."""
    outdir = os.path.join(IMG_DIR, subdir)
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, filename)

    img = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    # Gradient background
    c1, c2, c3 = colors
    # Fast gradient using horizontal bands
    for y in range(H):
        t = y / H
        if t < 0.5:
            c = lerp_color(c1, c2, t * 2)
        else:
            c = lerp_color(c2, c3, (t - 0.5) * 2)
        # Add horizontal variation
        for x in range(W):
            xt = x / W * 0.3
            final = lerp_color(c, c3, xt)
            draw.point((x, y), fill=final)

    add_decorations(draw, W, H, c2)

    # Emoji (large centered)
    try:
        emoji_font = ImageFont.truetype(FONT_BOLD, 56)
    except:
        emoji_font = ImageFont.load_default()

    # Title
    try:
        title_font = ImageFont.truetype(FONT_BOLD, 26 if len(name) < 20 else 20)
        sub_font = ImageFont.truetype(FONT_REG, 14)
    except:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    # Center text
    bbox = draw.textbbox((0, 0), name, font=title_font)
    tw = bbox[2] - bbox[0]

    # Position: emoji at top, name middle, subtitle below
    name_y = H // 2 - 5
    sub_y = name_y + 35

    # Shadow for text
    draw.text(((W - tw) // 2 + 1, name_y + 1), name, fill=(0, 0, 0, 180), font=title_font)
    draw.text(((W - tw) // 2, name_y), name, fill=(255, 255, 255, 230), font=title_font)

    bbox2 = draw.textbbox((0, 0), subtitle, font=sub_font)
    sw = bbox2[2] - bbox2[0]
    draw.text(((W - sw) // 2, sub_y), subtitle, fill=(255, 255, 255, 120), font=sub_font)

    # Bottom gradient overlay
    for y in range(H - 60, H):
        alpha = int(80 * ((y - (H - 60)) / 60))
        draw.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))

    # Save
    img = img.convert('RGB')
    img.save(outpath, 'JPEG', quality=85)
    return outpath

# ============================================================
# THEME COLORS (RGB tuples)
# ============================================================
theme_colors = {
    "Mythology": ((26,8,64), (48,32,160), (96,64,192)),
    "Egypt": ((42,24,0), (138,96,32), (192,144,48)),
    "Fruit": ((48,8,40), (160,32,96), (224,64,128)),
    "Fishing": ((0,24,48), (0,64,128), (0,128,192)),
    "Space": ((8,0,32), (16,16,160), (64,64,224)),
    "Western": ((42,16,0), (128,64,32), (192,96,48)),
    "Ocean": ((0,24,40), (0,56,96), (0,112,176)),
    "Adventure": ((16,32,0), (48,96,16), (80,160,32)),
    "Nature": ((8,24,8), (32,80,32), (64,160,64)),
    "Animals": ((24,16,8), (96,64,32), (160,96,48)),
    "Aliens": ((16,0,48), (64,32,160), (128,64,224)),
    "Classic": ((24,8,24), (80,32,80), (144,64,144)),
    "Horror": ((16,0,8), (64,0,24), (128,0,48)),
    "Fantasy": ((10,8,40), (48,32,128), (96,64,192)),
    "Vampires": ((24,0,8), (80,0,32), (144,0,64)),
    "Vikings": ((8,16,32), (32,48,96), (64,96,160)),
    "Asia": ((40,8,8), (128,32,32), (192,64,64)),
    "Pirates": ((16,8,24), (48,40,64), (96,88,128)),
    "Sweets": ((40,0,32), (128,32,96), (208,64,160)),
    "Anime": ((32,8,48), (96,32,160), (160,64,224)),
    "Samurai": ((24,0,16), (80,16,64), (160,32,128)),
    "Gems": ((16,8,40), (48,40,128), (80,72,192)),
    "Money": ((8,32,8), (32,96,32), (64,160,32)),
    "Ireland": ((0,24,8), (0,80,32), (0,160,64)),
    "Aztec": ((32,16,8), (96,64,32), (160,128,64)),
    "Mexico": ((40,8,8), (160,32,32), (224,64,64)),
    "Crime": ((10,10,24), (32,32,64), (64,64,128)),
    "Hawaii": ((0,32,32), (0,128,128), (0,192,192)),
    "Africa": ((32,16,8), (112,64,32), (176,128,64)),
    "Detective": ((16,16,32), (48,48,80), (96,96,144)),
    "Wrestling": ((32,8,8), (128,32,32), (192,64,64)),
    "Extreme": ((32,16,0), (128,96,0), (192,160,0)),
    "Arthurian": ((8,16,40), (32,48,96), (64,96,176)),
    "Safari": ((32,24,8), (128,96,48), (192,160,96)),
    "Fairy Tales": ((24,8,40), (80,32,128), (144,64,192)),
}
default_colors = ((10,8,40), (48,32,96), (96,64,160))

# ============================================================
# GENERATE ALL IMAGES
# ============================================================

# Import slot data from generate.py
import sys
sys.path.insert(0, '/home/claude/slotoro-site')

# Read the slots data
exec_globals = {}
with open('/home/claude/slotoro-site/generate.py', 'r') as f:
    code = f.read()
    # Extract just the data definitions (before functions)
    data_section = code.split('# ============================================================\n# HERO CARD')[0]
    exec(data_section, exec_globals)

slots_data = exec_globals['slots_data']
casinos = exec_globals['casinos']
live_games = exec_globals['live_games']

print(f"Generating images for {len(slots_data)} slots...")
count = 0
for s in slots_data:
    colors = theme_colors.get(s.get("theme", ""), default_colors)
    generate_card(s["name"], s["provider"], "", colors, f'{s["slug"]}.jpg', "slots")
    count += 1
    if count % 50 == 0:
        print(f"  {count} slots done...")

print(f"✅ {count} slot images generated")

# Live games
print(f"Generating images for {len(live_games)} live games...")
for g in live_games:
    generate_card(g["name"], "Spilavíti í beinni", "", ((10,8,40), (26,16,96), (48,32,144)), f'{g["slug"]}.jpg', "live")

print(f"✅ {len(live_games)} live game images generated")

# Top casinos
print(f"Generating images for top 20 casinos...")
for c in casinos[:20]:
    ctype_color = ((10,8,40), (40,20,128), (80,40,200)) if c["type"] == "crypto" else ((20,10,40), (60,30,100), (120,60,160))
    generate_card(c["name"], c["bonus"], "", ctype_color, f'{c["slug"]}.jpg', "casinos")

print("✅ Casino images generated")
print(f"\nTotal images in img/: ", end="")
os.system(f"find {IMG_DIR} -name '*.jpg' | wc -l")
