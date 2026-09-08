# Python Quiz Game

print("Welcome to the Quiz Game!")
print("You will be asked 5 questions. Type the letter of the correct answer (A, B, C, or D).")
print("Let's get started!\n")
print("-----QUIZ TIME-----")
questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Which element has the chemical symbol 'O'?",
    "Who painted the Mona Lisa?",
    "What is the hardest natural substance on Earth?"
)

options = (
    ("A) London", "B) Berlin", "C) Paris", "D) Madrid"),
    ("A) Jupiter", "B) Saturn", "C) Neptune", "D) Uranus"),
    ("A) Gold", "B) Oxygen", "C) Silver", "D) Hydrogen"),
    ("A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"),
    ("A) Diamond", "B) Graphite", "C) Platinum", "D) Emerald")
)

answers = ("C", "A", "B", "C", "A")
guess = []
score = 0
question_sum = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_sum]:
        print(option)
    user_guess = input("Enter your answer (A, B, C, or D): ").upper()
    guess.append(user_guess)
    if user_guess == answers[question_sum]:
        score += 1
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {answers[question_sum]}.\n")
    question_sum += 1

print(f"Your final score is: {score}/{len(questions)}")

