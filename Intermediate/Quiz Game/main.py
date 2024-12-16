import html

from tabulate import tabulate
from logo import logo
from question_model import Question
from data import fetch_questions
from quiz_brain import QuizBrain

def display_categories(categories):
    """Display categories in a table format with 3 columns, sorted by ID."""
    # Sort categories by their IDs
    sorted_categories = sorted(categories.items())

    # Format categories into rows of 3
    rows = []
    row = []
    for index, (id, name) in enumerate(sorted_categories, start=1):
        row.append(f"{id}: {name}")
        if index % 3 == 0:  # Add a new row after every 3 items
            rows.append(row)
            row = []
    if row:  # Add the remaining row if any
        rows.append(row)

    # Print the table using tabulate
    print("\nAvailable Categories:")
    print(tabulate(rows, tablefmt="grid"))

def main():
    print(logo)
    input("\nWelcome! Press Enter to continue...")

    # Categories from OpenTDB
    categories = {
        9: "General Knowledge",
        10: "Entertainment: Books",
        11: "Entertainment: Film",
        12: "Entertainment: Music",
        13: "Entertainment: Musicals & Theatres",
        14: "Entertainment: Television",
        15: "Entertainment: Video Games",
        16: "Entertainment: Board Games",
        17: "Science & Nature",
        18: "Science: Computers",
        19: "Science: Mathematics",
        20: "Mythology",
        21: "Sports",
        22: "Geography",
        23: "History",
        24: "Politics",
        25: "Art",
        26: "Celebrities",
        27: "Animals",
        28: "Vehicles",
        29: "Entertainment: Comics",
        30: "Science: Gadgets",
        31: "Entertainment: Japanese Anime & Manga",
        32: "Entertainment: Cartoon & Animations",
    }

    display_categories(categories)

    # Get user input for category
    try:
        category = int(input("\nEnter the category ID: "))
        if category not in categories:
            print("Invalid category. Exiting.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    amount = 10

    # Fetch questions from the API
    question_data = fetch_questions(category, amount)
    if not question_data:
        return  # Exit if no questions were fetched

    # Display and run quiz
    question_bank = []
    for question in question_data:
        q_text = html.unescape(question["question"])
        q_answer = question["correct_answer"]
        q_difficulty = question["difficulty"]
        new_question = Question(q_text, q_answer, q_difficulty)
        question_bank.append(new_question)

    # Add questions to quiz
    quiz = QuizBrain(question_bank)

    # Shuffle questions
    quiz.shuffle_questions()

    # Run quiz
    print("")
    while quiz.still_has_questions():
        quiz.next_question()

    print("Congratulations! You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()
