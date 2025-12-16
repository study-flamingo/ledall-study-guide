# Ledall Roll Study Guide - Project Roadmap

## Current Status: v0.6.0 Draft In Progress

The complete study guide (41 chapters, ~40,000 words) is compiled and ready for the next phase.

---

## Immediate Next Steps

### Phase 1: Proofreading & Polish
- [ ] Review for flow and consistency
- [ ] Verify citations and technical accuracy
- [ ] Final grammar and formatting pass
- [ ] Release as v1.0

---

## Future Enhancements

### Notion Digital Version

**Goal:** Interactive database version for modern practitioners.

**Structure:**
- **Master Database:** "All 41 Plays"
  - Properties: Play #, Name, Type (Flourish/Chase/Counter/Special), Difficulty, Key Concepts
  - Each entry links to full formatted chapter content
- **Terminology Database:** Cross-referenced glossary
- **Training Tracker:** Progress logging and scheduling
- **Bibliography Database:** All sources with links

**Timeline:** 2-3 days manual setup

---

### MCP Server for AI-Assisted Training

**Goal:** AI chat interface that knows the complete Ledall Roll system.

**Capabilities:**
- Answer questions about techniques ("How do I counter an aggressive opponent?")
- Suggest training progressions ("What should I practice after mastering Chase 4?")
- Explain terminology ("What's the difference between a rabett and a rake?")
- Find relevant plays ("Show me all techniques using springs")
- Generate custom drill sequences

**Implementation:**
- Create MCP server with study guide as knowledge base
- Semantic search across all 41 chapters
- Citation of specific sections in responses
- Training session planning

**Timeline:** 1-2 weeks development

---

### Obsidian Vault (Possible)

**Goal:** Graph-based view showing technique relationships.

**Features:**
- Each chapter as individual note
- Wikilinks between related techniques
- Graph view showing connections
- Tags for concepts (spring, rabett, proffer, etc.)
- Daily notes for practice logging

**Timeline:** 1-2 days conversion + organization

---

### Video Demonstration Library

**Goal:** Visual reference for all 41 plays - see the techniques in motion.

**Content Structure:**
- [ ] Full-speed demonstration of each play
- [ ] Slow-motion breakdown with commentary
- [ ] Common mistakes shown and corrected
- [ ] Partner drill variations
- [ ] Solo practice alternatives

**Organization:**
- Playlist per section (Flourishes, Chases, Counters, Special)
- Timestamp index for quick reference
- Downloadable for offline training
- Embed links in digital versions

**Timeline:** ~5 hours per play × 41 plays = 200+ hours (can film incrementally)

---

### Images & Diagrams

**Priority Additions:**
- [ ] Guard position diagrams (Roebuck, Hawk, Stop, Dragon's Tail, Pendant)
- [ ] Footwork diagrams for complex Chases (Tumbling Chase, Getting Chase)
- [ ] Attack angle illustrations for Counters
- [ ] Spring technique progression photos
- [ ] Historical manuscript images (where available/permitted)
- [ ] Blade trajectories overlaid on photos
- [ ] Distance markers for measure training

**Timeline:** Ongoing - 1-2 hours per diagram

---

### Study Tools & Practice Aids

**Drill Randomizer:**
- [ ] Generate random technique combinations for variety
- [ ] Filter by type, difficulty, or concept
- [ ] Create custom training sequences
- [ ] "Technique of the Day" feature

**Quick Reference Cards:**
- [ ] One-page summaries for each play (printable)
- [ ] Laminated cards for gym/salle use
- [ ] Step breakdown visible at a glance
- [ ] QR codes linking to videos/full chapter

**Interactive Decision Trees:**
- [ ] "Which Counter?" flowchart based on opponent behavior
- [ ] "What to practice next?" progression guide
- [ ] Troubleshooting guides ("My spring isn't working - why?")

**Assessment Tools:**
- [ ] Self-evaluation rubrics for each technique
- [ ] Progress tracking spreadsheets
- [ ] Partner assessment forms
- [ ] Milestone checklists (beginner → intermediate → advanced)

**Timeline:** Tools can be created incrementally as needed

---

## Implementation Priorities

### High Priority (Next 3 Months)
1. **Proofreading** - Quality first
2. **Notion version** - Modern, accessible format
3. **MCP server** - AI-assisted learning
4. **Basic diagrams** - Guard positions and footwork

### Medium Priority (3-6 Months)  
5. **Obsidian vault** - If useful for visualization
6. **Audio-guided sessions** - Hands-free training aid
7. **Video library** - Begin with Flourishes and key Chases
8. **Quick reference cards** - Training aids
9. **More illustrations** - Progressive enhancement

### Future Considerations
10. Mobile-optimized formats (ePub, PDF)
11. Community contribution system
12. Additional language versions (if demand exists)

---

## Big Stretch Goal: 3D/VR Training Animations 🚀

**The Dream:** Immersive VR environment for learning Medieval English longsword.

**What It Could Include:**
- 3D animated sequences viewable from any angle
- VR mode - step into a recreated Tudor training hall
- Virtual opponent that responds to your movements (VR controllers as sword)
- Slow-motion freeze-frame analysis of complex techniques
- Multiplayer VR training with remote partners worldwide
- Historical environment reconstruction

**Why It's Amazing:**
- First VR training app for historical swordsmanship
- Preserve techniques in interactive 3D format forever
- Practice anywhere without partner or equipment
- Incredible learning tool for complex footwork and spatial awareness
- See techniques from angles impossible in person (bird's eye, inside view)

**Why It Probably Won't Happen:**
- Massive time investment (500-1,000+ hours)
- Requires specialized skills (3D modeling, rigging, animation, VR development, motion capture)
- Equipment costs ($5,000+ for quality motion capture setup)
- Very small niche audience (English longsword practitioners with VR headsets)
- VR platforms evolve rapidly (maintenance burden)
- Ongoing costs for hosting multiplayer servers

**But If Someone Ever Wants To:**
- Start with simple stick-figure 3D animations (proof of concept)
- Partner with game dev students (could be amazing thesis project)
- Use existing 3D sword models from asset stores
- Record motion capture footage at HEMA events
- Open source all models/animations for community use
- Begin with just the 3 Flourishes to test feasibility

*It's fun to dream big! Even if we never build it, imagining the possibilities keeps the tradition alive and evolving.* ⚔️✨

---

---

## Additional Ideas Worth Exploring

### Sparring Scenario Cards
**Concept:** Deck of cards for training variety.
- Each card presents a scenario ("Opponent rushes you aggressively")
- List applicable techniques from the guide
- Practice finding and executing the right response
- Solo or partner use
- Physical deck or app-based

### Technique Cross-Reference Matrix
**Concept:** Visual map of how techniques connect.
- Which Chases lead into which Counters
- Shared movements across different plays
- Progression pathways highlighted
- Prerequisites clearly shown

### Historical Context Deep Dives
**Concept:** Supplementary essays on cultural/historical topics.
- Tudor England martial culture
- John Ledall of York - biographical research
- Weapons and armor of the period
- Legal framework for fighting
- Connection to other English manuscripts

### "Build Your Own Curriculum" Tool
**Concept:** Interactive planner for instructors.
- Select techniques by difficulty/theme
- Auto-generate lesson plans
- Suggest warm-ups, drills, and cool-downs
- Export to calendar or PDF

---

## Resource Needs

**Notion Version:**
- Skills: Notion databases, basic automation
- Time: 2-3 days
- Cost: Free

**MCP Server:**
- Skills: Python/TypeScript, MCP protocol, vector embeddings
- Time: 1-2 weeks
- Cost: Free (local) or minimal (hosting ~$5-10/month)

**Obsidian:**
- Skills: Markdown organization, plugin configuration
- Time: 1-2 days
- Cost: Free

**Diagrams/Images:**
- Skills: Illustration, photography, or photo editing
- Time: Varies (1-2 hours per diagram)
- Cost: Free (DIY) or commissioned work

---

---

## More Ideas Worth Exploring

### Comparative Technique Database
Cross-system reference mapping English → German → Italian techniques. A "Rosetta Stone" for HEMA practitioners.

### Sparring Scenario Cards  
Deck of cards presenting combat situations with applicable techniques listed. Great for training variety.

### Training Journal Template
Structured journal (Notion/Obsidian/PDF) for tracking personal progress, partner feedback, and breakthrough moments.

### Living Manuscript Project
Collaborative workspace where community shares multiple interpretations, test results, and votes on most effective reconstructions.

### Technique Cross-Reference Matrix
Visual map showing how techniques connect, which Chases lead to which Counters, shared movements, progression pathways.

### "Build Your Own Curriculum" Tool
Interactive planner for instructors to select techniques, auto-generate lesson plans, and export to calendar.

---

## Open Questions

1. Which should we prioritize: Notion or MCP server?
2. Obsidian: Worth the conversion effort for graph view?
3. Images: Create ourselves, commission, or accept community contributions?
4. MCP server: Local only or cloud-hosted for sharing?
5. Audio: Professional voice actor or authentic practitioner narration?

---

## How This Roadmap Evolves

This is a **living document** - we'll adjust priorities based on:
- What proves most useful in practice
- Community feedback and requests
- Available time and resources
- New opportunities or collaborations

**Last Updated:** December 13, 2025  
**Version:** 0.6.0 - Focused Roadmap
