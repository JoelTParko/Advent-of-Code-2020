import re

#Read and format data from input file
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
output1 = findSum2020(sortedInput, len(sortedInput)-1)
print("The answer to part 1 is: "+str(output1))

#Part 2
#Similar to part 1, put two pointers at extremes of the sorted list and slowly move towards each other
#A third extra pointer (rightPointer) is held beyond the pointer at the low end of the list (centerPointer)
#If the low pointer and the third pointer ever sum above 2020, then the low pointer has moved two far up
#The algorithm is reset, with the extra pointer now sitting one poistion higher up than previously
def find3Sum2020(sortedList, rightPointer, centerPointer, leftPointer=0):
    leftNum = sortedInput[leftPointer]
    centerNum = sortedInput[centerPointer]
    rightNum = sortedInput[rightPointer]
    sum1 = centerNum + rightNum
    #Check low pointer and extra pointer sum below 2020
    if(sum1 >= 2020):
        rightPointer-=1
        centerPointer = rightPointer-1
        return find3Sum2020(sortedList, rightPointer, centerPointer)
    #Perform same algorithm as in previous answer
    else:
        sum = sum1+leftNum
        if(sum==2020):
            return leftNum*centerNum*rightNum
        elif(sum>2020):
            return find3Sum2020(sortedList, rightPointer, centerPointer, leftPointer+1)
        else:
            return find3Sum2020(sortedList, rightPointer, centerPointer-1, leftPointer)

output2 = find3Sum2020(sortedInput, len(sortedInput)-1, len(sortedInput)-2)
print("The answer to part 2 is: " + str(output2))