# Day 2: I Was Told There Would Be No Math

import re

def presentSurface(length, width, height):
    return 2*(length * width) + 2*(width * height) + 2*(length*height)

def countSurfaceSmallestSide(length, width, height):
    listMeasures = [length, width, height]
    minValue = min(listMeasures)
    listMeasures.remove(minValue)
    secondMinValue = min(listMeasures)
    return minValue * secondMinValue

def parseNumbersFromFile(fileName):
    inputData = open(fileName, 'r').read()
    measurments = re.findall(r"[\d]+", inputData)
    return measurments

def feetOfRibbonForWrap(length, width, height):
    listMeasures = [length, width, height]
    minValue = min(listMeasures)
    listMeasures.remove(minValue)
    secondMinValue = min(listMeasures)
    return (2 * minValue) + (2 * secondMinValue)

def feetOfRibbonForBow(length, width, height):
    return length * width * height

def getSquareFeetOfWrappingPaper(fileName):
    measurments = parseNumbersFromFile(fileName)

    setOfMeasurment = []
    totalSurface = 0

    for character in measurments:
        setOfMeasurment.append(character)
        if(len(setOfMeasurment) == 3):
            l = int(setOfMeasurment[0])
            w = int(setOfMeasurment[1])
            h = int(setOfMeasurment[2])
            totalSurface += (presentSurface(l, w, h) + countSurfaceSmallestSide(l, w, h))
            setOfMeasurment.clear()

    return totalSurface
    
def getTotalFeetOfRibbon(fileName):
    measurments = parseNumbersFromFile(fileName) 

    setOfMeasurment = []
    totalFeetOfRibbon = 0

    for character in measurments:
        setOfMeasurment.append(character)
        if(len(setOfMeasurment) == 3):
            l = int(setOfMeasurment[0])
            w = int(setOfMeasurment[1])
            h = int(setOfMeasurment[2])
            totalFeetOfRibbon += (feetOfRibbonForWrap(l, w, h) + feetOfRibbonForBow(l, w, h))
            setOfMeasurment.clear()
    
    return totalFeetOfRibbon

print(getSquareFeetOfWrappingPaper('input.txt'))
print(getTotalFeetOfRibbon('input.txt'))

