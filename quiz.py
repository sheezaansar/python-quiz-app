class Question:
    def __init__(self, text, correct_answer, q_type="true_false", options=None):
        self.text = text
        self.correct_answer = correct_answer
        self.q_type = q_type
        self.options = options if options else []

    def check_answer(self, user_input):
        user_input = user_input.strip().lower()
        correct = self.correct_answer.strip().lower()

        if self.q_type == "mcq" and user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index < len(self.options):
                return self.options[index].strip().lower() == correct
            return False

        return user_input == correct
    def ask(self):
        print(self.text)
        if self.q_type == "mcq":
            for i, opt in enumerate(self.options, 1):
                print(f"{i}. {opt}")
        user_input = input("Your answer: ")
        if self.check_answer(user_input):
            print("✅ Correct!\n")
            return True
        else:
            print(f"❌ Wrong. Correct answer: {self.correct_answer}\n")
            return False


class QuizBank:
    def __init__(self, filepath):
        self.filepath = filepath
        self.questions = []

    def load(self):
        import json
        with open(self.filepath, "r") as f:
            data = json.load(f)
        for q in data:
            self.questions.append(
                Question(
                    q["text"],
                    q["correct_answer"],
                    q.get("type", "true_false"),
                    q.get("options", [])
                )
            )
        return self.questions


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for q in self.questions:
            if q.ask():
                self.score += 1
        self.show_result()

    def show_result(self):
        print(f"Final Score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    bank = QuizBank("questions.json")
    questions = bank.load()
    quiz = Quiz(questions)
    quiz.run()