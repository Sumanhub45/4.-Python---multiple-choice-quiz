
class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer == self.correct_answer

class QuizGame:
    def __init__(self):
        self.questions = [
            Question("What is the capital of France?", ["A. London", "B. Madrid", "C. Paris", "D. Rome"], "C"),
            Question("Which planet is known as the Red Planet?", ["A. Mars", "B. Jupiter", "C. Saturn", "D. Venus"], "A"),
            Question("What is the largest mammal in the world?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Rhino"], "B"),
        ]
        self.score = 0

    def start(self):
        print("Welcome to the Quiz Game!\n")
        for question in self.questions:
            self.ask_question(question)
        self.display_score()

    def ask_question(self, question):
        print(question.question)
        for option in question.options:
            print(option)
        answer = input("Your answer (enter the letter): ").upper()
        if question.is_correct(answer):
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong. The correct answer is {question.correct_answer}.\n")
        self.current_question += 1

    def display_score(self):
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start()
