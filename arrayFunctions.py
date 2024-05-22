global  findRowWithMMsClosestTo0, findRowWithField0

def findRowWithMMsClosestTo0(targetArray):

    #this merely declares the closest reading known to the first row and second column of the current array, which is the first M/Ms reading. it enables the rest of the code as is to work -ABQ
    closestReading = targetArray[0][1]

    #this will turn into a tracker inside the loop so we know which row has the minimun M/Ms reading -ABQ
    closestRow = None

    minKnownDifferenceTo0 = abs(closestReading)
    for i, row in enumerate(targetArray):
        currentDifferenceTo0 = abs(row[1])
        if currentDifferenceTo0 < minKnownDifferenceTo0:
            minKnownDifferenceTo0 = currentDifferenceTo0
            closestRow = int(i)
    return targetArray[closestRow]

#this function assumes that there is a column zero and it's the column with the field readings -ABQ
def findRowWithField0(targetArray):
    closestReading = targetArray[0][0]
    closestRow = None
    minKnownDifferenceTo0 = abs(closestReading)
    for i, row in enumerate(targetArray):
        currentDifferenceTo0 = abs(row[0])
        if currentDifferenceTo0 < minKnownDifferenceTo0:
            minKnownDifferenceTo0 = currentDifferenceTo0
            closestRow = int(i)
    return targetArray[closestRow]