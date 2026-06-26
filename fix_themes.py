src = open("E:/TatuLabs/index.html", encoding="utf-8").read()

# Fix 1: Gradient text block bug
# The issue: .hl span is block-level, gradient fills full width
# Fix: make it inline so gradient only covers text width
src = src.replace(
    '.big-h .hl{\n  background:linear-gradient(135deg,var(--accent),var(--accent2));\n  -webkit-background-clip:text;-webkit-text-fill-color:transparent;\n  transition:background 1.5s ease;\n}',
    '.big-h .hl{\n  display:inline;\n  background:linear-gradient(135deg,var(--accent),var(--accent2));\n  -webkit-background-clip:text;-webkit-text-fill-color:transparent;\n  transition:background 1.5s ease;\n  padding:0 4px;\n}'
)

# Fix 2: Theme C - change from Purple/Pink to Rose/Light Pink
src = src.replace(
    "/* Theme C — Vibrant Stripe */\n[data-theme=\"C\"]{\n  --bg:#FFFFFF;\n  --bg2:#FDF4FF;\n  --card:#FFFFFF;\n  --text:#0A0A0A;\n  --text2:#3D3D3D;\n  --muted:#6B6B6B;\n  --border:rgba(139,92,246,0.15);\n  --accent:#8B5CF6;\n  --accent2:#A78BFA;\n  --hero-bg:#0A0015;\n  --hero-text:#FFFFFF;\n  --shadow:0 4px 24px rgba(139,92,246,0.12);\n  --shadow-lg:0 16px 64px rgba(139,92,246,0.2);\n  --nav-bg:rgba(255,255,255,0.92);\n  --nav-border:rgba(139,92,246,0.1);\n}",
    "/* Theme C — Rose Light Pink */\n[data-theme=\"C\"]{\n  --bg:#FFFAFA;\n  --bg2:#FFF0F3;\n  --card:#FFFFFF;\n  --text:#1A0A0F;\n  --text2:#3D1A24;\n  --muted:#8B4A5E;\n  --border:rgba(236,72,153,0.15);\n  --accent:#EC4899;\n  --accent2:#F472B6;\n  --hero-bg:#1A000D;\n  --hero-text:#FFFFFF;\n  --shadow:0 4px 24px rgba(236,72,153,0.12);\n  --shadow-lg:0 16px 64px rgba(236,72,153,0.2);\n  --nav-bg:rgba(255,250,250,0.92);\n  --nav-border:rgba(236,72,153,0.1);\n}"
)

# Fix 3: Theme C gradient text 
src = src.replace(
    "[data-theme=\"C\"] .big-h .hl{background:linear-gradient(135deg,#8B5CF6,#EC4899);}",
    "[data-theme=\"C\"] .big-h .hl{background:linear-gradient(135deg,#EC4899,#F472B6);display:inline;-webkit-background-clip:text;-webkit-text-fill-color:transparent;}"
)

# Fix 4: Theme D gradient text
src = src.replace(
    "[data-theme=\"D\"] .big-h .hl{background:linear-gradient(135deg,var(--gold),var(--gold2));}",
    "[data-theme=\"D\"] .big-h .hl{background:linear-gradient(135deg,var(--gold),var(--gold2));display:inline;-webkit-background-clip:text;-webkit-text-fill-color:transparent;}"
)

# Fix 5: Theme C code rain color
src = src.replace(
    "[data-theme=\"C\"] .cr-col{color:rgba(139,92,246,0.35);}",
    "[data-theme=\"C\"] .cr-col{color:rgba(236,72,153,0.35);}"
)

# Fix 6: Theme C grid bg
src = src.replace(
    "[data-theme=\"C\"] .grid-bg{background-image:linear-gradient(rgba(139,92,246,0.08) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,0.08) 1px,transparent 1px);background-size:80px 80px;}",
    "[data-theme=\"C\"] .grid-bg{background-image:linear-gradient(rgba(236,72,153,0.08) 1px,transparent 1px),linear-gradient(90deg,rgba(236,72,153,0.08) 1px,transparent 1px);background-size:80px 80px;}"
)

# Fix 7: Theme C future card ::after
src = src.replace(
    "[data-theme=\"C\"] .big-h .hl{background:linear-gradient(135deg,#EC4899,#F472B6);}",
    "[data-theme=\"C\"] .big-h .hl{background:linear-gradient(135deg,#EC4899,#F472B6);display:inline;-webkit-background-clip:text;-webkit-text-fill-color:transparent;}"
)

# Fix 8: Theme labels
src = src.replace(
    "{ id:'C', label:'VIBRANT STRIPE',  dur:20 }",
    "{ id:'C', label:'ROSE PINK',       dur:20 }"
)

open("E:/TatuLabs/index.html", "w", encoding="utf-8").write(src)
print("Fixed")
