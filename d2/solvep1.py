with open('input.txt') as f:
    contents = f.readlines()

    hPos = 0
    dPos = 0

    for line in contents:
        move = line.split(' ')

        moveType = move[0]
        moveSize = int(move[1])

        if moveType == "forward":
            hPos += moveSize
        
        if moveType == "down":
            dPos += moveSize

        if moveType == "up":
            dPos -= moveSize

    print(hPos * dPos)
