# Changelog

All notable changes to the Ledall Roll Study Guide project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.6.0] - 2025-12-16

### Added

- **Complete manuscript** - `Ledall_Longsword_manuscript.md` (8,000+ lines) containing all 41 plays with full scholarly apparatus
- **Completion summary** - `docs/v0-6-0_completion_summary.md` documenting final compilation statistics
- **VSCode workspace settings** - `.vscode/settings.json` for consistent editor experience

### Changed

- **Project reorganization** - Cleaner directory structure separating working drafts from final output
  - Moved session work files from `sections/` to `drafts/sections/`
  - Moved `sources.md` to `docs/sources.md`
  - Renamed final manuscript to `Ledall_Longsword_manuscript.md`
- **README.md** - Major update reflecting completed v0.6.0 status with comprehensive usage guide
- **docs/ROADMAP.md** - Streamlined and refocused for post-compilation phase

### Removed

- `COMPILATION_COMPLETE.md` - Superseded by `docs/v0-6-0_completion_summary.md`
- `VOID_TERMINOLOGY_CORRECTION_PLAN.md` - Terminology corrections completed and merged
- Root-level `sections/` folder - Content moved to `drafts/sections/`
- Root-level `sources.md` - Moved to `docs/sources.md`

---

## [0.5.0] - 2025-12-13

### Added

- **Void terminology clarification** - Corrected "void" usage throughout the guide per historical sources
- Merged pull request #1 from `cursor/void-term-clarification-edit-89cd`

### Changed

- Refactored terminology usage to align with period-accurate meanings
- Updated execution order references for consistency

---

## [0.4.0] - 2025-12-12

### Changed

- Chapter semantics editing pass
- Typo corrections throughout

---

## [0.3.0] - 2025-12-11

### Added

- `LICENSE.md` - CC BY-SA 4.0 licensing
- `README.md` - Project introduction and usage guide
- `docs/ROADMAP.md` - Future development plans

---

## [0.2.0] - 2025-12-10

### Added

- Session work files:
  - `ledall_roll_session1_chases.md` - Chases 5-7, 9-12
  - `ledall_roll_session2_counters_1-9.md` - Counters 1-9
  - `ledall_roll_session3_counters_11-21.md` - Counters 11-21
  - `ledall_roll_session4_final.md` - Counter 23 and Conclusion
  - `ledall_roll_session4_special_techniques.md` - Stopping Rabett, Dragon's Tail
- `sources.md` - Complete bibliography with 10 academic sources

### Changed

- `ledall_guide_draft_02.md` - Enhanced with research citations and practitioner tips

---

## [0.1.0] - 2025-12-09

### Added

- Initial project structure
- `ledall_guide_draft_01.md` - First complete draft with all 41 plays
- `manuscript/ledall_modernization.csv` - Source transcript and modernization
- `overview.md` - Project summary

---

## Document Statistics (v0.6.0)

| Metric | Value |
|--------|-------|
| Total Lines | ~8,000 |
| Total Words | ~40,000 |
| Total Chapters | 41 |
| Flourishes | 3 |
| Chases | 13 |
| Counters | 23 |
| Special Techniques | 2 |
| Academic Citations | 10 |

---

## Project Structure (Current)

```
ledall-study-guide/
├── Ledall_Longsword_manuscript.md  ← MAIN OUTPUT (start here)
├── README.md
├── CHANGELOG.md
├── overview.md
├── docs/
│   ├── LICENSE.md
│   ├── ROADMAP.md
│   ├── sources.md
│   ├── FINAL_DRAFT_SUMMARY.md
│   └── v0-6-0_completion_summary.md
├── drafts/
│   ├── ledall_guide_draft_01.md
│   ├── ledall_guide_draft_02.md
│   └── sections/
│       └── [session work files]
├── manuscript/
│   └── ledall_modernization.csv
└── src/
    └── img/
        └── battle_of_pavia.jpg
```

---

*For detailed future plans, see [docs/ROADMAP.md](docs/ROADMAP.md).*
