# Higher Lower Game

Higher Lower game is a fun command-line game where players guess which of two random accounts has more followers on social media. For each correct guess, the player’s score increases. The game continues until the player makes an incorrect guess.

## Table of Contents

- [Game Overview](#game-overview)
- [How to Play](#how-to-play)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

## Game Overview

In this Higher Lower Game, you’ll compare two randomly selected accounts and guess which one has more followers. You can keep guessing as long as you're correct. The game ends when you make an incorrect guess.

## How to Play

1. Run the game from the command line.
2. Two accounts (A and B) will be displayed with brief descriptions.
3. Guess which account has more followers by entering either **A** or **B**.
4. If correct, your score will increase, and the game will continue with a new comparison.
5. If incorrect, the game will end, and your final score will be displayed.

## Features

- Compare two accounts and guess which one has more followers.
- Tracks the player’s score across multiple rounds.
- Randomized selection of accounts to ensure a unique experience each time.

## Prerequisites

- Python 3.x installed on your machine.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/AllenzoPaul/Higher-Lower-game.git

2. Navigate to the project directory:
    ```bash 
    cd higher-lower-game

3. Run the game:
    ```bash 
    python higher_lower_game.py

## Project Structure

- higher_lower_game.py: Main game logic, displays options, and checks answers.
- game_data.py: Contains data about each account, including names, descriptions, countries, and follower counts.
- art.py: Contains ASCII art for logos and visual elements.

## Future Improvements

- Add more accounts for greater variety.
- Add a leaderboard to track high scores.
- Include a graphical interface for improved user interaction.
