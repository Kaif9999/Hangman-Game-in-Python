# Hangman-Game-in-Python
Hangman Game in Python  Classic word-guessing fun in Python. Try to guess the hidden word one letter at a time. Customize the word list and enjoy Python programming. Fork and play! 🎮🐍

This Python project is a text-based Hangman game, a classic word-guessing game. In this game, you try to guess a hidden word by entering one letter at a time. The game includes a set number of lives, and you'll lose a life for each incorrect guess. The objective is to guess the word before running out of lives.



**Project Overview:**
This Python project is a text-based Hangman game, a classic word-guessing game where you try to guess a hidden word one letter at a time. The game provides a limited number of lives, and your goal is to guess the word before running out of lives.

### Getting Started

1. Clone the Repository
   ```bash
   git clone <repository-url>
   ```
2. Run the Game
  ```bash
   python hangman.py
  ```
### Key Components:

1. Random Word Selection:

The game selects a random word from a predefined list.
Word Display Initialization:

A list named display is created with dashes representing unguessed letters.
Game Loop:

The game runs in a loop until it's over.
Checking the Guess:

The code checks if the letter has already been guessed and provides feedback.
It also checks if the guessed letter is in the chosen word and updates the display accordingly.
If the letter is not in the chosen word, the player loses a life. If lives run out, the game ends with a "You Lose" message.
Winning the Game:

If all letters are guessed, and there are no dashes left in the display, the game ends with a "You Win" message.

### Customization
You can customize this game by adding more words to the word_list or modifying the visual elements like the Hangman stages.

### Visual Feedback
The Hangman stages are displayed as ASCII art to provide a visual representation of the player's progress.


### Contribution
This project is open to contributions. Feel free to suggest improvements or add new features.

### License
This project is under the MIT License.

Enjoy playing, and happy coding!
