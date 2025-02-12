# US States Game 🇺🇸  
A Python-based game where players guess U.S. states by name to see them appear on a map. The game tracks the player's progress and saves any missed states to a CSV file for review.  

---

## How to Run  
### Prerequisites  
Ensure you have Python and the required libraries installed. This project uses the `turtle` and `pandas` libraries.  

### Steps  
1. **Clone the repository** (or download the script manually):  
   ```sh
   git clone https://github.com/your-username/us-states-game.git
   cd us-states-game
2. **Install required libraries**: <br>
  If you haven't installed pandas, run:
    ```sh
    pip install pandas
    ```
3. **Run the script**:
   ```sh
   python main.py
   ```
4. Game Interaction: <br>
The game will prompt you to guess the name of a U.S. state. When you type the correct state name, it will appear on the map. If you type an incorrect answer, it will count as an attempt, but it won't display anything on the map.

5. Exit and Results: <br>
To exit the game at any time, type "Exit". The game will then save a CSV file named `states_missed.csv` containing all the states you missed during the game.

---

## Controls  

| Action                   | Input                                  |
|--------------------------|----------------------------------------|
| Guess the state          | Type the state name in the input prompt |
| Exit the game            | Type "Exit" in the input prompt        |

---

## Notes
🗺️ **Interactive Map** <br>
When you correctly guess a state, it will appear on a blank U.S. map image.

🎮 **Gameplay** <br>
The game prompts the player to guess states until all states have been guessed or the player exits the game.

📝 **CSV Output** <br>
If the player exits the game, the states they missed will be saved in a CSV file (states_missed.csv).

⚡ **Turtle Graphics** <br>
The turtle library is used to display the state names on the map, giving the game a visual aspect.

📚 **Data** <br>
The state coordinates and names are pulled from a CSV file (50_states.csv).

🚪 **Exit Functionality** <br>
The player can exit the game at any time by typing "Exit".
