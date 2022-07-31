
from random import randint
from IPython.display import clear_output

choices = ['rock', 'paper', 'scissors']

def rock_paper_scissors():

    while True:
        
        computer_response = choices[randint(0, 2)]
        player_response = input("Let's play rock paper scissors! Or, type 'I quit' to exit the game.\nWhat's your move?\n").lower()
        clear_output()

        if player_response == 'i quit':
            print("\nThank you for playing!")
            break

        elif player_response == computer_response:
            print(f"Game Tied! Computer also chose {computer_response}")

        elif player_response == 'rock':
            if computer_response == 'paper':
                print(f"You lose! Computer chose {computer_response}")
            else:
                print(f"You win! Computer chose {computer_response}")

        elif player_response == 'paper':
            if computer_response == 'scissors':
                print(f"You lose! Computer chose {computer_response}")
            else:
                print(f"You win! Computer chose {computer_response}")

        elif player_response == 'scissors':
            if computer_response == 'rock':
                print(f"You lose! Computer chose {computer_response}")
            else:
                print(f"You win! Computer chose {computer_response}")

        else:
            print("That doesn't seem to be an option. Try another input!")


rock_paper_scissors()