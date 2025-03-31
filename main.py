from engine import run
from games import NOK, Progression


def main():

    print("Welcome to the Brain Games!")
    print("Choose a game to play:")
    print("1. Find the smallest common multiple of given numbers.")
    print("2. What number is missing in the progression?")
    
    choice = input("Enter the number of the game you want to play (1 or 2): ")
    
    if choice == "1":
        run(NOK)
    elif choice == "2":
        run(Progression)
    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()