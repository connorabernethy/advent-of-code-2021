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

part_one()
