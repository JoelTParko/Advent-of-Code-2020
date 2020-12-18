import re

def readFile(fileLocation):
    input = []
    fs = open(fileLocation)
    for line in fs:
        parsedLine= re.sub("[^0-9]","",line)
        input.append(int(parsedLine))
    return input

#Quicksort algorithm
def quicksort(inList):
    length = len(inList)
    #Handle Cases
    if(length > 2):
        midpoint = len(inList) // 2
        left = quicksort(inList[:midpoint])
        right = quicksort(inList[midpoint:])
    elif length == 1:
        return inList
    else:
        left = inList[0]
        right = inList[1]
        return [left,right] if left >= right else [right,left]
    pointerA = 0
    pointerB = 0
    outList = []
    #Sort left and right sides of list
    while True:
        if(left[pointerA] >= right[pointerB]):
            outList.append(left[pointerA])
            pointerA+=1
        else:
            outList.append(right[pointerB])
            pointerB+=1
        if(pointerA == len(left)):
            outList.extend(right[pointerB:])
            break
        elif(pointerB == len(right)):
            outList.extend(left[pointerA:])
            break
    return outList

#Recursive function to find pair that sums to 2020
#Uses pointers at either end of sorted list, moving the appropriate one depending on what the current sum is
def findSum2020(sortedList, rightPointer, leftPointer=0):
    leftNum = sortedList[leftPointer]
    rightNum = sortedList[rightPointer]
    sum = leftNum+rightNum
    if(sum==2020):
        return leftNum*rightNum
    elif(sum > 2020):
        return findSum2020(sortedList,rightPointer,leftPointer+1)
    else:
        return findSum2020(sortedList, rightPointer-1, leftPointer)

#Part 1

input = readFile("./inputs/day1.txt")
sortedInput = quicksort(input)
print(sortedInput)
output = findSum2020(sortedInput, len(sortedInput)-1)
print(output)

