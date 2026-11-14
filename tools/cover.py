# -*- coding: utf-8 -*-
"""Original stylised slot covers (glossy cartoon title over neon scene).
Not the providers' artwork — our own design using the game name."""
import math, random, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(__file__)
F_TITLE = os.path.join(HERE, "fonts", "luckiest-guy-latin-400-normal.woff")
F_SUB = os.path.join(HERE, "fonts", "lilita-one-latin-400-normal.woff")

# (bg dark, bg mid, accent glow, title top, title bottom, outline)
SCHEMES = {
 "candy":  ((40,6,60),(150,30,140),(255,120,220),(255,240,120),(255,70,170),(70,0,60)),
 "gold":   ((30,12,4),(120,60,10),(255,200,90),(255,250,190),(240,150,20),(60,20,0)),
 "ocean":  ((2,18,45),(10,90,150),(90,220,255),(220,255,255),(40,170,255),(0,30,70)),
 "fire":   ((35,4,4),(150,30,10),(255,140,40),(255,240,140),(255,80,20),(60,0,0)),
 "jungle": ((4,28,12),(20,110,50),(160,255,120),(250,255,170),(90,210,60),(0,45,10)),
 "night":  ((10,4,35),(60,20,130),(160,110,255),(240,230,255),(170,120,255),(25,0,60)),
 "egypt":  ((25,14,4),(110,70,20),(255,210,120),(255,245,200),(220,160,40),(55,25,0)),
 "ice":    ((6,16,40),(40,80,150),(170,220,255),(255,255,255),(130,200,255),(10,30,80)),
 "horror": ((8,2,2),(70,8,12),(255,40,40),(255,220,200),(210,20,30),(20,0,0)),
 "neon":   ((10,0,30),(80,0,120),(0,255,230),(255,255,255),(0,230,255),(40,0,80)),
}
THEME_SCHEME = {"Mythology":"gold","Fruit":"candy","Fishing":"ocean","Egypt":"egypt","Space":"neon","Adventure":"jungle",
 "Western":"fire","Aliens":"neon","Classic":"fire","Nature":"jungle","Animals":"gold","Ocean":"ocean","Horror":"horror",
 "Magic":"night","Asia":"fire","Sweets":"candy","Anime":"candy","Gems":"night","Aztec":"jungle","Mexico":"fire",
 "Pirates":"ocean","Ireland":"jungle","Samurai":"fire","Money":"gold","Vampires":"horror","Safari":"gold","Arthurian":"night",
 "Vikings":"ice","Fantasy":"night","Detective":"night","Extreme":"neon","Wrestling":"fire","Africa":"fire","Fairy Tales":"candy",
 "Crime":"night","Hawaii":"ocean"}
KEYWORDS = [("bass","ocean"),("fish","ocean"),("kraken","ocean"),("shark","ocean"),("pirate","ocean"),("aloha","ocean"),("atlantis","ocean"),
 ("sweet","candy"),("sugar","candy"),("candy","candy"),("fruit","candy"),("juicy","candy"),("jar","candy"),("bonbon","candy"),("berry","candy"),
 ("gold","gold"),("cash","gold"),("money","gold"),("riches","gold"),("bank","gold"),("midas","gold"),("olympus","gold"),("zeus","gold"),("athena","gold"),
 ("dead","egypt"),("egypt","egypt"),("giza","egypt"),("ra ","egypt"),("pharaoh","egypt"),("anubis","egypt"),("cleo","egypt"),("tut","egypt"),
 ("fire","fire"),("hot","fire"),("chilli","fire"),("dragon","fire"),("burn","fire"),("samurai","fire"),("wild west","fire"),("bandit","fire"),
 ("viking","ice"),("thor","ice"),("odin","ice"),("frozen","ice"),("snow","ice"),("xmas","ice"),("christmas","ice"),("winter","ice"),
 ("horror","horror"),("blood","horror"),("vampire","horror"),("zombie","horror"),("hell","horror"),("mental","horror"),("tombstone","horror"),("devil","horror"),
 ("jungle","jungle"),("aztec","jungle"),("gorilla","jungle"),("leprechaun","jungle"),("irish","jungle"),("clover","jungle"),("buffalo","jungle"),("rhino","jungle"),
 ("star","neon"),("space","neon"),("galaxy","neon"),("cosmic","neon"),("laser","neon"),("reactoonz","neon"),("crew","neon"),("rave","neon"),
 ("princess","candy"),("moon","night"),("magic","night"),("witch","night"),("mystery","night"),("wolf","night"),("night","night")]

def pick_scheme(name, theme=None):
    if theme in THEME_SCHEME: return THEME_SCHEME[theme]
    l = " " + name.lower() + " "
    for k, v in KEYWORDS:
        if k in l: return v
    return list(SCHEMES)[sum(map(ord, name)) % len(SCHEMES)]

def _lerp(a, b, t): return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def _background(W, H, sc, rnd):
    dark, mid, glow = sc[0], sc[1], sc[2]
    img = Image.new("RGB", (W, H), dark)
    # radial glow
    rad = Image.radial_gradient("L").resize((W*2, H*2))
    rad = rad.crop((W//2, int(H*0.35), W//2+W, int(H*0.35)+H))
    midimg = Image.new("RGB", (W, H), mid)
    img = Image.composite(img, midimg, rad)
    # light rays
    rays = Image.new("L", (W, H), 0); d = ImageDraw.Draw(rays)
    cx, cy = W/2, H*0.42; n = 14; off = rnd.random()
    for i in range(n):
        a1 = (i+off)/n*2*math.pi; a2 = a1 + math.pi/n*0.55; R = max(W, H)*1.2
        d.polygon([(cx,cy),(cx+R*math.cos(a1),cy+R*math.sin(a1)),(cx+R*math.cos(a2),cy+R*math.sin(a2))], fill=38)
    rays = rays.filter(ImageFilter.GaussianBlur(6))
    img = Image.composite(Image.new("RGB",(W,H),glow), img, rays)
    # bokeh + sparkles
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); od = ImageDraw.Draw(ov)
    for _ in range(14):
        r = rnd.randint(6, 34); x = rnd.randint(0, W); y = rnd.randint(0, H)
        od.ellipse([x-r,y-r,x+r,y+r], fill=glow+(rnd.randint(25,70),))
    ov = ov.filter(ImageFilter.GaussianBlur(3))
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    od = ImageDraw.Draw(img)
    for _ in range(18):
        x = rnd.randint(0, W); y = rnd.randint(0, H); s = rnd.randint(1, 3)
        od.line([(x-s*3,y),(x+s*3,y)], fill=(255,255,255,200)); od.line([(x,y-s*3),(x,y+s*3)], fill=(255,255,255,200))
    # stage arc (like slot frames)
    arc = Image.new("RGBA", (W, H), (0,0,0,0)); ad = ImageDraw.Draw(arc)
    ad.ellipse([-W*0.3, H*0.78, W*1.3, H*1.6], fill=glow+(70,))
    ad.ellipse([-W*0.3, H*0.82, W*1.3, H*1.64], fill=dark+(255,))
    ad.ellipse([-W*0.3, -H*0.62, W*1.3, H*0.08], outline=glow+(120,), width=max(3, W//90))
    arc = arc.filter(ImageFilter.GaussianBlur(1.5))
    img = Image.alpha_composite(img, arc)
    # vignette
    vig = Image.radial_gradient("L").resize((W, H)).point(lambda v: int(v*0.75))
    img = Image.composite(Image.new("RGBA",(W,H),(0,0,0,255)), img, vig)
    return img

def _wrap(draw, text, font, maxw):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def _title(img, name, sc, box):
    W, H = img.size; x0, y0, x1, y1 = box; maxw = x1-x0; maxh = y1-y0
    probe = ImageDraw.Draw(img)
    text = name.upper().replace("’", "'")
    for size in range(int(maxh*0.42), 14, -2):
        f = ImageFont.truetype(F_TITLE, size)
        lines = _wrap(probe, text, f, maxw)
        lh = int(size*1.02)
        if len(lines) <= 4 and lh*len(lines) <= maxh and all(probe.textlength(l, font=f) <= maxw for l in lines): break
    total = lh*len(lines); top = y0 + (maxh-total)//2
    mask = Image.new("L", (W, H), 0); md = ImageDraw.Draw(mask)
    for i, l in enumerate(lines):
        tw = probe.textlength(l, font=f); md.text(((W-tw)/2, top+i*lh), l, font=f, fill=255)
    stroke = max(3, size//9)
    out = mask.filter(ImageFilter.MaxFilter(stroke*2+1))
    glow = out.filter(ImageFilter.GaussianBlur(size/4))
    img = Image.composite(Image.new("RGBA",(W,H),sc[2]+(255,)), img, glow.point(lambda v: int(v*0.9)))
    shadow = ImageChops.offset(out, 0, max(3,size//10))
    img = Image.composite(Image.new("RGBA",(W,H),(0,0,0,255)), img, shadow)
    img = Image.composite(Image.new("RGBA",(W,H),sc[5]+(255,)), img, out)
    # gradient fill per line
    grad = Image.new("RGBA", (W, H))
    gd = ImageDraw.Draw(grad)
    for i in range(len(lines)):
        ly = top + i*lh
        for y in range(lh+4):
            gd.line([(0, ly+y), (W, ly+y)], fill=_lerp(sc[3], sc[4], min(1, y/lh*1.15))+(255,))
    img = Image.composite(grad, img, mask)
    # glossy highlight on upper part of letters
    hl = Image.new("L", (W, H), 0); hd = ImageDraw.Draw(hl)
    for i in range(len(lines)):
        ly = top + i*lh; hd.rectangle([0, ly+int(lh*0.08), W, ly+int(lh*0.38)], fill=120)
    hl = ImageChops.multiply(hl, mask.filter(ImageFilter.MinFilter(3)))
    img = Image.composite(Image.new("RGBA",(W,H),(255,255,255,255)), img, hl)
    return img

def render(name, provider, out, W=400, H=300, theme=None):
    rnd = random.Random(name)
    sc = SCHEMES[pick_scheme(name, theme)]
    img = _background(W, H, sc, rnd)
    pad = int(W*0.07)
    img = _title(img, name, sc, (pad, int(H*0.10), W-pad, int(H*0.80)))
    d = ImageDraw.Draw(img); sf = ImageFont.truetype(F_SUB, max(14, W//22))
    p = provider; tw = d.textlength(p, font=sf); th = sf.size
    y = int(H*0.86)
    d.rounded_rectangle([(W-tw)/2-12, y-4, (W+tw)/2+12, y+th+6], radius=(th+10)//2, fill=(0,0,0,150), outline=sc[2]+(160,), width=1)
    d.text(((W-tw)/2, y), p, font=sf, fill=(255,255,255,235))
    img.convert("RGB").save(out, "JPEG", quality=84, optimize=True)
