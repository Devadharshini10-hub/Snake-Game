# 🐍 Classic Snake Game - Python Turtle Edition

This is a simple and fun implementation of the classic Snake Game using Python's Turtle Graphics library. The project is modular, cleanly structured with OOP principles, and includes features like increasing difficulty, a scoreboard with high score tracking, and reset mechanics upon collision.

---

## 🚀 Features

* Classic snake movement with arrow key control
* Food spawning in random locations
* Snake grows with each food eaten
* Scoreboard with persistent high score (saved in `data.txt`)
* Wall and self-collision detection with automatic reset

---

## 🗂️ Project Structure

```
📁 snake-game/
├── food.py         # Food logic - random placement and appearance
├── main.py         # Game loop and screen setup
├── scoreboard.py   # Score tracking and high score handling
├── snake.py        # Snake movement and behavior
└── data.txt        # Stores high score persistently
```

---

## 🧑‍💻 How to Run

### Requirements

* Python 3.x installed on your system
* No external packages required – uses built-in `turtle`, `time`, and `random` modules

### Steps

1. Clone this repository or download the files.
2. Make sure a file named `data.txt` with a numeric value (`0` if starting fresh) exists in the same directory.
3. Run the game:

   ```bash
   python main.py
   ```
4. Use the arrow keys (↑ ↓ ← →) to control the snake.

---

## 📸 Screenshots

> Add your own screenshots here, if available:

```
[Game window with black background, snake, blue/red food, and white score text on top]
```

---

## 📌 Game Rules

* Each time the snake eats food, it grows and your score increases.
* If the snake hits the wall or itself, the score resets but high score remains.
* Food appears randomly; red food may act as a power-up (based on your logic).

---

## 🛠️ Technologies Used

* Python
* Turtle Graphics module

