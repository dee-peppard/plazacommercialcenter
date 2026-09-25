#!/usr/bin/env python3
"""Generates the four unit landing pages (210ecota, 218ecota, 220ecota, 218-220ecota).

Source of truth for those pages: edit the PAGES data / CSS / template here, then run
    python3 tools/build_unit_pages.py
to rewrite <slug>/index.html for all four. Do not hand-edit the generated files.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.plazacommercialcenter.com"
PHONE_DISPLAY, PHONE_TEL = "(805) 681-2878", "+18056812878"
EMAIL = "management@plazacommercialcenter.com"

U = "/units"
PAGES = {
    "210": dict(
        slug="210ecota", nav="Unit 210", h1_num="210", sf="2,300", sf_note="Square Feet",
        ceiling="14′", avail="Available Now", avail_short="Available Now",
        subject="Leasing Inquiry: Unit 210",
        title="210 East Cota Street — 2,300 SF Commercial Space for Lease | Plaza Commercial Center",
        desc="Unit 210 at Plaza Commercial Center: 2,300 SF of flex office/showroom space in Santa Barbara's Lagoon District with 14-ft ceilings, arched brick entrance, reception, conference room and private parking. NNN lease.",
        tagline="A 2,300 SF single-story suite behind one of the Plaza's signature arched brick entrances — with 14-foot ceilings, exposed wood beams and signage visible from East Cota Street.",
        hero=f"{U}/210/210-interior-1.jpg", hero_pos="center 55%",
        thumb=f"{U}/210/210-interior-5.jpg",
        blurb="Showroom or office · reception entry · conference room",
        overview=[
            "Unit 210 is a 2,300 SF single-story suite on East Cota Street, set behind one of the Plaza's signature arched brick entrances. Fourteen-foot ceilings and exposed wood beams give the open floor the volume of a studio, and signage visible from East Cota Street gives your business real street presence.",
            "The current layout includes a reception entry, room for 15 desks, a large conference room, a wet pantry, two bathrooms (including a shower) and a large rear entry door — a natural fit for a showroom or office under C-M zoning. Private off-street parking is included, and the lease is NNN (triple net).",
        ],
        highlights=[
            "14-ft ceilings, signage visible from East Cota St.",
            "15 desks, large conference room, reception entry",
            "Wet pantry · 2 bathrooms · shower",
            "Large rear entry door · concrete floors",
            "Ideal for showroom or office · C-M zoning",
            "Private off-street parking included",
            "NNN / Triple Net lease",
        ],
        stats=[("2,300", "Square Feet"), ("14′", "Ceiling Height"), ("NNN", "Triple Net Lease"), ("Now", "Availability")],
        photos=[
            ("210/210-interior-1.jpg", "Open workspace under exposed beams", "Long open office in Unit 210 with exposed wood beam ceilings, ductwork and workstations"),
            ("210/210-interior-2.jpg", "Arched glass entry & reception", "Arched brick entry with glass storefront and reception desk in Unit 210"),
            ("210/210-interior-3.jpg", "Conference room", "Conference room with a long wood table and display shelves in Unit 210"),
            ("210/210-interior-4.jpg", "Wet pantry", "Wet pantry with white cabinetry, sink and counter in Unit 210"),
            ("210/210-interior-5.jpg", "Workstations along the brick wall", "Wood workstations beside an exposed brick wall and roll-up door in Unit 210"),
        ],
        renders=[
            ("210/210-Rendering-studio.jpeg", "Product design studio", "Concept rendering of Unit 210 as a product design studio with workbenches and a materials wall"),
            ("210/210Rendering-GallerySpace.jpeg", "Exhibition & gallery space", "Concept rendering of Unit 210 as an exhibition and product gallery"),
            ("210/210Rendering.jpeg", "Gallery walkway", "Concept rendering of Unit 210's long room leading to the brick arch, styled as a gallery walkway"),
            ("210/210Cota-EntranceRendering.jpg", "Entry facade concept", "Elevation sketch of the arched brick entry facade of Unit 210 with landscaping"),
        ],
        plan="210/210ECotaFloorPlan.png", plan_alt="Floor plan of Unit 210 showing open workspace, conference room, kitchen and two bathrooms",
        plan_title="Unit 210 Floor Plan",
        plan_text="2,300 SF single-story layout with a front reception entry, open work floor, conference room, kitchen/break area, two bathrooms and a rear entry. Existing furnished layout shown for reference.",
        plan_facts=[("Size", "2,300 SF"), ("Bathrooms", "2 (incl. shower)"), ("Rear access", "Large rear entry door"), ("Lease", "NNN / Triple Net")],
        plan_download="210ECotaFloorPlan.png", plan_download_name="Unit-210-East-Cota-Floor-Plan.png",
        others=["218", "220", "218-220"],
    ),
    "218": dict(
        slug="218ecota", nav="Unit 218", h1_num="218", sf="1,894", sf_note="Square Feet",
        ceiling="14′+", avail="Available October 1st", avail_short="Available October 1st",
        subject="Leasing Inquiry: Unit 218",
        title="218 East Cota Street — 1,894 SF Commercial Space for Lease | Plaza Commercial Center",
        desc="Unit 218 at Plaza Commercial Center: 1,894 SF of flex space in Santa Barbara's Lagoon District with 14-ft+ exposed wood beam ceilings, a 10-ft roll-up door and concrete floors. Available October 1st. NNN lease.",
        tagline="A 1,894 SF single-story suite with 14-foot-plus exposed wood beam ceilings, a brick wall and a large 10′ roll-up door — available October 1st.",
        hero=f"{U}/218/218-B.jpg", hero_pos="center 50%",
        thumb=f"{U}/218/218-B.jpg",
        blurb="10′ roll-up door · exposed beams · can combine with 220",
        overview=[
            "Unit 218 is a 1,894 SF single-story suite on East Cota Street with 14-foot-plus exposed wood beam ceilings, brick walls, concrete floors and a large 10′ roll-up door. It has two bathrooms and an open floor that can be set up as a studio, shop, showroom or office.",
            "Unit 218 is available October 1st. It can also be leased together with neighboring Unit 220 for 4,747 SF of contiguous space. The lease is NNN (triple net), and private off-street parking is included.",
        ],
        highlights=[
            "14-ft+ exposed wood beam ceilings",
            "Large 10′ roll-up door",
            "Two bathrooms",
            "Concrete floors",
            "Possible 4,747 SF contiguous with Unit 220",
            "Private off-street parking included",
            "NNN / Triple Net lease",
        ],
        stats=[("1,894", "Square Feet"), ("14′+", "Ceiling Height"), ("NNN", "Triple Net Lease"), ("Oct 1", "Availability")],
        photos=[
            ("218/218-A.jpg", "Interior view", "Interior of Unit 218 with exposed beams, brick wall and concrete floor"),
            ("218/218-B.jpg", "Interior view toward the roll-up door", "Interior of Unit 218 looking toward the open roll-up door"),
            ("shared/218-220-BathroomFinish.jpg", "Bathroom finishes", "Bathroom with wood-framed mirror and vanity, shared finish for Units 218 and 220"),
        ],
        renders=[
            ("218/218-Rendering.jpeg", "Design studio concept", "Concept rendering of Unit 218 as a design studio with a materials sample wall"),
        ],
        plan="shared/218-220-floorplan.png", plan_alt="Floor plan showing Unit 218 (1,894 SF) above Unit 220 (2,853 SF) as 4,747 SF of contiguous space",
        plan_title="Unit 218 Floor Plan",
        plan_text="Unit 218 (1,894 SF) is the upper suite on this plan, shown with neighboring Unit 220 (2,853 SF) — together 4,747 SF of contiguous space. The 10′ roll-up door is on the right wall.",
        plan_facts=[("Size", "1,894 SF"), ("Roll-up door", "10′ door"), ("Bathrooms", "2"), ("Lease", "NNN / Triple Net")],
        plan_download="218220ecota_floorplan.png", plan_download_name="Units-218-220-East-Cota-Floor-Plan.png",
        others=["210", "220", "218-220"],
    ),
    "220": dict(
        slug="220ecota", nav="Unit 220", h1_num="220", sf="2,853", sf_note="Square Feet",
        ceiling="14′+", avail="Available 30-60 Days Notice", avail_short="Available 30-60 Days Notice",
        subject="Leasing Inquiry: Unit 220",
        title="220 East Cota Street — 2,853 SF Commercial Space for Lease | Plaza Commercial Center",
        desc="Unit 220 at Plaza Commercial Center: 2,853 SF of flex space in Santa Barbara's Lagoon District with 14-ft+ exposed wood beam ceilings, a 10-ft roll-up door and its own street entrance. NNN lease.",
        tagline="Our largest available suite at 2,853 SF — 14-foot-plus exposed wood beam ceilings, a large 10′ roll-up door and its own street entrance.",
        hero=f"{U}/220/220-interior-2.jpg", hero_pos="center 60%",
        thumb=f"{U}/220/220-interior-2.jpg",
        blurb="Largest suite · own street entrance · 10′ roll-up door",
        overview=[
            "Unit 220 is the largest of the Plaza's available suites at 2,853 SF, with 14-foot-plus exposed wood beam ceilings, a brick back wall, concrete floors, a large 10′ roll-up door and its own street entrance. It's move-in ready with two bathrooms.",
            "Unit 220 is available with 30–60 days notice. It can also be leased together with neighboring Unit 218 for 4,747 SF of contiguous space. The lease is NNN (triple net), and private off-street parking is included.",
        ],
        highlights=[
            "14-ft+ exposed wood beam ceilings",
            "Large 10′ roll-up door",
            "Own street entrance",
            "Two bathrooms · move-in ready",
            "Concrete floors",
            "Possible 4,747 SF contiguous with Unit 218",
            "NNN / Triple Net lease",
        ],
        stats=[("2,853", "Square Feet"), ("14′+", "Ceiling Height"), ("NNN", "Triple Net Lease"), ("30–60", "Days Notice")],
        photos=[
            ("220/220-interior-1.jpg", "Open floor and glass entry door", "Unit 220 open floor with brick wall and glass entry door"),
            ("220/220-interior-2.jpg", "Exposed beam ceilings", "Unit 220 interior with exposed wood beam ceilings and brick back wall"),
            ("220/220-interior-3.jpg", "Open floor plan", "Unit 220 open concrete floor with brick wall"),
            ("220/220-Entrance-A.jpg", "Street entrance", "Brick exterior of Unit 220 with glass street entrance and accessible parking"),
            ("220/220-Entrance-B.jpg", "Roll-up door & parking", "Exterior roll-up door of Unit 220 beside the parking area"),
            ("shared/218-220-BathroomFinish.jpg", "Bathroom finishes", "Bathroom with wood-framed mirror and vanity, shared finish for Units 218 and 220"),
        ],
        renders=[
            ("220/220-Rendering.jpeg", "Architecture studio concept", "Concept rendering of Unit 220 as an architecture studio with drafting tables and models"),
            ("220/220-Rendering-Gallery.jpeg", "Gallery & showroom concept", "Concept rendering of Unit 220 as a gallery and showroom with exhibition walls"),
        ],
        plan="shared/218-220-floorplan.png", plan_alt="Floor plan showing Unit 220 (2,853 SF) below Unit 218 (1,894 SF) as 4,747 SF of contiguous space",
        plan_title="Unit 220 Floor Plan",
        plan_text="Unit 220 (2,853 SF) is the lower suite on this plan, shown with neighboring Unit 218 (1,894 SF) — together 4,747 SF of contiguous space. Roll-up door on the right wall; street entrance at the lower left.",
        plan_facts=[("Size", "2,853 SF"), ("Roll-up door", "10′ door"), ("Bathrooms", "2"), ("Lease", "NNN / Triple Net")],
        plan_download="218220ecota_floorplan.png", plan_download_name="Units-218-220-East-Cota-Floor-Plan.png",
        others=["210", "218", "218-220"],
    ),
    "218-220": dict(
        slug="218-220ecota", nav="218 + 220 Combined", h1_num="218–220", sf="4,747", sf_note="Contiguous SF",
        ceiling="14′+", avail="218: Oct 1st · 220: 30-60 Days Notice", avail_short="218: October 1st · 220: 30-60 Days Notice",
        subject="Leasing Inquiry: Units 218 & 220",
        title="218–220 East Cota Street — 4,747 SF Contiguous Commercial Space | Plaza Commercial Center",
        desc="Units 218 and 220 at Plaza Commercial Center combine for 4,747 SF of contiguous flex space in Santa Barbara's Lagoon District — 14-ft+ exposed wood beam ceilings, two 10-ft roll-up doors, private parking. NNN lease.",
        tagline="Two adjoining suites, one 4,747 SF space — 14-foot-plus exposed wood beam ceilings, two 10′ roll-up doors and room to build out a full studio, showroom or headquarters.",
        hero=f"{U}/220/220-interior-3.jpg", hero_pos="center 55%",
        thumb=f"{U}/220/220-interior-3.jpg",
        blurb="4,747 SF contiguous · Units 218 + 220 together",
        overview=[
            "Units 218 and 220 sit side by side on East Cota Street and can be leased together as 4,747 SF of contiguous space — 1,894 SF plus 2,853 SF — under 14-foot-plus exposed wood beam ceilings with brick walls and concrete floors.",
            "Each unit has its own large 10′ roll-up door and two bathrooms, and Unit 220 has its own street entrance. Unit 218 is available October 1st and Unit 220 is available with 30–60 days notice. Either unit can also be leased on its own. The lease is NNN (triple net), and private off-street parking is included.",
        ],
        highlights=[
            "4,747 SF contiguous (1,894 SF + 2,853 SF)",
            "14-ft+ exposed wood beam ceilings",
            "Two large 10′ roll-up doors (one per unit)",
            "Two bathrooms in each unit",
            "Concrete floors",
            "Private off-street parking included",
            "NNN / Triple Net lease",
        ],
        stats=[("4,747", "Contiguous SF"), ("14′+", "Ceiling Height"), ("NNN", "Triple Net Lease"), ("2 Units", "218 + 220")],
        photos=[
            ("218/218-A.jpg", "Unit 218 — interior view", "Interior of Unit 218 with exposed beams, brick wall and concrete floor"),
            ("218/218-B.jpg", "Unit 218 — toward the roll-up door", "Interior of Unit 218 looking toward the open roll-up door"),
            ("220/220-interior-1.jpg", "Unit 220 — open floor and glass entry", "Unit 220 open floor with brick wall and glass entry door"),
            ("220/220-interior-2.jpg", "Unit 220 — exposed beam ceilings", "Unit 220 interior with exposed wood beam ceilings and brick back wall"),
            ("220/220-interior-3.jpg", "Unit 220 — open floor plan", "Unit 220 open concrete floor with brick wall"),
            ("220/220-Entrance-A.jpg", "Unit 220 — street entrance", "Brick exterior of Unit 220 with glass street entrance and accessible parking"),
            ("220/220-Entrance-B.jpg", "Unit 220 — roll-up door & parking", "Exterior roll-up door of Unit 220 beside the parking area"),
            ("shared/218-220-BathroomFinish.jpg", "Bathroom finishes", "Bathroom with wood-framed mirror and vanity, shared finish for Units 218 and 220"),
        ],
        renders=[
            ("218/218-Rendering.jpeg", "Unit 218 — design studio concept", "Concept rendering of Unit 218 as a design studio with a materials sample wall"),
            ("220/220-Rendering.jpeg", "Unit 220 — architecture studio concept", "Concept rendering of Unit 220 as an architecture studio with drafting tables and models"),
            ("220/220-Rendering-Gallery.jpeg", "Unit 220 — gallery & showroom concept", "Concept rendering of Unit 220 as a gallery and showroom with exhibition walls"),
        ],
        plan="shared/218-220-floorplan.png", plan_alt="Floor plan showing Unit 218 (1,894 SF) and Unit 220 (2,853 SF) together as 4,747 SF of contiguous space",
        plan_title="Units 218 + 220 Floor Plan",
        plan_text="Unit 218 (1,894 SF) and Unit 220 (2,853 SF) side by side — 4,747 SF of contiguous space with a 10′ roll-up door on each unit and a street entrance for Unit 220.",
        plan_facts=[("Combined size", "4,747 SF"), ("Unit 218", "1,894 SF"), ("Unit 220", "2,853 SF"), ("Lease", "NNN / Triple Net")],
        plan_download="218220ecota_floorplan.png", plan_download_name="Units-218-220-East-Cota-Floor-Plan.png",
        others=["210", "218", "220"],
    ),
}

ORDER = ["210", "218", "220", "218-220"]
LABEL = {"210": "Unit 210", "218": "Unit 218", "220": "Unit 220", "218-220": "218 + 220 Combined"}
SF_LINE = {"210": "2,300 SF", "218": "1,894 SF", "220": "2,853 SF", "218-220": "4,747 SF contiguous"}

CSS = r"""
:root{--cream:#F6F1E9;--cream-dark:#EDE8DE;--warm-white:#FAF8F4;--dark:#252220;--dark-mid:#3A3530;--terracotta:#B86245;--terra-light:#D4896E;--sage:#6B7B5E;--sand:#C4B49A;--nav-h:72px}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--nav-h) + 60px)}
body{font-family:'DM Sans',sans-serif;background:var(--warm-white);color:var(--dark);-webkit-font-smoothing:antialiased}
img{max-width:100%}
a{color:inherit}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h);display:flex;justify-content:space-between;align-items:center;padding:0 52px;background:rgba(37,34,32,.96);backdrop-filter:blur(10px)}
.nav-logo{font-family:'Cormorant Garamond',serif;font-size:26px;font-weight:400;letter-spacing:.08em;color:var(--cream);text-decoration:none}
.nav-logo span{color:var(--terracotta)}
.nav-links{display:flex;gap:40px;list-style:none}
.nav-links a{font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:rgba(246,241,233,.6);text-decoration:none;transition:color .2s}
.nav-links a:hover{color:var(--cream)}
.nav-hamburger{display:none;flex-direction:column;justify-content:center;gap:6px;cursor:pointer;padding:4px;background:none;border:none}
.nav-hamburger span{display:block;width:26px;height:1.5px;background:var(--cream)}
.mobile-menu{display:none;position:fixed;inset:0;background:var(--dark);z-index:200;flex-direction:column;align-items:center;justify-content:center}
.mobile-menu.open{display:flex}
.mobile-menu-close{position:absolute;top:16px;right:24px;background:none;border:none;cursor:pointer;color:rgba(246,241,233,.5);font-size:32px;line-height:1;padding:4px 8px}
.mobile-menu a{font-family:'Cormorant Garamond',serif;font-size:38px;font-weight:300;color:rgba(246,241,233,.75);text-decoration:none;letter-spacing:.04em;padding:16px 0;border-bottom:1px solid rgba(246,241,233,.08);width:280px;text-align:center}
.mobile-menu a:hover{color:var(--terracotta)}
.mobile-menu a.mobile-menu-cta{margin-top:36px;background:var(--terracotta);color:#fff;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:16px 36px;border-bottom:none;width:auto}

/* HERO */
.hero{position:relative;min-height:88vh;display:flex;align-items:flex-end;padding:calc(var(--nav-h) + 64px) 52px 72px;background-size:cover;background-repeat:no-repeat;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:linear-gradient(to right,rgba(30,25,22,.84) 0%,rgba(30,25,22,.55) 60%,rgba(30,25,22,.3) 100%),radial-gradient(ellipse at 68% 38%,rgba(184,98,69,.12) 0%,transparent 55%)}
.hero-content{position:relative;max-width:720px}
.hero-eyebrow{font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:#E8A98F;margin-bottom:20px;text-shadow:0 1px 14px rgba(0,0,0,.65)}
.hero-title{font-family:'Cormorant Garamond',serif;font-size:clamp(52px,8vw,100px);font-weight:300;line-height:.95;color:var(--cream);margin-bottom:22px;letter-spacing:-.01em}
.hero-title em{font-style:italic;color:rgba(246,241,233,.55)}
.hero-badge{display:inline-block;font-size:12px;font-weight:500;letter-spacing:.2em;text-transform:uppercase;color:#fff;background:var(--terracotta);padding:9px 16px;margin-bottom:24px}
.hero-tagline{font-size:21px;font-weight:300;line-height:1.6;color:rgba(246,241,233,.9);max-width:600px;margin-bottom:38px}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap}
.btn-primary,.btn-ghost{display:inline-flex;align-items:center;gap:10px;padding:15px 30px;text-decoration:none;font-size:11px;letter-spacing:.15em;text-transform:uppercase;transition:all .2s}
.btn-primary{background:var(--terracotta);color:#fff;font-weight:500}
.btn-primary:hover{background:#a0553a}
.btn-ghost{border:1px solid rgba(246,241,233,.32);color:rgba(246,241,233,.8)}
.btn-ghost:hover{border-color:rgba(246,241,233,.65);color:var(--cream)}

/* UNIT SWITCHER */
.unit-switch{position:sticky;top:var(--nav-h);z-index:90;background:var(--dark-mid);border-bottom:1px solid rgba(246,241,233,.08)}
.switch-inner{display:flex;align-items:center;gap:8px;padding:12px 52px;overflow-x:auto;white-space:nowrap;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.switch-inner::-webkit-scrollbar{display:none}
.switch-label{font-size:10px;letter-spacing:.26em;text-transform:uppercase;color:var(--sand);margin-right:14px;flex-shrink:0}
.switch-inner a{flex-shrink:0;font-size:12px;letter-spacing:.14em;text-transform:uppercase;text-decoration:none;color:rgba(246,241,233,.7);border:1px solid rgba(246,241,233,.18);padding:10px 18px;transition:all .2s}
.switch-inner a:hover{color:#fff;border-color:rgba(246,241,233,.5)}
.switch-inner a[aria-current="page"]{background:var(--terracotta);border-color:var(--terracotta);color:#fff}

/* STATS */
.stats-bar{background:var(--terracotta);display:flex}
.stat{flex:1;padding:28px 20px;text-align:center;border-right:1px solid rgba(255,255,255,.18)}
.stat:last-child{border-right:none}
.stat-num{font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:300;color:#fff;line-height:1;margin-bottom:8px}
.stat-lbl{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.75)}

/* SECTIONS */
.section{padding:96px 52px}
.eyebrow{font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--terracotta);margin-bottom:14px}
.section-title{font-family:'Cormorant Garamond',serif;font-size:clamp(36px,4.5vw,56px);font-weight:300;line-height:1.08;color:var(--dark);margin-bottom:24px}
.rule{width:44px;height:1px;background:var(--terracotta);margin-bottom:36px}
.about{background:var(--cream-dark)}
.about-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:80px;align-items:start}
.body-copy{font-size:19px;font-weight:300;line-height:1.8;color:var(--dark-mid)}
.body-copy p+p{margin-top:20px}
.highlights{background:var(--warm-white);padding:36px 34px;border-top:3px solid var(--terracotta)}
.highlights h3{font-size:12px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;color:var(--terracotta);margin-bottom:20px}
.highlights ul{list-style:none;display:flex;flex-direction:column;gap:14px}
.highlights li{display:grid;grid-template-columns:20px 1fr;gap:10px;font-size:17px;font-weight:300;line-height:1.5;color:var(--dark-mid)}
.highlights li::before{content:'\2014';color:var(--terracotta);font-size:12px;margin-top:3px}

/* GALLERY */
.gallery{background:var(--warm-white)}
.gallery h3.sub{font-size:12px;font-weight:500;letter-spacing:.26em;text-transform:uppercase;color:var(--sage);padding-bottom:14px;border-bottom:2px solid var(--cream-dark);margin:0 0 18px}
.gallery h3.sub:not(:first-of-type){margin-top:56px}
.gallery .note{font-size:14px;font-weight:300;color:rgba(58,53,48,.65);margin:-4px 0 18px}
.g-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.g-item{margin:0}
.g-btn{display:block;width:100%;padding:0;border:none;background:var(--cream-dark);cursor:zoom-in;aspect-ratio:3/2;overflow:hidden}
.g-btn img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s}
.g-btn:hover img,.g-btn:focus-visible img{transform:scale(1.03)}
.g-item figcaption{font-size:14px;font-weight:300;line-height:1.4;color:var(--dark-mid);padding:10px 2px 0}

/* FLOOR PLAN */
.floorplan{background:var(--cream-dark)}
.plan-grid{display:grid;grid-template-columns:minmax(280px,480px) 1fr;gap:72px;align-items:start}
.plan-card{background:#fff;padding:20px;border:1px solid rgba(58,53,48,.08)}
.plan-card img{display:block;width:100%;height:auto}
.plan-facts{display:grid;grid-template-columns:1fr 1fr;gap:3px;margin:32px 0}
.fact{background:var(--warm-white);padding:18px 20px}
.fact dt{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--terracotta);margin-bottom:6px}
.fact dd{font-family:'Cormorant Garamond',serif;font-size:24px;color:var(--dark)}
.btn-dark{display:inline-flex;align-items:center;gap:10px;padding:15px 28px;text-decoration:none;font-size:11px;font-weight:500;letter-spacing:.15em;text-transform:uppercase;border:1px solid var(--terracotta);color:var(--terracotta);transition:all .2s}
.btn-dark:hover{background:var(--terracotta);color:#fff}
.plan-actions{display:flex;gap:12px;flex-wrap:wrap}

/* OTHER UNITS */
.others{background:var(--dark)}
.others .section-title{color:var(--cream)}
.others-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:48px}
.o-card{display:flex;flex-direction:column;background:var(--dark-mid);text-decoration:none;border-top:3px solid var(--terracotta);transition:transform .22s}
.o-card:hover{transform:translateY(-5px)}
.o-card img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}
.o-body{padding:28px 30px 32px}
.o-label{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--sand);margin-bottom:8px}
.o-sf{font-family:'Cormorant Garamond',serif;font-size:40px;font-weight:300;color:var(--cream);line-height:1.05;margin-bottom:10px}
.o-blurb{font-size:15px;font-weight:300;line-height:1.5;color:rgba(246,241,233,.62);margin-bottom:20px}
.o-link{font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--terracotta)}

/* EXPLORE */
.explore{background:var(--cream-dark)}
.explore-grid{display:grid;grid-template-columns:1fr 1fr;gap:3px;margin-top:8px}
.x-card{display:block;background:var(--warm-white);padding:40px 38px;text-decoration:none;border-left:3px solid var(--terracotta);transition:background .2s}
.x-card:hover{background:#fff}
.x-card h3{font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:400;color:var(--dark);margin-bottom:10px}
.x-card p{font-size:16px;font-weight:300;line-height:1.6;color:var(--dark-mid);margin-bottom:18px}
.x-card span{font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--terracotta)}

/* CONTACT */
.contact-section{background:var(--dark);display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;padding:96px 52px}
.contact-section .section-title{color:var(--cream)}
.contact-body{font-size:21px;font-weight:300;line-height:1.75;color:rgba(246,241,233,.55)}
.contact-cards{display:flex;flex-direction:column;gap:3px}
.contact-card{background:var(--dark-mid);padding:24px 30px}
.cc-lbl{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--sand);margin-bottom:8px}
.cc-val{font-family:'Cormorant Garamond',serif;font-size:22px;color:var(--cream);text-decoration:none;line-height:1.4;word-break:break-word}
a.cc-val:hover{color:var(--terracotta)}
.contact-cta{display:block;background:var(--terracotta);color:#fff;text-align:center;padding:20px 30px;text-decoration:none;font-size:11px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;margin-top:3px;transition:background .2s}
.contact-cta:hover{background:#a0553a}

/* FOOTER */
footer{background:#18160F;padding:34px 52px;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.footer-name{font-family:'Cormorant Garamond',serif;font-size:15px;color:rgba(246,241,233,.4);letter-spacing:.05em}
.footer-links{display:flex;gap:26px;flex-wrap:wrap}
.footer-links a{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:rgba(246,241,233,.4);text-decoration:none}
.footer-links a:hover{color:var(--cream)}
.footer-copy{font-size:11px;color:rgba(246,241,233,.25)}

/* LIGHTBOX */
.lb{display:none;position:fixed;inset:0;background:rgba(18,16,14,.97);z-index:300;flex-direction:column}
.lb.open{display:flex}
.lb-top{display:flex;justify-content:space-between;align-items:center;padding:20px 32px;border-bottom:1px solid rgba(246,241,233,.07)}
.lb-cap{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:300;color:rgba(246,241,233,.7)}
.lb-right{display:flex;align-items:center;gap:26px}
.lb-count{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:rgba(246,241,233,.3)}
.lb-close{background:none;border:none;color:rgba(246,241,233,.45);font-size:32px;line-height:1;cursor:pointer;padding:0 4px}
.lb-close:hover{color:var(--cream)}
.lb-stage{flex:1;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;padding:24px 88px;min-height:0}
.lb-stage img{max-width:100%;max-height:100%;object-fit:contain;display:block;user-select:none}
.lb-arrow{position:absolute;top:50%;transform:translateY(-50%);background:none;border:none;color:rgba(246,241,233,.35);font-size:64px;font-weight:200;line-height:1;cursor:pointer;padding:16px 20px;font-family:'Cormorant Garamond',serif}
.lb-arrow:hover{color:rgba(246,241,233,.9)}
.lb-prev{left:0}.lb-next{right:0}

/* RESPONSIVE */
@media (max-width:960px){
  :root{--nav-h:64px}
  nav{padding:0 24px}
  .nav-links{display:none}
  .nav-hamburger{display:flex}
  .hero{padding:calc(var(--nav-h) + 48px) 24px 56px;min-height:80vh}
  .switch-inner{padding:10px 24px}
  .stats-bar{flex-wrap:wrap}
  .stat{flex:1 1 50%;border-bottom:1px solid rgba(255,255,255,.14)}
  .section,.contact-section{padding:64px 24px}
  .about-grid,.plan-grid,.contact-section,.explore-grid{grid-template-columns:1fr;gap:44px}
  .explore-grid{gap:3px}
  .others-grid{grid-template-columns:1fr}
  footer{padding:30px 24px;flex-direction:column;text-align:center}
  .footer-links{justify-content:center}
}
@media (max-width:640px){
  .nav-logo{font-size:19px;white-space:nowrap}
  .hero-eyebrow{letter-spacing:.18em;line-height:1.6}
  .hero-tagline{font-size:17px}
  .body-copy{font-size:16px;line-height:1.75}
  .highlights{padding:28px 22px}
  .highlights li{font-size:15px}
  .g-grid{grid-template-columns:1fr 1fr;gap:10px}
  .g-item figcaption{font-size:12.5px}
  .plan-facts{grid-template-columns:1fr 1fr}
  .fact dd{font-size:20px}
  .contact-body{font-size:17px}
  .cc-val{font-size:15px}
  .eyebrow{font-size:11px}
  .lb-stage{padding:16px 44px}
  .lb-arrow{font-size:44px;padding:10px}
  .lb-top{padding:14px 18px}
  .lb-cap{font-size:15px}
  .x-card{padding:30px 26px}
}
"""

JS = r"""
(function(){
  var menu=document.getElementById('mobileMenu');
  document.querySelectorAll('[data-menu-open]').forEach(function(b){b.addEventListener('click',function(){menu.classList.add('open')})});
  document.querySelectorAll('[data-menu-close]').forEach(function(b){b.addEventListener('click',function(){menu.classList.remove('open')})});
  var items=[].slice.call(document.querySelectorAll('.g-btn'));
  var lb=document.getElementById('lb'),img=document.getElementById('lbImg'),cap=document.getElementById('lbCap'),cnt=document.getElementById('lbCount'),i=0;
  function show(n){i=(n+items.length)%items.length;var b=items[i];img.src=b.dataset.src;img.alt=b.dataset.alt;cap.textContent=b.dataset.cap;cnt.textContent=(i+1)+' / '+items.length}
  function open(n){show(n);lb.classList.add('open');document.body.style.overflow='hidden'}
  function close(){lb.classList.remove('open');document.body.style.overflow=''}
  items.forEach(function(b,n){b.addEventListener('click',function(){open(n)})});
  document.getElementById('lbClose').addEventListener('click',close);
  document.getElementById('lbPrev').addEventListener('click',function(){show(i-1)});
  document.getElementById('lbNext').addEventListener('click',function(){show(i+1)});
  lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('lb-stage'))close()});
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'){menu.classList.remove('open')}
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close();
    if(e.key==='ArrowLeft')show(i-1);
    if(e.key==='ArrowRight')show(i+1);
  });
  var sx=0;
  lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){var d=sx-e.changedTouches[0].clientX;if(Math.abs(d)>48){show(d>0?i+1:i-1)}},{passive:true});
})();
"""


def esc(s):
    return html.escape(s, quote=True)


def gallery_items(entries, start):
    out = []
    for n, (f, cap, alt) in enumerate(entries):
        src = f"{U}/{f}"
        out.append(
            f'<figure class="g-item"><button type="button" class="g-btn" data-src="{src}" data-cap="{esc(cap)}" data-alt="{esc(alt)}" aria-label="View larger: {esc(cap)}">'
            f'<img src="{src}" alt="{esc(alt)}" loading="lazy" decoding="async"></button>'
            f'<figcaption>{esc(cap)}</figcaption></figure>'
        )
    return "\n".join(out)


def build(key):
    p = PAGES[key]
    url = f"{SITE}/{p['slug']}/"
    mailto = f"mailto:{EMAIL}?subject={p['subject'].replace(' ', '%20').replace('&', '%26')}"
    og_img = SITE + p["hero"]

    cur = ' aria-current="page"'
    switch = "".join(
        '<a href="/%s/"%s>%s</a>' % (PAGES[k]["slug"], cur if k == key else "", LABEL[k]) for k in ORDER
    )
    stats = "".join(f'<div class="stat"><div class="stat-num">{esc(n)}</div><div class="stat-lbl">{esc(l)}</div></div>' for n, l in p["stats"])
    overview = "".join(f"<p>{esc(t)}</p>" for t in p["overview"])
    highlights = "".join(f"<li>{esc(t)}</li>" for t in p["highlights"])
    facts = "".join(f'<div class="fact"><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for a, b in p["plan_facts"])
    real = gallery_items(p["photos"], 0)
    rend = gallery_items(p["renders"], len(p["photos"]))
    others = ""
    for k in p["others"]:
        o = PAGES[k]
        others += (
            f'<a class="o-card" href="/{o["slug"]}/"><img src="{o["thumb"]}" alt="" loading="lazy" decoding="async">'
            f'<div class="o-body"><div class="o-label">{"Units 218 + 220" if k == "218-220" else "Unit " + k} &middot; East Cota Street</div>'
            f'<div class="o-sf">{SF_LINE[k]}</div><div class="o-blurb">{esc(o["blurb"])}</div><span class="o-link">View {"combined space" if k == "218-220" else "Unit " + k} &rarr;</span></div></a>'
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Plaza Commercial Center">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<!-- NAV -->
<nav>
    <a href="/" class="nav-logo">Plaza <span>Commercial</span> Center</a>
    <ul class="nav-links">
        <li><a href="/">Main Site</a></li>
        <li><a href="/#available">Available Units</a></li>
        <li><a href="/design-community.html">Design Community</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
    <button class="nav-hamburger" data-menu-open aria-label="Open menu"><span></span><span></span><span></span></button>
</nav>

<div class="mobile-menu" id="mobileMenu">
    <button class="mobile-menu-close" data-menu-close aria-label="Close menu">&times;</button>
    <a href="/">Main Site</a>
    <a href="/#available">Available Units</a>
    <a href="/design-community.html">Design Community</a>
    <a href="#contact" data-menu-close>Contact</a>
    <a href="{mailto}" class="mobile-menu-cta">Schedule a Tour</a>
</div>

<!-- HERO -->
<header class="hero" style="background-image:url('{p['hero']}');background-position:{p['hero_pos']};">
    <div class="hero-content">
        <p class="hero-eyebrow">Available for Lease &middot; Lagoon District, Santa Barbara</p>
        <h1 class="hero-title">{esc(p['h1_num'])} <em>East Cota</em></h1>
        <div class="hero-badge">{esc(p['avail_short'])}</div>
        <p class="hero-tagline">{esc(p['tagline'])}</p>
        <div class="hero-actions">
            <a href="{mailto}" class="btn-primary">Schedule a Tour</a>
            <a href="#photos" class="btn-ghost">See Photos</a>
            <a href="#floorplan" class="btn-ghost">Floor Plan</a>
        </div>
    </div>
</header>

<!-- UNIT SWITCHER -->
<div class="unit-switch"><div class="switch-inner"><span class="switch-label">Available Units</span>{switch}</div></div>

<!-- STATS -->
<div class="stats-bar">{stats}</div>

<!-- OVERVIEW -->
<section class="about section" id="overview">
    <div class="about-grid">
        <div>
            <p class="eyebrow">Unit Summary</p>
            <h2 class="section-title">{esc(p['sf'])} SF{" of contiguous space" if key == "218-220" else " on East Cota Street"}</h2>
            <div class="rule"></div>
            <div class="body-copy">{overview}</div>
        </div>
        <div class="highlights">
            <h3>Highlights</h3>
            <ul>{highlights}</ul>
        </div>
    </div>
</section>

<!-- PHOTOS -->
<section class="gallery section" id="photos">
    <p class="eyebrow">Photos</p>
    <h2 class="section-title">See the space</h2>
    <div class="rule"></div>
    <h3 class="sub">The Space</h3>
    <div class="g-grid">
{real}
    </div>
    <h3 class="sub">Concept Renderings</h3>
    <p class="note">Illustrative concepts of how the space could be built out &mdash; not photographs of completed tenant improvements.</p>
    <div class="g-grid">
{rend}
    </div>
</section>

<!-- FLOOR PLAN -->
<section class="floorplan section" id="floorplan">
    <div class="plan-grid">
        <div class="plan-card"><img src="{U}/{p['plan']}" alt="{esc(p['plan_alt'])}" loading="lazy" decoding="async"></div>
        <div>
            <p class="eyebrow">Floor Plan</p>
            <h2 class="section-title">{esc(p['plan_title'])}</h2>
            <div class="rule"></div>
            <div class="body-copy"><p>{esc(p['plan_text'])}</p></div>
            <dl class="plan-facts">{facts}</dl>
            <div class="plan-actions">
                <a class="btn-dark" href="{U}/{p['plan']}" download="{p['plan_download_name']}">&#8681;&nbsp; Download Floor Plan</a>
                <a class="btn-dark" href="/docs/Plaza-Commercial-Center-Brochure.pdf" target="_blank" rel="noopener">&#8681;&nbsp; Property Brochure</a>
            </div>
        </div>
    </div>
</section>

<!-- OTHER UNITS -->
<section class="others section" id="other-units">
    <p class="eyebrow">Also Available</p>
    <h2 class="section-title">More space at the Plaza</h2>
    <div class="rule"></div>
    <div class="others-grid">{others}</div>
</section>

<!-- EXPLORE -->
<section class="explore section">
    <p class="eyebrow">Explore</p>
    <h2 class="section-title">Plaza Commercial Center</h2>
    <div class="rule"></div>
    <div class="explore-grid">
        <a class="x-card" href="/"><h3>The Main Site</h3><p>The full property overview &mdash; all 15 units, the Lagoon District neighborhood and everything currently available.</p><span>Visit plazacommercialcenter.com &rarr;</span></a>
        <a class="x-card" href="/design-community.html"><h3>Design Community</h3><p>Meet the architects, showrooms and makers already at the Plaza, and see concept renderings for the available units.</p><span>See who's here &rarr;</span></a>
    </div>
</section>

<!-- CONTACT -->
<section class="contact-section" id="contact">
    <div>
        <p class="eyebrow">Get in Touch</p>
        <h2 class="section-title">Schedule a tour</h2>
        <div class="rule"></div>
        <p class="contact-body">Our management team can walk you through {"Units 218 and 220" if key == "218-220" else "Unit " + key}, discuss lease terms and answer questions. Tours are by appointment.</p>
    </div>
    <div class="contact-cards">
        <div class="contact-card"><div class="cc-lbl">Phone</div><a href="tel:{PHONE_TEL}" class="cc-val">{PHONE_DISPLAY}</a></div>
        <div class="contact-card"><div class="cc-lbl">Email</div><a href="mailto:{EMAIL}" class="cc-val">{EMAIL}</a></div>
        <div class="contact-card"><div class="cc-lbl">Address</div><span class="cc-val">East Cota Street<br>Between Garden Street and Santa Barbara Street</span></div>
        <a href="{mailto}" class="contact-cta">Request a Tour &rarr;</a>
    </div>
</section>

<footer>
    <div class="footer-name">Plaza Commercial Center</div>
    <div class="footer-links"><a href="/">Main Site</a><a href="/#available">Available Units</a><a href="/design-community.html">Design Community</a></div>
    <div class="footer-copy">&copy; 2026 Plaza Commercial Center &nbsp;&middot;&nbsp; Santa Barbara, CA</div>
</footer>

<!-- LIGHTBOX -->
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Photo viewer">
    <div class="lb-top"><span class="lb-cap" id="lbCap"></span><div class="lb-right"><span class="lb-count" id="lbCount"></span><button class="lb-close" id="lbClose" aria-label="Close">&times;</button></div></div>
    <div class="lb-stage"><button class="lb-arrow lb-prev" id="lbPrev" aria-label="Previous photo">&#8249;</button><img id="lbImg" src="" alt=""><button class="lb-arrow lb-next" id="lbNext" aria-label="Next photo">&#8250;</button></div>
</div>

<script>{JS}</script>
</body>
</html>
"""
    d = os.path.join(ROOT, p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    return d


if __name__ == "__main__":
    for k in ORDER:
        print(build(k))
