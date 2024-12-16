import random

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def shuffle_questions(self):
        random.shuffle(self.question_list)

    def still_has_questions(self):
        """Returns True if there are remaining questions in the question bank"""
        return self.question_number < 10

    def next_question(self):
        """Gets and Checks user answer for current question and increments to next question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q{self.question_number}: {current_question.text}")
        print(f"Difficulty: {current_question.difficulty.capitalize()}")  # Display difficulty level
        user_answer = input("\nTrue or False: ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks user answer for current question to the correct answer in question bank"""
        # Normalize user input
        if user_answer in ["t", "true"]:
            user_answer = "True"
        elif user_answer in ["f", "false"]:
            user_answer = "False"
        else:
            print("\nInvalid input. Please enter 't', 'f', 'true', or 'false'.")
            return
        
        # Check if user answer is same as correct answer
        if user_answer.lower() == correct_answer.lower():
            print("\nYou got it right!")
            self.score += 1
        else:
            print("\nOops, you got it wrong.")

        # Print out correct answer and user's current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"\nYour current score is: {self.score}/{self.question_number}")
        print("")
