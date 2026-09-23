board = [ ["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"] ]
 
print(board[0])
print(board[1])
print(board[2])

#X first move
col = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
col -= 1
row -= 1

board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])

for counter in range(1,5): #NEW CODE: loops for X and O players
    #O move
    col = int(input("O player, select a column 1-3: "))
    row = int(input("O player, select a row 1-3: "))
    col -= 1
    row -= 1
 
    if board[row][col] == '-':
      board[row][col] = "O"
    else:
      print("Oops, that spot was already taken. ")
    print(board[0])
    print(board[1])
    print(board[2])
 
    #X move
    col = int(input("X player, select a column 1-3: "))
    row = int(input("X player, select a row 1-3: "))
    col -= 1
    row -= 1
 
    if board[row][col] == '-':
      board[row][col] = "X"
    else:
      print("Oops, that spot was already taken. ")
    print(board[0])
    print(board[1])
    print(board[2])



