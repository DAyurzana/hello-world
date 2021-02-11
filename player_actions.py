#player_actions.py
#Duke A.
#02/11/2021


def check_play_again(user_input):
    if user_input == "y":
        print("Yes, play again")
    elif user_input == "n":
        print("No, quit the game")
    else:
        print("invalid input")


check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
