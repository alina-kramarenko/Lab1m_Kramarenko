rounds = 3


def run(game):
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.game_name)
    
    for _ in range(rounds):
        question, answer = game.play()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer.isdigit() and int(user_answer) == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")