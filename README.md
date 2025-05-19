# 🐷 Tantony: Piglet Power – A Trick-Taking Strategy Card Game

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
git clone https://github.com/Rutmaniyar/Tantony-Game.git
cd tantony-card-game
python tantony_game.py
```

> All interactions are via the console. Players type in card choices (e.g., `2 of Hearts`) and recipient selections during gameplay.

---

## 📚 Project Structure

- `tantony_game.py` – Main Python script containing all game logic.
- `README.md` – You’re reading it.

---

## 💡 Strategy Tips

- Keep an eye on your opponents' trick quotas — first low-value tricks on them early!
- Assign tricks to your partner if you want to control the next lead.
- Try to set up a high “hog” (Ace lead when no one else can follow suit).

---

## 🧩 Possible Enhancements

- Add memory/recap system for played tricks
- GUI using PyQt6 or Pygame
- Web version with Flask + WebSockets
- AI players for solo or mixed play

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Credits

- Original game design: [David Parlett](https://www.parlettgames.uk/oricards/tantony.html)
- Python implementation by Rut Maniyar

---

Enjoy the tactical chaos of Tantony — where even winning a trick might not be in your best interest!
