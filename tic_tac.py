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

#O first move
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

#X second move
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

#O second move
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

#X third move
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

#0 third move
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

#X fourth move
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

#O fourth move
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

#X fifth move
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