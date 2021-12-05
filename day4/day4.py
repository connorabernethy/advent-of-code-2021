f = open("input.txt")

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

            index +=1
    index = 0
    count = 0
    total = 0
    print(boards)
