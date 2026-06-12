
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input. Students will practice control flow, string manipulation, and simple I/O.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Create a playable Hangman program that selects a hidden word and lets the player guess letters until they either reveal the word or run out of attempts. Provide clear prompts, show the current progress of the word, and display remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Accept single-letter guesses and update the displayed progress (e.g., `_ a _ _ _`).
- Track and display incorrect guesses remaining.
- Prevent repeated penalties for guessing the same correct letter multiple times.
- End the game with a clear win or lose message and reveal the word when the player loses.

## ✅ Starter files

- Starter code: [assignments/games-in-python/starter-code.py](assignments/games-in-python/starter-code.py)

## Example

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess! Word: _ a _ _ _
Incorrect guesses remaining: 5
```

## Notes for instructors

- Keep the word list moderate in size and appropriate for the students' level.
- Encourage adding features like letter validation, hints, or difficulty levels as optional extensions.
