* `data/machine_specs.txt` – CPU model, RAM, Ubuntu 22.04, GAP 4.11 / Sage 9.5.
* `requirements.txt` – only `sageconf >= 9.5` if using pure Python,
or leave empty for GAP.

## Reproduce
```bash
# Sage version
sage code/centralizer_depth3.py
# GAP version
gap -q < code/centralizer_enum_depth2.g
