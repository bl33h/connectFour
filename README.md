# connectFour
This project is an implementation of Connect Four with a graphical user interface using Python and Pygame. It supports both player versus AI and AI versus AI gameplay modes, providing an engaging experience for users to challenge the computer or observe AI battles. The AI logic is powered by the MiniMax algorithm, which can optionally use alpha-beta pruning to enhance performance by reducing the number of nodes evaluated in the decision-making process.

<p align="center">
  <br>
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTZkdjl2eW91dDlwbWlwdWk0aW85M2s2MGgxNm9rdGRzc2JrZGc1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hGvTQoPJCDKQEK23to/giphy.gif" alt="pic" width="500">
  <br>
</p>

<p align="center">
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a>
</p>

## Files
- board.py: Manages the game board representation and operations.
- connect4.py: Core game logic implementation, utilizing the MiniMax algorithm.
- game.py: Integrates all components (board, game logic, GUI) and manages the game flow.
- gui.py: Provides the graphical interface using Pygame, handling user interactions and rendering.
- main.py: Main entry point for starting the game application.
- main_menu.py: Handles the main menu logic and transitions.
- minimax.py: Implements the MiniMax algorithm with optional alpha-beta pruning for AI.

## Features
- Player vs. AI and AI vs. AI Modes: Play against an intelligent AI or watch an AI vs. AI showdown.
- Graphical User Interface: Fully interactive GUI with dynamic updates during gameplay.
- Intelligent AI: AI uses MiniMax algorithm, optionally enhanced with alpha-beta pruning for efficiency.

- **Version I**: This is the initial version of the simulation, designed to explore and measure the efficiency of the integer division operation.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/bl33h/connectFour

# Open the project
$ cd src

# Run the app
$ python main.py
