import tkinter as tk
from tkinter import messagebox

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the largest mammal in the world?"
        ]

        self.choices = [
            ["Paris", "London", "Berlin", "Madrid"],
            ["Mars", "Venus", "Earth", "Jupiter"],
            ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
            ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"]
        ]

        self.correct_answers = [0, 2, 0, 1]
        self.user_answers = [tk.IntVar() for _ in range(len(self.questions))]

        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.radio_buttons = [None] * 4
        for i in range(4):
            self.radio_buttons[i] = tk.Radiobutton(root, text="", variable=self.user_answers[i], value=i)
            self.radio_buttons[i].pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_score)
        self.submit_button.pack(pady=10)

        self.next_question(0)

    def next_question(self, question_number):
        self.question_label.config(text=self.questions[question_number])

        for i in range(4):
            self.radio_buttons[i].config(text=self.choices[question_number][i])

    def calculate_score(self):
        score = 0
        for i in range(len(self.questions)):
            if self.user_answers[i].get() == self.correct_answers[i]:
                score += 1
        messagebox.showinfo("Result", f"Your score: {score}/{len(self.questions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()
