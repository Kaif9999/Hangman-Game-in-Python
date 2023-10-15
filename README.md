# Hangman-Game-in-Python
Hangman Game in Python  Classic word-guessing fun in Python. Try to guess the hidden word one letter at a time. Customize the word list and enjoy Python programming. Fork and play! 🎮🐍

This Python project is a text-based Hangman game, a classic word-guessing game. In this game, you try to guess a hidden word by entering one letter at a time. The game includes a set number of lives, and you'll lose a life for each incorrect guess. The objective is to guess the word before running out of lives.

#Key Components:

#Imported Libraries:

random: Used to select a random word from the list of words.
word_list: A list of words to choose from.
stages: ASCII art representing the Hangman stages as you progress.
logo: ASCII art representing the game logo.
Initialization:

A random word is chosen from the word_list.
The player starts with 6 lives.
The game displays the Hangman logo.
Word Display Initialization:

A list named display is created, filled with dashes representing unguessed letters.
Game Loop:

The game runs in a loop until it's over.
The player enters a letter guess.
Checking the Guess:

The code checks if the letter has already been guessed and provides feedback.
It also checks if the guessed letter is in the chosen word and updates the display accordingly.
If the letter is not in the chosen word, the player loses a life. If lives run out, the game ends with a "You Lose" message.
Winning the Game:

If all letters are guessed and there are no dashes left in display, the game ends with a "You Win" message.
Visual Feedback:

The Hangman stages are displayed as ASCII art to provide a visual representation of the player's progress.
This is a simple and fun project that's a great way to practice Python programming. It's customizable - you can add more words to the word_list or even expand its features. Enjoy playing, and happy coding!


