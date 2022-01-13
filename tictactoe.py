'''
Wk 2 - Tic-Tac-Toe
Author: Monika Meyers
'''


def main():
    again = 'Y'
    player = next_move("")
    grid = create_grid()
    while again == 'Y':
        again = game_play(grid, player)
        if again == 'Y':
                grid = create_grid()

#Function to play game.
def game_play(grid, player):
    while not (winning_move(grid) or tie_game(grid)):
        draw_grid(grid)
        players_choice(player, grid)
        player = next_move(player)
    draw_grid(grid)
    print("Good game. Thanks for playing!")
    again = input("Do you want to play again? (Y/N): ")

    print() 
    return again

#Function to create the list of numbers for each box that the player uses to choose.
def create_grid():
    grid = []
    for box in range(9):
        grid.append(box + 1)
    return grid

#Function to draw grid of choices
def draw_grid(grid):
    print()
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print('-+-+-')
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print('-+-+-')
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print()

# Function if the game it a tie.    
def tie_game(grid):
    for box in range(9):
        if grid[box] != "x" and grid[box] != "o":
            return False
    return True 

#Function to determine if there is a winner.    
def winning_move(grid):
    if (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6]):
        return True

#Function to get Player's choice on the grid.
def players_choice(player, grid):
    box = int(input(f"{player}'s turn to choose a square (1-9): "))
    grid[box - 1] = player

#Function to determine which player is next.
def next_move(current_player):
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"

if __name__ == "__main__":
    main()