# Quiz Game
This is a simple quiz game that pulls 10* questions from Open Trivia DB by creating a custom API url using the OTDB format. This game will simply ask the user 10 True/False questions and report if the user was correct or not and display the current user score and eventually display the overall score at the end of the quiz. This was an initial attempt at OOP to help simplify code adjustments through modularization. 

---

## How to Run  
### Prerequisites  
Ensure you have Python installed (version 3.x recommended) and the required dependencies:  

```sh
pip install tabulate
```

### Steps
1. **Clone the repository** (or download the script manually):
   ```sh
   git clone https://github.com/your-username/quiz-game.git
   cd quiz-game
   ```
2. **Run the game**:
   ```sh
   python main.py
   ```

---

## Controls

| Action              | Input                    |
|---------------------|-------------------------|
| Select a category  | Enter the category ID   |
| Answer a question  | Type your answer and press Enter |

---

# Features
**Multiple Categories** – Choose from various trivia categories, such as Science, Entertainment, History, and more. <br>
**API Integration** – Fetches real-time questions from Open Trivia Database (OpenTDB). <br>
**Shuffled Questions** – The order of questions is randomized for a fresh experience each time. <br>
**Varying Difficulty** – Questions come in Easy, Medium, and Hard levels. <br>
**Score Tracking** – Your final score is displayed at the end of the game. <br>
**Neatly Displayed Categories** – Uses tabulate to present category choices in an easy-to-read format. <br>
