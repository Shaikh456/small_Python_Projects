# 🎮 Simple Quiz Game in Python

def quiz_game():
    """
    A simple command-line quiz game.
    Player answers multiple-choice questions, and score is calculated at the end.
    """

    # List of quiz questions with options and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the backbone of web development?",
            "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
            "answer": "B"
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Galileo Galilei"],
            "answer": "C"
        },
        {
            "question": "Which data structure uses FIFO (First In, First Out)?",
            "options": ["A) Stack", "B) Queue", "C) Tree", "D) Graph"],
            "answer": "B"
        },
    ]

    score = 0  # Keep track of score
    total_questions = len(questions)  # Count total number of questions

    print("🎉 Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Type A, B, C, or D to answer.\n")

    # Loop through each question in the quiz
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")  # Print question
        for option in q["options"]:      # Print all options
            print(option)

        # Get user input and convert it to uppercase (so input is not case-sensitive)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if the answer is correct
        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    # Display final score
    print("📊 Quiz Completed!")
    print(f"Your Score: {score}/{total_questions}")

    # Feedback based on performance
    if score == total_questions:
        print("🏆 Excellent! Perfect score!")
    elif score >= total_questions // 2:
        print("👍 Good job! You passed.")
    else:
        print("😢 Better luck next time.")


# Run the game
if __name__ == "__main__":
    quiz_game()
