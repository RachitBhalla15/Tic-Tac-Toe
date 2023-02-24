def brdgame(brd):
    """
    Print the current state of the game brd.
    """
    print("-------------")
    for row_idx in brd:
        print("|", end=" ")
        for cell_idx in row_idx:
            print(cell_idx, end=" | ")
        print("\n-------------")

def chk_win(brd, Plyr):
    """
    Check if the specified Plyr has won the game.
    """
    # Check row_idxs
    for row_idx in brd:
        if all(cell_idx == Plyr for cell_idx in row_idx):
            return True
    # Check columns
    for i in range(3):
        if all(brd[j][i] == Plyr for j in range(3)):
            return True
    # Check diagonals
    if all(brd[i][i] == Plyr for i in range(3)):
        return True
    if all(brd[i][2-i] == Plyr for i in range(3)):
        return True
    # No win
    return False

def game_run():
    """
    Play a game of XO.
    """
    brd = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    Plyrs = ["X", "O"]
    Current_Player = Plyrs[0]
    while True:
        brdgame(brd)
        move = input(f"Plyr {Current_Player}, enter your move (row,column): ")
        row_idx, col = map(int, move.split(","))
        if brd[row_idx][col] != " ":
            print("That cell is already taken. Try again.")
            continue
        brd[row_idx][col] = Current_Player
        if chk_win(brd, Current_Player):
            brdgame(brd)
            print(f"Player {Current_Player} wins!")
            break
        if all(brd[i][j] != " " for i in range(3) 
                    for j in range(3)):
            brdgame(brd)
            print("It's a tie!")
            break
        Current_Player = Plyrs[1] if Current_Player == Plyrs[0] else Plyrs[0]

if __name__ == "__main__":
    game_run()
