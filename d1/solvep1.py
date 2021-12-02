with open('inputp1.txt') as f:
    contents = f.readlines()
    prevMeasure = None
    numOfIncMeasures = 0
    for measure in contents:
        if prevMeasure != None:
            if int(measure) - int(prevMeasure) > 0:
                numOfIncMeasures += 1
        prevMeasure = measure

    print(numOfIncMeasures)

