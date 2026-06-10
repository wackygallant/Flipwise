# Flipwise 📚

A modern, interactive flashcard study application built with Python and CustomTkinter. Study efficiently with a clean UI, track your progress, and manage your cards all in one place.

## Features ✨

- **Quiz Mode**: Study flashcards one at a time with reveal functionality
- **Add Cards**: Easily create new flashcards with questions and answers
- **Track Progress**: Monitor your learning with:
  - Total cards count
  - Correct/Incorrect answer tracking
  - Accuracy percentage
  - Per-card statistics
- **Persistent Storage**: All cards are automatically saved to `data/cards.json`
- **Dark Theme**: Easy on the eyes with a modern dark interface

## Installation 🚀

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone or download this project**
   ```bash
   cd Flipwise
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install customtkinter
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

## Usage 📖

### Quiz Tab
- Study your flashcards one at a time
- Click **"Reveal Answer"** to see the answer
- Mark your response as:
  - **Got it** ✓ (correct)
  - **Missed it** ✗ (incorrect)
- Your progress updates automatically

### Add Card Tab
- **Question**: Enter your question or prompt
- **Answer**: Type the answer (supports multi-line text)
- Click **"Add Flashcard"** to save
- **Delete**: Remove cards by entering their index number (0, 1, 2, etc.)

### Stats Tab
- View your **accuracy percentage**
- See total cards and correct/incorrect counts
- Browse individual card statistics including:
  - Question preview
  - Correct attempts
  - Total attempts
  - Accuracy for that card

## Project Structure 📁

```
Flipwise/
├── main.py              # Main application entry point
├── deck.py              # Deck class for managing flashcards
├── flashcard.py         # FlashCard class for individual cards
├── test.py              # Test file (optional)
├── data/
│   └── cards.json       # Stored flashcards (auto-generated)
└── README.md            # This file
```

## File Descriptions

- **main.py**: Contains the `FlipwiseApp` class with the GUI interface and all user interactions
- **deck.py**: Manages the collection of flashcards, including loading/saving to JSON
- **flashcard.py**: Defines the `FlashCard` class with properties for tracking answers
- **cards.json**: JSON file storing all your flashcards (created automatically)

## Data Format 💾

Flashcards are stored in `data/cards.json` in the following format:

```json
{
  "cards": [
    {
      "question": "What is the capital of France?",
      "answer": "Paris",
      "correct": 2,
      "attempted": 3
    }
  ]
}
```

## Tips for Effective Studying 💡

1. **Create specific questions**: More detailed questions lead to better retention
2. **Review regularly**: The stats tab helps you identify weak areas
3. **Check accuracy**: Focus on cards where you have low accuracy
4. **Add variety**: Mix different topics to keep your studying engaging

## Requirements 📋

- Python 3.8+
- customtkinter 5.0+

## License 📄

This project is open source and available for personal and educational use.

## Support 🤝

If you encounter any issues or have suggestions, feel free to improve the code!

---

**Happy studying! 🎓**
