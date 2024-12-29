def get_questions(path):
    questions = []
    with open(path, "r") as file:
        lines = file.readlines()

    question = {}
    for line in lines:
        line = line.strip()
        if line.startswith("#Q"):
            if question:
                questions.append(question)
            question = {"question": line[2:].strip(), "options": {}, "answer": ""}
        elif line.startswith("^"):
            question["answer"] = line[1:].strip()
        elif line and question:
            option = line[0]
            text = line[2:]
            question["options"][option] = text

    if question:
        questions.append(question)

    return questions


def trivia(path):
    questions = get_questions(path)

    score = 0
    print("Welcome to the Trivia!")
    trivia_length = int(input("\nFirst things first, how many questions do you want to answer? ").strip())

    for i, q in enumerate(questions, 1):
        if i > trivia_length:
            break

        print(f"\nQuestion {i}: {q['question']}")
        for option, text in q["options"].items():
            print(f"    {option}. {text}")

        user_answer = input("Your answer: ").strip().upper()
        if user_answer == q["answer"].upper() or q["options"][user_answer] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz Complete! You scored {score} out of {trivia_length}.")


file_path = "sports.txt"
trivia(file_path)
