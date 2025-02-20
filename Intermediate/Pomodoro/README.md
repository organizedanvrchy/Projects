# Pomodoro Timer
A simple Pomodoro Timer built using Python's Tkinter library. This application helps users follow the Pomodoro Technique, a time management method that alternates between work sessions and breaks to improve productivity.

## How to Run
1. Ensure you have Python installed on your system (Python 3.x recommended).
2. Install Tkinter if not already installed (Tkinter is included by default in standard Python installations).
3. Save the provided `pomodoro.py` script along with an image file named `tomato.png` in the same directory.
4. Open a terminal or command prompt and navigate to the script's directory.
5. Run the script using:
   ```sh
   python pomodoro.py
   ```

## Features
- **Pomodoro Timer**: Implements the classic 25-minute work session followed by short and long breaks.
- **Automated Cycles**: The timer automatically switches between work and break sessions.
- **Visual Feedback**: Displays a tomato image along with a countdown timer.
- **Check Marks**: Tracks completed work sessions with checkmarks.
- **Start and Reset**: Users can start a session and reset the timer at any time.
- **Customizable Durations**: Easily modify work and break durations by changing the `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` values in the script.
