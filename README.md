# 🐍 Snake Game (Terminal Edition)

Welcome to the **Terminal Snake Game**, a retro-style game built entirely in Python using the `curses` library!  
This was a fun little **2-hour Saturday project**, crafted with care and nostalgia to bring the classic Snake to your terminal.  
Enjoy animated intros, ASCII snakes, dynamic difficulty levels, and a responsive, fast-paced gameplay loop — all inside your terminal window!

---

## 🎮 Features

- 🐍 Classic Snake gameplay
- 🎞 ASCII animation intro with moving snakes
- ⏳ Animated loading and blinking title effects
- 🎚 Difficulty selector with 10 levels, from *Very Easy* to *Impossible*
- 🍎 Fruits randomly appear, and eating them increases your score
- 🧱 Game Over screen with terminal-filling animation
- 💀 Snake collision with walls or itself ends the game

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x

### 💻 Windows Users

Python’s `curses` library is not included by default on Windows.  
To run this game on Windows, **you must install**:

```bash
pip install windows-curses
```

> You can run the game inside a terminal like Windows Terminal, Git Bash, or WSL. PowerShell/CMD may have issues with rendering.

### ▶️ Running the Game

```bash
python snake_game.py
```

> You'll be greeted with a cinematic intro. Use arrow keys to select difficulty and hit **ENTER** to begin!

---

## 🎮 Controls

| Key         | Action               |
|-------------|----------------------|
| ↑ / ↓ / ← / → | Move the snake        |
| ENTER       | Select difficulty     |
| ESC         | Quit the game         |


---

## 🧠 About the Code

- **`game_loop`**: Core loop that controls snake movement, collision, and scoring.
- **`intro_animation`**: Multi-phase intro with ASCII animation, loading bar, and difficulty selector.
- **`draw_*` functions**: Handle rendering of snake, fruit, and UI borders.
- **`curses.wrapper(start)`**: Safely initializes and terminates the terminal in a clean state.

---

## 📁 File Structure

```plaintext
snake_game.py   # All game logic in a single file
README.md       # You're here!
```

---

## 💡 Tips

- Start on **Moderate** for a balanced experience.
- As difficulty increases, game speed becomes faster.
- Try reaching a high score on **Impossible**... if you dare 🧠🔥

---

## 📜 License

This project is free and open-source under the MIT License.

---

Made with ❤️ in the terminal — and coded in just 2 hours on a Saturday.
