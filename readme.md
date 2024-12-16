# Tic Tac Toe Game

A Python-based **Tic Tac Toe** game with a graphical user interface (GUI) implemented using **Tkinter**. This project supports both single-player mode (against the computer) and two-player mode, offering a fun and interactive way to play this classic game.

## Features

- **Single-Player Mode**: Play against an AI opponent.
- **Two-Player Mode**: Play with a friend on the same computer.
- **Custom Symbol Selection**: Choose whether the first player uses `X` or `O`.
- **Interactive GUI**: Simple and clean graphical interface using Tkinter.
- **Reset Option**: Restart the game easily at any point.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. **Install dependencies**:
    - Make sure you have Python 3.7 or higher installed.
    - Install the required packages (e.g., NumPy):
        ```bash
        pip install numpy
        ```

3. **Run the game**:
    ```bash
    python main.py
    ```

---

## How to Play

### **Game Modes**
- **Single-Player Mode**:
  - You play against the computer.
  - Toggle the mode to `1P` (single player) in the settings.
  - The computer will make its moves automatically.

- **Two-Player Mode**:
  - Toggle the mode to `2P` (two players) in the settings.
  - Both players take turns on the same device.

### **Customizing Symbols**
- You can choose whether the first player uses `X` or `O` by clicking on the toggle for symbols before starting the game.

### **Starting the Game**
1. Choose the game mode and symbols.
2. Click the **Start** button to begin.
3. Players take turns clicking on the grid to mark their symbol.
4. The game announces a winner when a row, column, or diagonal is completed with the same symbol.

---

## File Structure

```plaintext
.
├── main.py             # Entry point for the game
├── game.py             # Game logic and AI functionality
├── ui.py               # Tkinter GUI implementation
├── assets/             # Image assets used in the game
│   ├── toggle-on.png
│   ├── toggle-off.png
│   ├── 1p.png
│   ├── 2p.png
│   ├── cross.png
│   ├── circle.png
│   ├── blank.png
│   ├── red-cross-100.png
│   ├── blue-circle-100.png
│   └── tic-tac-toe.ico
└── README.md           # Project documentation
```

---

## Code Overview

### **game.py**
This file contains the core logic of the game, including:
- **Game Board Management**: Keeps track of the board state.
- **AI Logic**: Determines the computer's moves in single-player mode.
- **Win Conditions**: Checks for a winning line or a draw.

### **ui.py**
This file handles the graphical user interface, featuring:
- Game grid creation.
- Player interactions.
- Dynamic updates to reflect game state.

### **main.py**
The entry point of the application, which initializes the `GameBrain` and `GameInterface` classes.

---

## Dependencies

- **Python 3.7+**
- **NumPy**: Used for managing the game state efficiently.
    ```bash
    pip install numpy
    ```
- **Tkinter**: Comes pre-installed with Python for GUI development.

---

## How It Works

### **Single-Player Mode (AI Logic)**
The computer makes random moves on empty tiles. The moves are chosen using the `numpy` library to ensure valid placement.

### **Two-Player Mode**
Each player takes turns clicking on the grid. The game automatically checks for a winner after every move.

### **Winning Conditions**
The game checks for three matching symbols (`X` or `O`) in:
- A row
- A column
- A diagonal

---


## Future Improvements

- Add a smarter AI opponent with difficulty levels.
- Implement an online multiplayer mode.
- Add animations and sound effects for better user experience.
- Make the GUI responsive for different screen sizes.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## Contact

For any questions or suggestions, feel free to reach out:
- **Email**: wlqinnovations@example.com
- **GitHub**: [wlqinnovations](https://github.com/wlqinnovations)
