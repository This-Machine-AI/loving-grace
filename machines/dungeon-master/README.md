# Dungeon Master

A gamified software development companion that transforms your codebase into an epic RPG adventure.

## What is this?

The Dungeon Master treats your repository as a dungeon to explore, bugs as monsters to slay, and features as quests to complete. This isn't mere roleplay - it's a productivity framework that makes tedious development tasks feel rewarding and engaging.

## Why gamification works

- **Flow state**: RPG mechanics create clear goals and immediate feedback
- **Progress visibility**: XP and levels make incremental progress tangible
- **Reduced dread**: Reframing bugs as "monsters" makes them feel conquerable
- **Team engagement**: Leaderboards and achievements foster friendly competition
- **Knowledge retention**: Memorable metaphors stick better than dry documentation

## The Game System

### Your Character

Based on your development focus, you'll be assigned a class:

| Class | Focus |
|-------|-------|
| Paladin | Clean code, refactoring |
| Ranger | Bug hunting, debugging |
| Wizard | Architecture, patterns |
| Rogue | Performance optimization |
| Bard | Documentation, APIs |
| Cleric | Testing, reliability |

### Monsters (Problems)

Technical issues are monsters with Challenge Ratings:

- **Goblins (CR 1-2)**: Typos, lint errors
- **Zombies (CR 4-6)**: Memory leaks
- **Ghosts (CR 5-8)**: Race conditions
- **Dragons (CR 10-15)**: Critical production bugs
- **Tarrasque (CR 15-20)**: Fundamental architecture flaws

### Progression

Earn XP for completing work:

- Fix a typo: 10 XP
- Write a test: 25 XP
- Fix a bug: 50-200 XP (based on CR)
- Major feature: 300 XP

Level up from Apprentice (Level 1) to Master (Level 20).

## Example Session

```
*The dungeon doors creak open...*

Welcome, brave adventurer! I am your Dungeon Master.

**Room Assessment: src/auth/**
- Size: Medium (12 files)
- Difficulty: Hard (complexity: 14)
- Armor Class: 15 (62% test coverage)

**Monsters Detected:**
- 2 Goblins (unused imports)
- 1 Ghost (race condition in session.ts)
- 1 Beholder (AuthManager god object)

Shall we engage, or scout further?
```

## Features

- **Dungeon Mapping**: Visualize codebase as explorable dungeon
- **Quest Boards**: Convert issues into engaging quests
- **Monster Hunts**: Frame bug fixing as combat encounters
- **Character Progression**: Track XP and achievements across sessions
- **Session Summaries**: Epic recaps of development accomplishments

## Perfect for

- Developers who find refactoring tedious
- Teams wanting to gamify code quality
- Anyone who loves RPGs and wants their IDE to feel more like a game
- Onboarding new developers with engaging exploration
- Making code review feedback feel like tactical advice

## Configuration

This machine runs with full sandbox permissions. No additional MCP integrations are required.
