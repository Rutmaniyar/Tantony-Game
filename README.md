# 🐷 Tantony Game: A Trick-Taking Strategy Card Game

Tantony is a unique and strategic trick-taking card game for four players, originally designed by David Parlett. Unlike traditional trick games, Tantony allows players to **assign won tricks** to other players — including their opponents — adding a rich layer of strategy and bluffing.

This is a fully-functional **console-based implementation in Python** of the complete Tantony ruleset, including:

- 💥 Trick transfer system (winner chooses the recipient)
- ♠️ Trick scoring based on the **lowest card in the lead suit** (the "runt")
- 🧠 Tactical play to manage trick quotas (each player must receive exactly 3 per hand)
- 👥 Partnership-based play and scoring system
- 🎯 Full 4-hand game with scoring and leader rotation

---

## 🃏 Game Rules Overview

- 4 players in 2 teams (1 & 3 vs. 2 & 4).
- 52-card deck, no trump.
- Players must follow suit if possible.
- Highest card in lead suit wins the trick (called the “sow”).
- The value of the trick is the **value of the lowest card in the lead suit**.
- The winner of the trick assigns it to any player who hasn’t yet received 3 tricks.
- The trick's recipient leads the next.
- After 13 tricks, score is calculated based on the “runts” received.

---

## 🖥️ Getting Started

### 📦 Prerequisites

- Python 3.10 or later

### ▶️ How to Run

```bash
git clone https://github.com/yourusername/tantony-card-game.git
cd tantony-card-game
python tantony_game.py
