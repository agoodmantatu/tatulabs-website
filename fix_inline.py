src = open("E:/TatuLabs/index.html", encoding="utf-8").read()

# Nuclear fix — find .big-h .hl and add display:inline
old = ".big-h .hl{\n  background:linear-gradient(135deg,var(--accent),var(--accent2));\n  -webkit-background-clip:text;-webkit-text-fill-color:transparent;\n  transition:background 1.5s ease;\n}"
new = ".big-h .hl{\n  display:inline;\n  background:linear-gradient(135deg,var(--accent),var(--accent2));\n  -webkit-background-clip:text;-webkit-text-fill-color:transparent;\n  transition:background 1.5s ease;\n}"

if old in src:
    src = src.replace(old, new)
    print("Fixed .hl display:inline")
else:
    # Try without newlines
    idx = src.find(".big-h .hl{")
    if idx > 0:
        print("Found at:", idx)
        print("Context:", repr(src[idx:idx+200]))
    else:
        print("NOT FOUND - searching differently")
        # Add inline to all .hl uses
        src = src.replace(
            "background:linear-gradient(135deg,var(--accent),var(--accent2));  -webkit-background-clip:text;-webkit-text-fill-color:transparent;",
            "display:inline;background:linear-gradient(135deg,var(--accent),var(--accent2));  -webkit-background-clip:text;-webkit-text-fill-color:transparent;"
        )

open("E:/TatuLabs/index.html", "w", encoding="utf-8").write(src)
print("Done")
