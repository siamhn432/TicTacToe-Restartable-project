
def printBoard(gameValues):
    # Print the Tic Tac Toe board
    print(f" {gameValues[0]} | {gameValues[1]} | {gameValues[2]} ")
    print(f"---|---|---")
    print(f" {gameValues[3]} | {gameValues[4]} | {gameValues[5]} ")
    print(f"---|---|---")
    print(f" {gameValues[6]} | {gameValues[7]} | {gameValues[8]} ")


def checkWin(gameValues):
    # All Winning Patterns
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        # Check if X wins
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X':
            printBoard(gameValues)
            print("X Won the match!")
            return 1
        # Check if O wins
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O':
            printBoard(gameValues)
            print("O Won the match!")
            return 0

    # Check if the board is full
    if all(isinstance(item, str) for item in gameValues):
        printBoard(gameValues)
        return -2
    
    return -1  # No winner yet


def play_game():
    print("Welcome to our simple TicTacToe Game!")
    gameValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1  # 1 for X, 0 for O

    while True:
        try:
            if chance == 1:
                printBoard(gameValues)
                print("\nX's Turn")
                value = int(input("Please enter a value (0-8): "))

                # Check if the position is available
                if gameValues[value] != 'O' and gameValues[value] != 'X':
                    gameValues[value] = 'X'
                else:
                    print("\nPosition already taken! Please choose a different location for X.")
                    continue

            else:
                printBoard(gameValues)
                print("\nO's Turn")
                value = int(input("Please enter a value (0-8): "))

                # Check if the position is available
                if gameValues[value] != 'X' and gameValues[value] != 'O':
                    gameValues[value] = 'O'
                else:
                    print("\nPosition already taken! Please choose a different location for O.")
                    continue

        except (IndexError, ValueError):
            # Exception if input is invalid
            print("\nInvalid input! Please enter a value from 0 to 8.\n")
            continue

        # Switch player turn
        chance = 1 - chance
        result = checkWin(gameValues)

        # Check game result
        if result == -2:
            print("Game Draw!")
            break
        if result != -1:
            print("Match Over!")
            break

# Main program with restart option
if __name__ == '__main__':
    while True:
        play_game()
        restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thank you for playing! Goodbye!")
            break
