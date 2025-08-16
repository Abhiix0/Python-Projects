#Quiz game

print("Welcome to the Quiz game!")
score = 0
question_num = 0
guesses = []
questions = (
    "What is the capital of France?",
    "What is 2 + 2?",        
    "What is the largest planet in our solar system?",
    "What is the boiling point of water in Celsius?",
    "Who wrote 'Romeo and Juliet?'"
)
answers = (
    "A",  # Paris
    "B",  # 4
    "C",  # Jupiter
    "B",  # 100
    "A"   # Shakespeare
)
options = (
    ("A) Paris", "B) London", "C) Berlin", "D) Madrid"),  
    ("A) 3", "B) 4", "C) 5", "D) 6"),
    ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"),
    ("A) 90", "B) 100", "C) 110", "D) 120"),
    ("A) Shakespeare", "B) Dickens", "C) Austen", "D) Tolkien")
)

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
      print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    guesses.append(user_answer)
    if user_answer == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answers[question_num]}.")
    question_num += 1

print("----------------------------------")
print("Quiz completed! Results Time:")        
print(f"Your score is {score} out of {len(questions)}.")
if score == len(questions):
    print("Congratulations! You got all answers correct!")  
else:
    print("Better luck next time!") 
print("Thank you for playing the Quiz game!")
 