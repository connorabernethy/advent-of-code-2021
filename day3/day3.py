# Connor Abernethy
# Advent of Code 2021
# 12/03/2021

def part_one():
    f = open("input.txt")

    list = f.readlines()

    count = 0
    index = 0
    gammaRate = ""

    while index < len(list[0]) - 1:
        for num in list:
            if num[index] == "1":
                count += 1
            else:
                count -= 1
        if count > 0:
            gammaRate += "1"
        else:
            gammaRate += "0"
        count = 0
        index += 1

    print("Gamma rate: " + gammaRate)
    epsilonRate = ""

    for char in gammaRate:
        if char == "1":
            epsilonRate += "0"
        else:
            epsilonRate += "1"

    print("Epsilon rate: " + epsilonRate)

    # Strings converted to decimal values and multiplied together:
    print(199 * 3896)

def part_two():
    f = open("input.txt")

    list = f.readlines()
    newList = list

    count = 0
    index = 0
    oxygenRating = ""

    while index < len(list[0]) - 1:
        for num in newList:
            if num[index] == "1":
                count += 1
            else:
                count -= 1
        if count > 0 or count == 0:
            newList = [num1 for num1 in newList if num1[index] != "0"]
        elif count < 0:
            newList = [num1 for num1 in newList if num1[index] != "1"]

        count = 0
        index += 1

    oxygenRating = newList[0]
    newList = list
    co2Rating = ""
    index = 0

    while index < len(list[0]) - 1:
        for num in newList:
            if num[index] == "1":
                count += 1
            else:
                count -= 1
        if count > 0 or count == 0:
            newList = [num1 for num1 in newList if num1[index] != "1"]
        elif count < 0:
            newList = [num1 for num1 in newList if num1[index] != "0"]
        
        if len(newList) == 1:
            co2Rating = newList[0]

        count = 0
        index += 1

    print("Oxygen rating: " + oxygenRating)
    print("CO2 rating: " + co2Rating)
    # Binary ratings converted to decimal then multiplied
    print("Answer: ", end="")
    print((509*2693))

part_one()
part_two()
