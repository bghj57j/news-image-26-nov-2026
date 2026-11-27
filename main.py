# News-image entry for make.fun: Thursday 26 November 2026, 36 stories.
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024

BG = (255, 255, 255)
INK = (23, 35, 49)
MUTED = (74, 88, 101)
NAVY = (18, 43, 68)
RULE = (220, 227, 232)
ACCENTS = {
    "North America": (31, 91, 145),
    "Europe": (100, 73, 145),
    "Middle East": (174, 70, 46),
    "Russia-Ukraine": (142, 91, 36),
    "Asia-Pacific": (0, 119, 125),
    "Africa": (38, 112, 75),
    "Latin America": (183, 105, 28),
    "Business / Tech / Science": (69, 91, 111),
}


# Load bundled fonts relative to this script; grader images may lack system fonts.
def font(bold, size):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(HERE, name), size)


TITLE_FONT = font(True, 42)
SUBTITLE_FONT = font(False, 18)
REGION_FONT = font(True, 17)
STORY_FONT = font(False, 14)
NUM_FONT = font(True, 11)

# Each entry below is a distinct event dated 26 November 2026. The four
# stories dated 25 November in the research list are intentionally excluded.
REGIONS = [
    ("North America", [
        (1, "US coasts: Thanksgiving storms; 800,000+ without power, 1,000+ flights disrupted"),
        (2, "US: FinCEN confirms cyber breach; CISA adds 10 critical vulnerabilities"),
        (3, "Washington: Pentagon warns munitions rebuild will take years; $25bn allocated"),
        (4, "UK / Hormuz: US removes Iran-strike bombers; Iran tightens northern sea lane"),
        (5, "US: Markets shut for Thanksgiving; Friday trading is a half-day"),
    ]),
    ("Europe", [
        (6, "Brussels: Spain’s Pablo Hernández de Cos picked to lead ECB in February 2027"),
        (7, "Brussels: EU leaders fail to agree 2028–34 budget; talks resume 17 December"),
        (8, "Ibiza: Med Emre tanker capsizes; 1 dead, 17 rescued, up to 7,000 tonnes of diesel"),
        (9, "Serbia: New presidential election set for 27 December"),
        (10, "Italy: Government scolds Ukraine over strikes off Libya"),
        (11, "Bangkok: Refinery blast reported"),
        (12, "Israel: Gadi Eisenkot reaches coalition deal as government talks continue"),
    ]),
    ("Middle East", [
        (13, "Kuwait: Drone strike kills 2 Italian technicians; 4 hurt; Iran denies involvement"),
        (14, "Jazan, Saudi Arabia: Houthi refinery strike kills 1; Saudi Arabia says 50 targets hit"),
        (15, "Gaza: Strikes kill about 9; 19 Palestinians dead in 48 hours despite ceasefire"),
        (16, "Israel: US envoy Jared Kushner urges a change of course"),
        (17, "Oil: Brent rises 3.5% to about $94.61/barrel amid Houthi attack risks"),
        (18, "Saudi Arabia: Projectile hits Jizan port; drones and missiles intercepted near 3 cities"),
    ]),
    ("Russia-Ukraine", [
        (19, "Ukraine: Air defences say 87 Russian missiles and drones downed overnight"),
        (20, "Russia: Ukraine says it hit 15 refineries in November; 112 drones launched overnight"),
    ]),
    ("Asia-Pacific", [
        (21, "Asia: Nikkei +1.3%, KOSPI +1.2%, Hang Seng +1.9%, Taiex +2.6% on Thursday"),
        (22, "Philippines: Coast Guard commissions 3 patrol ships; Taiwan spy case draws 6-year term"),
        (23, "Sri Lanka: Women win Emerging Nations Trophy, beating Ireland by 6 wickets"),
        (24, "Mumbai: 18th-anniversary memorial for 26/11 attacks at Taj Hotel"),
        (25, "Beijing / Brasília: China and Brazil push back on Washington’s new tariff list"),
    ]),
    ("Africa", [
        (26, "DR Congo: Ebola cases top 12,000, deaths near 5,900; responders evacuate amid fighting"),
        (27, "Sudan: Drone attacks kill at least 15 in Blue Nile state"),
        (28, "Africa: Lower-cost, twice-yearly HIV-prevention shot lenacapavir begins rollout"),
        (29, "Haiti: Nearly 4.9 million face growing health needs amid gang violence and displacement"),
    ]),
    ("Latin America", [
        (30, "Venezuela: Edmundo González announces return after 2 years in Spanish exile"),
        (31, "Brazil: Budget panel cuts US$370 million in spending"),
        (32, "Paraguay: Thousands protest gender violence and effects of banking crisis"),
        (33, "Colombia: Marks 10 years since FARC peace deal; Catholic Church pledges continued role"),
        (34, "Peru: Gas deal to reach 15 cities in 7 Andean regions; construction starts in 2027"),
    ]),
    ("Business / Tech / Science", [
        (35, "Global: UN says seaborne trade stagnates as conflict and climate disruption deepen"),
        (36, "Giza, Egypt: Tanker-fire toll rises to 31 dead and 21 injured; driver detained"),
    ]),
]


def wrap(text, max_width, draw):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if draw.textlength(candidate, font=STORY_FONT) <= max_width:
            current = candidate
        else:
            if not current:
                raise ValueError("A story word is wider than the text column")
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise ValueError("Story exceeds the two-line layout: " + text)
    return lines


def draw_region(draw, x, y, width, name, stories):
    color = ACCENTS[name]
    draw.rounded_rectangle((x, y, x + width, y + 25), radius=5, fill=(242, 246, 249))
    draw.rounded_rectangle((x, y, x + 5, y + 25), radius=2, fill=color)
    draw.text((x + 13, y + 2), name, font=REGION_FONT, fill=NAVY)
    count = str(len(stories))
    count_width = draw.textlength(count, font=NUM_FONT)
    draw.text((x + width - count_width - 11, y + 7), count, font=NUM_FONT, fill=MUTED)
    y += 31
    for number, text in stories:
        lines = wrap(text, width - 48, draw)
        dot_y = y + 4
        draw.ellipse((x + 2, dot_y, x + 22, dot_y + 20), fill=color)
        label = str(number)
        label_width = draw.textlength(label, font=NUM_FONT)
        draw.text((x + 12 - label_width / 2, dot_y + 4), label, font=NUM_FONT, fill=BG)
        for line_no, line in enumerate(lines):
            draw.text((x + 31, y + line_no * 17), line, font=STORY_FONT, fill=INK)
        y += max(25, len(lines) * 17 + 4)
    return y


image = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(image)

# The title names the exact day; the subtitle frames the one-page summary.
draw.rectangle((0, 0, W, 131), fill=NAVY)
draw.text((30, 13), "Thursday 26 November 2026", font=TITLE_FONT, fill=BG)
draw.text((33, 72), "THE WORLD ON ONE PAGE", font=font(True, 17), fill=(191, 213, 231))
draw.text((33, 99), "36 dated stories  ·  8 regions", font=SUBTITLE_FONT, fill=BG)

left_regions = REGIONS[0:1] + REGIONS[2:3] + REGIONS[6:7] + REGIONS[7:8]
right_regions = REGIONS[1:2] + REGIONS[3:6]
margin = 25
col_gap = 24
col_width = (W - 2 * margin - col_gap) // 2
for x, groups in ((margin, left_regions), (margin + col_width + col_gap, right_regions)):
    y = 148
    for index, (name, stories) in enumerate(groups):
        y = draw_region(draw, x, y, col_width, name, stories)
        if index < len(groups) - 1:
            y += 10

# A quiet baseline keeps the footer clear of the story columns.
draw.line((25, 1002, 999, 1002), fill=RULE, width=1)
draw.text((30, 1007), "THURSDAY · 26 NOVEMBER 2026", font=font(True, 10), fill=MUTED)
draw.text((833, 1007), "WORLD / 01", font=font(True, 10), fill=MUTED)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
image.save(os.path.join(output_dir, "entry.png"), format="PNG", optimize=True)
print("saved entry.png")
