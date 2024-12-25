game_on = True
row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]
available = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def printboard():
    print(row_1)
    print(row_2)
    print(row_3)

print("Welcome to Tic Tac Toe!")
player1name = input("Who is player 1? ")
player2name = input("Who is player 2? ")
print(f"{player1name} will go first and play as X.")

def checkwin():
    global game_on
    if (
        row_1 == ["X", "X", "X"] or row_2 == ["X", "X", "X"] or row_3 == ["X", "X", "X"] or 
        (row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X") or 
        (row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X") or 
        (row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X") or 
        (row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X") or 
        (row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X")
    ):
        print(f"{player1name} wins!")
        game_on = False
    elif (
        row_1 == ["O", "O", "O"] or row_2 == ["O", "O", "O"] or row_3 == ["O", "O", "O"] or 
        (row_1[0] == "O" and row_2[0] == "O" and row_3[0] == "O") or 
        (row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O") or 
        (row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O") or 
        (row_1[0] == "O" and row_2[1] == "O" and row_3[2] == "O") or 
        (row_1[2] == "O" and row_2[1] == "O" and row_3[0] == "O")
    ):
        print(f"{player2name} wins!")
        game_on = False

def askplayer1():
    printboard()
    player1 = input(f"{player1name}, choose a number 1-9: ")
    while player1 not in available:
        print("That space is already taken. Try again.")
        player1 = input(f"{player1name}, choose a number 1-9: ")
    if player1 == "1":
        row_1[0] = "X"
    elif player1 == "2":
        row_1[1] = "X"
    elif player1 == "3":
        row_1[2] = "X"
    elif player1 == "4":
        row_2[0] = "X"
    elif player1 == "5":
        row_2[1] = "X"
    elif player1 == "6":
        row_2[2] = "X"
    elif player1 == "7":
        row_3[0] = "X"
    elif player1 == "8":
        row_3[1] = "X"
    elif player1 == "9":
        row_3[2] = "X"
    available.remove(player1)
    checkwin()

def askplayer2():
    printboard()
    player2 = input(f"{player2name}, choose a number 1-9: ")
    while player2 not in available:
        print("That space is already taken. Try again.")
        player2 = input(f"{player2name}, choose a number 1-9: ")
    if player2 == "1":
        row_1[0] = "O"
    elif player2 == "2":
        row_1[1] = "O"
    elif player2 == "3":
        row_1[2] = "O"
    elif player2 == "4":
        row_2[0] = "O"
    elif player2 == "5":
        row_2[1] = "O"
    elif player2 == "6":
        row_2[2] = "O"
    elif player2 == "7":
        row_3[0] = "O"
    elif player2 == "8":
        row_3[1] = "O"
    elif player2 == "9":
        row_3[2] = "O"
    available.remove(player2)
    checkwin()

while game_on:
    askplayer1()
    if not game_on:
        break
    askplayer2()