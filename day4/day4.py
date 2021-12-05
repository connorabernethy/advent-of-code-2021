def check_board(board):
    total = 0
    for num in board:
        if num[1] == False:
            total += num[0]
    return total


f = open("input.txt")
total = 0
list = f.readlines()

print(len(list))


# Parse input numbers:

inputs = str.split(list[0], ",")

# Convert inputs to integer representations

inputList = []

for num in inputs:
    inputList.append(int(num))

flag = False
index = 0
i = 2
j = i + 5
board1 = []
boards = []
while j < len(list) + 5:
    board1 = []
    #print(i, end="---")
    #print(j,end="")
    for num1 in list[i:j]:
        index = 0
        num1 = str.split(num1)
        while index < len(num1):
            if int(num1[index]) in inputList:
                flag = False
                board1.append([int(num1[index]), flag])
            else:
                flag = False
                board1.append([int(num1[index]), flag])
            index += 1
    i = j+1
    j = i+5
    boards.append(board1)

index = 0
# print(boards)
print(len(boards))
print(boards[0])
print(len(boards[0]))

# boards is a list of lists of dictionaries, with each list of size 25 dicts.

for number in inputList:
    for board in boards:
        index = 0
        #print(len(board))
        while (index < len(board)):
            if board[index][0] == number:
                board[index][1] = True
                if board[0][1] == True and board[1][1] == True and board[2][1] == True and board[3][1] == True and board[4][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[5][1] == True and board[6][1] == True and board[7][1] == True and board[8][1] == True and board[9][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[10][1] == True and board[11][1] == True and board[12][1] == True and board[13][1] == True and board[14][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[15][1] == True and board[16][1] == True and board[17][1] == True and board[18][1] == True and board[19][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[20][1] == True and board[21][1] == True and board[22][1] == True and board[23][1] == True and board[24][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[0][1] == True and board[5][1] == True and board[10][1] == True and board[15][1] == True and board[20][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[1][1] == True and board[6][1] == True and board[11][1] == True and board[16][1] == True and board[21][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[2][1] == True and board[7][1] == True and board[12][1] == True and board[17][1] == True and board[22][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[3][1] == True and board[8][1] == True and board[13][1] == True and board[18][1] == True and board[23][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)
                elif board[4][1] == True and board[9][1] == True and board[14][1] == True and board[19][1] == True and board[24][1] == True:
                    win = board[index][0]
                    total = check_board(board)
                    print(total * win)

            index +=1
    index = 0
    count = 0
