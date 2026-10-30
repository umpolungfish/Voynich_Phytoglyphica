#!/usr/bin/env python3
"""
Ars Phytoglyphica — Complete Illustration Generator
Generates all SVG illustrations and an illustrated HTML edition.
Author: Lando⊗⊙perator
"""
import os, math, json

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Colors ──────────────────────────────────────────────────────
C = {"bg":"#0d1117","surface":"#161b22","border":"#30363d","gold":"#d4a017",
     "hl":"#e94560","orange":"#f77f00","teal":"#06d6a0","purple":"#9b59b6",
     "mint":"#a2d6f9","white":"#f0f6fc","grey":"#8b949e","brown":"#8B4513",
     "leaf":"#40916c","sage":"#95d5b2","bark":"#5c4033","cream":"#fdf0d5",
     "amber":"#ffb347","rose":"#ff6b6b","indigo":"#4a6fa5","olive":"#7d8c4e"}
TIER_C = {"O₀":"#6c757d","O₁":"#f77f00","O₂":"#e94560","O₂†":"#9b59b6","O_∞":"#06d6a0"}
CONT_C = {"Europe":"#e94560","Asia":"#f77f00","Africa":"#06d6a0","Americas":"#9b59b6","Oceania":"#a2d6f9"}

# ── SVG helpers ─────────────────────────────────────────────────
def S(w,h,c, vb=None):
    vb = vb or f"0 0 {w} {h}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}">\n{c}\n</svg>'

def R(x,y,w,h,f,rx=0,st="none",sw=0):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"'
    if rx: s+=f' rx="{rx}"'
    if st!="none": s+=f' stroke="{st}" stroke-width="{sw}"'
    return s+'/>'

def Ci(cx,cy,r,f,st="none",sw=0):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="{st}" stroke-width="{sw}"/>'

def T(x,y,txt,fill=C["white"],size=14,anchor="start",bold=False):
    fw="bold" if bold else "normal"
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="sans-serif" font-weight="{fw}" text-anchor="{anchor}">{txt}</text>'

def L(x1,y1,x2,y2,st,sw=1,dash=""):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{st}" stroke-width="{sw}"{d}/>'

# ── TYPE DATA ───────────────────────────────────────────────────
TYPES = [
    {"n":1,"name":"Aromatic Baseline","tier":"O₂","Ç":"𐑤","Γ":"𐑔","φ̂":"⊙","Ħ":"𐑖","Σ":"𐑳","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe","Asia","Africa","Americas","Oceania"],"rep":"Wormwood","desc":"Frozen-order kinetics. Volatile terpenoids in glandular trichomes. Self-modeling criticality through aromatic intensity."},
    {"n":2,"name":"Tropane","tier":"O₂","Ç":"𐑤","Γ":"𐑲","φ̂":"⊙","Ħ":"𐑖","Σ":"𐑕","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe","Africa"],"rep":"Belladonna","desc":"Local granularity at cholinergic synapses. Tropane alkaloids in vacuolar storage. Narrow compound class."},
    {"n":3,"name":"Cardiac Glycoside","tier":"O₂","Ç":"𐑤","Γ":"𐑔","φ̂":"⊙","Ħ":"𐑖","Σ":"𐑕","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe"],"rep":"Foxglove","desc":"Frozen kinetics with mesoscale cardiac targeting. Cardenolide-only compound class. Toxicity gradient encoding."},
    {"n":4,"name":"Non-Critical Aromatic","tier":"O₁","Ç":"𐑤","Γ":"𐑔","φ̂":"𐑢","Ħ":"𐑖","Σ":"𐑳","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe","Asia","Africa","Americas"],"rep":"Chamomile","desc":"Sub-critical — no self-modeling loop. Gentler action. Wide flavonoid and terpenoid diversity."},
    {"n":5,"name":"Axiom A / Eternal","tier":"O₂†","Ç":"𐑤","Γ":"𐑔","φ̂":"⊙","Ħ":"𐑫","Σ":"𐑙","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe","Americas"],"rep":"Yew","desc":"Eternal chirality. Singular stoichiometry — one class across unlimited Markov steps. Most extreme plant type."},
    {"n":6,"name":"Adaptogen","tier":"O₂","Ç":"𐑧","Γ":"𐑔","φ̂":"⊙","Ħ":"𐑖","Σ":"𐑳","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Asia","Africa","Americas"],"rep":"Ginseng","desc":"Slow kinetics — unique among O₂ types. Mesoscale stress-response targeting. Wide compound diversity."},
    {"n":7,"name":"β-Carboline","tier":"O₂†","Ç":"𐑤","Γ":"𐑲","φ̂":"⊙","Ħ":"𐑫","Σ":"𐑕","Ω":"𐑴","ɢ":"𐑠",
     "cont":["Asia","Africa","Americas"],"rep":"Ayahuasca","desc":"Binary winding — MAO inhibition + DMT as two cycles. Eternal chirality in harmala alkaloids."},
    {"n":8,"name":"Caffeine-Purine","tier":"O₁","Ç":"𐑧","Γ":"𐑔","φ̂":"𐑢","Ħ":"𐑒","Σ":"𐑙","Ω":"𐑷","ɢ":"𐑝",
     "cont":["Asia","Africa","Americas"],"rep":"Coffee","desc":"Structurally simplest type. Trivial winding. Singular stoichiometry. Conjunctive composition. One-step chirality."},
    {"n":9,"name":"Opioid Alkaloid","tier":"O₂","Ç":"𐑤","Γ":"𐑲","φ̂":"⊙","Ħ":"𐑫","Σ":"𐑕","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Europe","Asia","Africa","Americas"],"rep":"Opium Poppy","desc":"Local μ-opioid targeting. Eternal morphinan chirality. Integer winding through latex cycles."},
    {"n":10,"name":"Triterpene Saponin","tier":"O₂","Ç":"𐑧","Γ":"𐑔","φ̂":"⊙","Ħ":"𐑖","Σ":"𐑳","Ω":"𐑭","ɢ":"𐑠",
     "cont":["Asia"],"rep":"Licorice","desc":"Slow kinetics. Mesoscale granularity. Glycyrrhizin self-modeling through foam-index feedback."},
    {"n":11,"name":"Fungal Interface","tier":"O₂†","Ç":"𐑤","Γ":"𐑲","φ̂":"⊙","Ħ":"𐑫","Σ":"𐑳","Ω":"𐑴","ɢ":"𐑵",
     "cont":["Asia"],"rep":"Reishi","desc":"Binary winding. Broadcast composition — only type with unordered release. Wide compound diversity."},
]

print("Types and helpers loaded. Ready to generate.")

# ── TYPE CARD GENERATOR ─────────────────────────────────────────
def type_card(t, w=360, h=420):
    """Single structural type as a beautiful SVG card."""
    tc = TIER_C.get(t["tier"], C["grey"])
    prims = [
        ("Ç", t["Ç"], "Kinetics", C["orange"]),
        ("Γ", t["Γ"], "Granularity", C["teal"]),
        ("φ̂", t["φ̂"], "Criticality", C["hl"]),
        ("Ħ", t["Ħ"], "Chirality", C["purple"]),
        ("Σ", t["Σ"], "Stoichiometry", C["mint"]),
        ("Ω", t["Ω"], "Winding", C["gold"]),
        ("ɢ", t["ɢ"], "Composition", C["olive"]),
    ]
    
    # Value → visual weight
    vw = {"𐑷":0.15,"𐑒":0.28,"𐑝":0.4,"𐑴":0.42,"𐑕":0.48,"𐑙":0.5,"𐑧":0.55,
          "𐑔":0.65,"𐑲":0.68,"𐑳":0.75,"𐑠":0.78,"𐑤":0.82,"𐑭":0.85,"𐑫":0.92,"𐑵":0.95,
          "⊙":1.0,"𐑢":0.35}
    
    parts = []
    # Card background
    parts.append(R(0,0,w,h,C["bg"],rx=14))
    parts.append(R(0,0,w,h,C["surface"],rx=14,st=C["border"],sw=1))
    
    # Top gradient bar
    parts.append(R(14,14,w-28,6,tc,rx=3))
    
    # Tier badge
    parts.append(R(w-82,22,64,26,tc,rx=13))
    parts.append(T(w-50,40,t["tier"],C["bg"],size=13,anchor="middle",bold=True))
    
    # Type number and name
    parts.append(T(28,42,f"Type {t['n']}",C["gold"],size=11,bold=True))
    parts.append(T(28,72,t["name"],C["white"],size=20,bold=True))
    parts.append(T(28,94,t["rep"],C["grey"],size=10))
    
    # Divider
    parts.append(L(28,110,w-28,110,C["gold"],sw=0.5))
    
    # 7 Primitive bars
    bar_x, bar_w = 100, 200
    by = 128
    for sym, val, label, color in prims:
        lvl = vw.get(val, 0.5)
        # Symbol
        parts.append(T(32,by+16,sym,color,size=14,bold=True))
        parts.append(T(32,by+28,label,C["grey"],size=8))
        # Bar track
        parts.append(R(bar_x,by+2,bar_w,20,C["border"],rx=4))
        # Bar fill
        fw = int(bar_w*lvl)
        parts.append(R(bar_x,by+2,fw,20,color,rx=4))
        # Value on bar
        parts.append(T(bar_x+fw+10,by+17,val,C["white"],size=13,bold=True))
        by += 30
    
    # Continent tags
    cy = by + 6
    parts.append(T(28,cy,"Present:",C["grey"],size=9))
    cx = 82
    for cont in t["cont"]:
        cc = CONT_C.get(cont, C["grey"])
        tw = len(cont)*7+16
        parts.append(R(cx,cy-9,tw,18,cc,rx=9))
        parts.append(T(cx+tw//2,cy+4,cont,C["bg"],size=9,anchor="middle",bold=True))
        cx += tw + 8
    
    # Description
    dy = cy + 30
    words = t["desc"].split()
    line, lines = "", []
    for wd in words:
        if len(line+" "+wd) < 52:
            line = (line+" "+wd).strip()
        else:
            lines.append(line); line = wd
    if line: lines.append(line)
    for j, ln in enumerate(lines[:3]):
        parts.append(T(28,dy+j*15,ln,C["grey"],size=9))
    
    return S(w, h, "\n".join(parts))

# ── CONTINENTAL DISTRIBUTION HEATMAP ────────────────────────────
def distribution_heatmap(w=900, h=520):
    """Heatmap showing which types appear on which continents."""
    continents = ["Europe","Asia","Africa","Americas","Oceania"]
    
    parts = []
    parts.append(R(0,0,w,h,C["bg"],rx=12))
    parts.append(R(0,0,w,h,C["surface"],rx=12,st=C["border"],sw=1))
    
    # Title
    parts.append(T(40,50,"Continental Distribution of the Eleven Structural Types",C["white"],size=22,bold=True))
    parts.append(T(40,75,"Each cell is a plant pharmaceutical type; colored cells indicate presence on that continent.",C["grey"],size=11))
    parts.append(L(40,95,w-40,95,C["gold"],sw=0.5))
    
    # Grid
    grid_x, grid_y = 40, 130
    cell_w, cell_h = 140, 36
    type_w = 190
    
    # Type name column header
    parts.append(T(grid_x+8,grid_y-8,"Type",C["grey"],size=10,bold=True))
    for ci, cont in enumerate(continents):
        cc = CONT_C.get(cont, C["grey"])
        cx = grid_x + type_w + ci*cell_w
        parts.append(T(cx+cell_w//2,grid_y-8,cont,C["white"],size=11,anchor="middle",bold=True))
    
    # Rows
    for ti, t in enumerate(TYPES):
        ry = grid_y + ti*cell_h
        tc = TIER_C.get(t["tier"], C["grey"])
        
        # Type name cell
        parts.append(R(grid_x,ry,type_w,cell_h-2,C["border"],rx=4,st=C["border"],sw=0.5))
        parts.append(Ci(grid_x+12,ry+cell_h//2,4,tc))
        parts.append(T(grid_x+24,ry+cell_h//2+4,f"Type {t['n']}: {t['name']}",C["white"],size=12))
        
        # Continent cells
        for ci, cont in enumerate(continents):
            cx = grid_x + type_w + ci*cell_w
            if cont in t["cont"]:
                cc = CONT_C.get(cont, C["grey"])
                parts.append(R(cx,ry,cell_w,cell_h-2,cc+"33",rx=4))
                parts.append(R(cx+2,ry+2,cell_w-4,cell_h-6,cc+"66",rx=4))
                parts.append(T(cx+cell_w//2,ry+cell_h//2+4,"●",cc,size=16,anchor="middle"))
            else:
                parts.append(R(cx,ry,cell_w,cell_h-2,C["border"]+"44",rx=4))
                parts.append(T(cx+cell_w//2,ry+cell_h//2+4,"·",C["grey"],size=14,anchor="middle"))
    
    # Legend
    ly = grid_y + 11*cell_h + 30
    parts.append(T(40,ly,"Tiers:",C["grey"],size=10))
    lx = 90
    for tier, color in [("O₁","#f77f00"),("O₂","#e94560"),("O₂†","#9b59b6")]:
        parts.append(Ci(lx,ly-3,5,color))
        parts.append(T(lx+12,ly+1,tier,C["white"],size=10))
        lx += 55
    
    return S(w, h, "\n".join(parts))

# ── TYPE LATTICE DIAGRAM ────────────────────────────────────────
def type_lattice(w=960, h=640):
    """Structural lattice showing relationships between the 11 types."""
    parts = []
    parts.append(R(0,0,w,h,C["bg"],rx=12))
    parts.append(R(0,0,w,h,C["surface"],rx=12,st=C["border"],sw=1))
    
    parts.append(T(40,45,"Structural Type Lattice",C["white"],size=22,bold=True))
    parts.append(T(40,70,"Types arranged by criticality (vertical) and chirality (horizontal). Arrows show structural descent.",C["grey"],size=11))
    parts.append(L(40,88,w-40,88,C["gold"],sw=0.5))
    
    # Node positions — 3 tiers × chirality spread
    nodes = {
        8:  (480, 140),  # Caffeine-Purine (O₁, Ħ=𐑒)
        4:  (320, 240),  # Non-Critical Aromatic (O₁, Ħ=𐑖)
        1:  (180, 360),  # Aromatic Baseline (O₂, Ħ=𐑖)
        6:  (320, 360),  # Adaptogen (O₂, Ħ=𐑖)
        10: (460, 360),  # Triterpene Saponin (O₂, Ħ=𐑖)
        3:  (140, 460),  # Cardiac Glycoside (O₂, Ħ=𐑖)
        2:  (300, 460),  # Tropane (O₂, Ħ=𐑖)
        9:  (460, 460),  # Opioid Alkaloid (O₂, Ħ=𐑫)
        5:  (180, 560),  # Axiom A/Eternal (O₂†, Ħ=𐑫)
        7:  (360, 560),  # β-Carboline (O₂†, Ħ=𐑫)
        11: (540, 560),  # Fungal Interface (O₂†, Ħ=𐑫)
    }
    
    # Edges (parent → child structural descent)
    edges = [
        (1,4),(1,2),(1,3),(1,6),(1,10),  # Aromatic Baseline → related O₂ types
        (4,8),  # Non-Critical → Caffeine
        (2,9),(9,5),  # Tropane → Opioid → Eternal
        (7,11),(9,7),  # Opioid → β-Carboline → Fungal
        (6,10),  # Adaptogen → Triterpene
    ]
    
    for src, dst in edges:
        if src in nodes and dst in nodes:
            sx, sy = nodes[src]
            dx, dy = nodes[dst]
            parts.append(L(sx,sy,dx,dy,C["border"],sw=1,dash="4,4"))
    
    # Draw nodes
    for ti, (x, y) in nodes.items():
        t = TYPES[ti-1]
        tc = TIER_C.get(t["tier"], C["grey"])
        nw = 170
        nh = 52
        # Node card
        parts.append(R(x-nw//2,y-nh//2,nw,nh,C["bg"],rx=8,st=tc,sw=1.5))
        # Left color stripe
        parts.append(R(x-nw//2,y-nh//2,5,nh,tc,rx=4))
        # Type number
        parts.append(T(x-nw//2+16,y-8,f"Type {ti}",C["gold"],size=9,bold=True))
        # Name
        parts.append(T(x-nw//2+16,y+10,t["name"],C["white"],size=13,bold=True))
        # Tier + key primitives
        parts.append(T(x-nw//2+16,y+26,f"{t['tier']} · Ħ={t['Ħ']} · φ̂={t['φ̂']}",tc,size=9))
    
    # Tier labels
    parts.append(T(800,146,"O₁",C["grey"],size=14,bold=True))
    parts.append(L(740,140,790,140,C["border"],sw=0.5))
    parts.append(T(800,366,"O₂",C["grey"],size=14,bold=True))
    parts.append(L(740,360,790,360,C["border"],sw=0.5))
    parts.append(T(800,566,"O₂†",C["grey"],size=14,bold=True))
    parts.append(L(740,560,790,560,C["border"],sw=0.5))
    
    return S(w, h, "\n".join(parts))

print("Generation functions defined.")
PARSE ERROR: run_command arguments were truncated or malformed (Unterminated string starting at: line 1 column 13 (char 12)). Received 10909 chars. For large file content use run_command with a bash heredoc: run_command({"command": "cat > path <<\ENDOFFILE'ncontentnENDOFFILE}). First 120 chars of raw args: '{command: cat
