# Fruit Catcher Repair Lab

This project is a 2D arcade catch-and-dodge game using **Pygame**. It introduces students to sprite collision checking, continuous horizontal movement, falling entity lifecycle management, life counters, and game state transitions within an object-oriented codebase.
---

## What's Provided

A working Fruit Catcher game with:

- A controllable basket at the bottom with clamped screen-edge boundaries
- Falling fruits (Apples, Oranges, Grapes) that spawn at randomized x-coordinates with independent falling speeds
- Keyboard controls supporting both `A` / `D` and `Left` / `Right` arrow keys
- Live score and lives HUD display
- A Game Over screen overlay with restart functionality

It has **one deliberate bug** and **three optional features** left as tasks to implement. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

**Controls:** Use A / D or Left / Right arrows to slide the basket. Press R to restart after Game Over.

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the floor miss scoring and life deduction bug

Dropping fruits onto the floor improperly rewards points instead of penalizing the player, and lives never decrease, making it impossible to lose. Correct the miss handling so dropping fruits deducts a life and triggers Game Over when all lives are lost, ensuring points are only earned on valid basket catches.

### Task 2: Implement rotten fruit & hazard bombs

The player currently only catches beneficial items without needing to dodge. Introduce falling hazard items that deduct lives or penalize score if collected in the basket.
 
### Task 3: Implement dynamic falling speed escalation

Fruits currently drop at fixed intervals and constant speeds. Gradually increase the challenge as score climbs by shrinking the spawn delay and increasing the baseline falling speed of newly spawned objects/

### Task 4: Implement fruit splash particle effects

Caught or dropped fruits instantly disappear from the screen. Add visual feedback using a lightweight particle system that emits colored splash droplets whenever a fruit lands in the basket or splatters against the floor.

---

## Expected Behavior

- Sliding the basket catches falling fruits, removing them and awarding +1 point per catch.
- Missing a fruit and letting it touch the ground deducts 1 life without increasing the score.
- Losing all 3 lives displays the GAME OVER banner and freezes further updates.
- Pressing R after losing resets the score, restores lives to 3, and clears lingering fruits.

## Folder Structure

```
fruit_catcher/
├── game/
│   ├── basket.py
│   ├── fruit.py
│   └── game_engine.py
├── main.py
└── README.md
```

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
