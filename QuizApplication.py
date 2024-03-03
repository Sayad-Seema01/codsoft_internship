import tkinter as tk
from tkinter import ttk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x500")
        self.root.configure(background="#000000")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "Madrid", "Rome"], "correct_answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct_answer": "Mars"},
            {"question": "What is the largest mammal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "correct_answer": "Blue Whale"}
            # Add more questions as needed
        ]

        self.current_question_index = 0
        self.score = 0

        # Widgets
        self.welcome_label = ttk.Label(root, text="Welcome to the Quiz App!", font=('Helvetica', 16, 'bold'), foreground="#3498db", background="#000000")
        self.rules_label = ttk.Label(root, text="Rules:\n1. Answer all questions.\n2. Each correct answer gives you 1 point.", foreground="#ffffff", background="#000000")
        self.question_label = ttk.Label(root, text="", font=('Helvetica', 14), foreground="#ffffff", background="#000000")
        self.option_buttons = [ttk.Button(root, text="", command=lambda i=i: self.check_answer(i), style="TButton") for i in range(4)]
        self.feedback_label = ttk.Label(root, text="", foreground="#ffffff", background="#000000")
        self.score_label = ttk.Label(root, text="", foreground="#ffffff", background="#000000")
        self.next_button = ttk.Button(root, text="Next", command=self.next_question, style="TButton")
        self.play_again_button = ttk.Button(root, text="Play Again", command=self.reset_quiz, style="TButton")

        # Style
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12), foreground="#000000", background="#BFEA7C")
        style.map("TButton", foreground=[("pressed", "black"), ("active", "#BFEA7C")])

        # Grid layout
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.rules_label.grid(row=1, column=0, columnspan=2, pady=10)
        self.question_label.grid(row=2, column=0, columnspan=2, pady=10)
        for i, button in enumerate(self.option_buttons):
            button.grid(row=3 + i, column=0, columnspan=2, pady=5)
        self.feedback_label.grid(row=7, column=0, columnspan=2, pady=10)
        self.score_label.grid(row=8, column=0, columnspan=2, pady=10)
        self.next_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.play_again_button.grid(row=10, column=0, columnspan=2, pady=10)

        self.reset_quiz()

    def reset_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)

            self.feedback_label.config(text="")
            self.score_label.config(text=f"Score: {self.score}/{self.current_question_index}")
        else:
            self.show_final_results()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["correct_answer"]

        if self.option_buttons[selected_option]["text"] == correct_answer:
            self.feedback_label.config(text="Correct!", foreground="#2ecc71")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. Correct answer: {correct_answer}", foreground="#e74c3c")

        self.current_question_index += 1
        self.show_question()

    def show_final_results(self):
        self.question_label.config(text="")
        self.feedback_label.config(text="")
        self.score_label.config(text=f"Final Score: {self.score}/{len(self.questions)}")

        if self.score == len(self.questions):
            message = "Congratulations! You answered all questions correctly."
        elif self.score >= len(self.questions) / 2:
            message = "Well done! You passed the quiz."
        else:
            message = "Better luck next time."

        self.feedback_label.config(text=message, foreground="#3498db")
        self.next_button.config(state=tk.DISABLED)
        self.play_again_button.grid(row=10, column=0, columnspan=2, pady=10)

    def next_question(self):
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.show_final_results()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
