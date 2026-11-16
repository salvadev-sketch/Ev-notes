# EV & Hybrid Master Technician Handbook

A 10-module illustrated training resource for developing EV and hybrid technicians.
Each module is an A4 PDF handbook plus a matching editable 16:9 PowerPoint, with the same
figures, figure numbers, terminology and fault scenarios in both.

All monitors, waveforms and measurements are **SIMULATED TRAINING DATA**. Fault codes use the
**TRN-** prefix so they cannot be mistaken for real DTCs. Nothing here is OEM service information.

| Module | Title | PDF | PowerPoint |
|---|---|---|---|
| 1 | HV Battery and Cell Chemistry | built (rebuilt, 29 pp, awaiting review) | approved earlier against a previous PDF; needs re-check |
| 2 | Power Electronics | built (26 pp, awaiting review) | not built |
| 3 | Electric Motors and Traction | outline approved; build interrupted | not started |
| 4 | Hybrid Drivetrains | not started | not started |
| 5 | Thermal Management | not started | not started |
| 6 | Networks and Control Units | not started | not started |
| 7 | Software and Adaptations | not started | not started |
| 8 | Electrical Fundamentals and Advanced Diagnostics | not started | not started |
| 9 | EV Charging | not started | not started |
| 10 | HV Safety and Workshop Practice | not started | not started |

## Layout
- `docs/PROJECT_SPEC.md`: role, content rules, visual format, working style
- `docs/STATUS.md`: current state and what was lost in the environment reset
- `docs/outlines/`: approved outlines
- `src/common/`: shared figure helpers and PDF framework (ReportLab, matplotlib, Liberation Sans)
- `src/module03/data3.py`: verified Module 3 numbers
- `modules/`: finished PDFs

## Build notes
`pip install reportlab matplotlib pillow pypdf`. Set `EV_MODULE` and `EV_DATA` (data module name) before importing `bk`.
