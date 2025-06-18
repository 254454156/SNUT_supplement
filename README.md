# Supplement for “Fractal–Spiral Manifold” (Paper 1)

This repository contains the enumeration scripts and raw logs that support  
**Conjecture 1 (Triadic‑Uniqueness)** up to denominator 3³.

## Directory layout
* `code/centralizer_depth3.py` – Python/Sage script scanning all
  matrices `M = A / 3^d` with `|a_ij| ≤ 20`, `d ≤ 3`,  
  subject to `MR = RM`, `det M = ±1`, `||M|| > 1`.
* `code/centralizer_enum_depth2.g` – equivalent GAP script (depth 2).
* `data/depth3_run.log` – console output, shows  

