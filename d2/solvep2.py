with open('input.txt') as f:
    contents = f.readlines()

    hPos = 0
    dPos = 0
    aim = 0

    for line in contents:
        move = line.split(' ')

        moveType = move[0]
        moveSize = int(move[1])
        
        if moveType == "down":
            aim += moveSize

        if moveType == "up":
            aim -= moveSize

        if moveType == "forward":
            hPos += moveSize
            dPos += (aim * moveSize)

    print(hPos * dPos)
