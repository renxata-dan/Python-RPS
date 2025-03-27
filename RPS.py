import random

# Print game rules
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # TODO: Get and convert user input
    # HINT: Use input() to read from the user and wrap it with int()
    choice = ___

    # TODO: Keep asking until the input is valid (between 1 and 3)
    # HINT: Use a while loop to check if choice is not in the valid range
    while ___:
        choice = ___

    # TODO: Map the user’s choice to its name
    # HINT: Use if-elif-else to assign choice_name based on choice number
    if choice == ___:
        choice_name = '___'  # HINT: This should be "Rock"
    elif ___:
        choice_name = '___'  # HINT: This should be "Paper"
    else:
        choice_name = '___'  # HINT: This should be "Scissors"

    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    # TODO: Computer makes a random choice
    # HINT: Use random.randint() with range 1 to 3
    comp_choice = ___

    # TODO: Map computer's choice to its name
    if ___:
        comp_choice_name = '___'
    elif ___:
        comp_choice_name = '___'
    else:
        comp_choice_name = '___'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # TODO: Determine the winner
    # HINT: First handle tie, then combinations where Paper, Rock, or Scissors win
    if ___:
        result = "DRAW"
    elif (choice == ___ and comp_choice == ___) or (choice == ___ and comp_choice == ___):
        result = '___'  # HINT: Paper wins in this case
    elif (___ and ___) or (___ and ___):
        result = '___'  # HINT: Rock wins in this case
    elif (___ and ___) or (___ and ___):
        result = '___'  # HINT: Scissors wins in this case

    # TODO: Print game result
    # HINT: Compare result with "DRAW" and with user choice_name
    if ___:
        print("<== It's a tie! ==>")
    elif ___:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # TODO: Ask to play again
    # HINT: Use input() and convert to lowercase
    print("Do you want to play again? (Y/N)")
    ans = ___.___()
    if ans == 'n':
        break

print("Thanks for playing!")
