with open('inputp2.txt') as f:
    contents = f.readlines()
    prevSet = None
    currSet = None
    start = 0
    stop = len(contents)
    offset = 2
    numOfIncMeasures = 0

    for i in range(len(contents)):

        currSet = contents[i : i+offset+1]

        if prevSet is not None:
            prevSetInt = list(map(int, prevSet))
            currSetInt = list(map(int, currSet))
    
            if sum(currSetInt) - sum(prevSetInt) > 0:
                numOfIncMeasures += 1

        prevSet = currSet

    print(numOfIncMeasures)



