from random import randint
def guessing_game():
    while True:
        numbers = randint(20, 40)
        question = input("Chose a number from 20 - 40: ")
        # if question >= '15':
        #     print("invalid number, choose a number between 1-15")
        #     continue
        if question == numbers:
            print("congrats you won!!!")
        else:
            print("sorry you lost!")
            print(f"The correct number is {numbers}")
        keep_playing = input("Would you like to play again? (yes/no): ")
        if keep_playing.lower() == 'yes':
            continue
        elif keep_playing.lower() == 'no':
            print("Thanks for playing!!!")
        else:
            print("Enter a valid input!")
            break
guessing_game()