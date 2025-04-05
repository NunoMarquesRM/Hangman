# Hangman Game

A classic implementation of the Hangman word-guessing game in Python. This project features ASCII art, a comprehensive word list, and an interactive command-line interface.

## 🎮 Game Features

- Classic Hangman gameplay with 6 lives
- ASCII art visualization of the hangman
- Extensive word list with 216 carefully selected words
- Clear visual feedback for game progress
- Input validation and duplicate guess prevention
- Win/lose condition tracking

## 🚀 How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Game Rules:
   - You have 6 lives to guess the hidden word
   - Guess one letter at a time
   - Each correct guess reveals the letter in the word
   - Each wrong guess brings the hangman closer to completion
   - Win by guessing all letters before the hangman is complete
   - Lose if the hangman is completed before guessing the word

## 📁 Project Structure

- `main.py` - Core game logic and main game loop
- `hangman_art.py` - ASCII art for the game stages and logo
- `hangman_words.py` - Comprehensive list of words for the game

## 🛠️ Requirements

- Python 3.x

## 🎯 Game Example

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _ _ _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: 
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements. Some potential enhancements could be:

- Adding difficulty levels
- Implementing a scoring system
- Adding sound effects
- Creating a high score system
- Adding a play again option
- Implementing a GUI version

## 📝 License

This project is open source and available under the MIT License.

## 👏 Acknowledgments

- ASCII art created for educational purposes
- Word list curated for optimal gameplay experience 