#Read and format data from input file
def readFile(location):
    input = []
    file = open(location)
    for line in file:
        line = line.replace('\n', '')
        chars = []
        for char in line:
            chars.append(char)
        input.append(chars)
    return input

#Toboggan function moves the character by a specified number of units in the x and y directions
#The function returns the number of 'tree' tiles encountered 
def Toboggan(map, deltaX, deltaY):
    treeCount = 0
    count = 0
    x = 0
    y = 0
    while(y<len(map)):
        count+=1
        if(map[y][x]=='#'):
            treeCount+=1
        x=x+deltaX
        y=y+deltaY
        if(x>=len(map[0])):
            x= x-len(map[0])
    return treeCount

#Part 1

input = readFile("./inputs/day3.txt")
print(input)
output1 = Toboggan(input, 3, 1)
print(output1)

#Part 2
#Generalised inital function used in part 1 so that any change in x and y can be easily calculated
output2 = Toboggan(input, 1, 1) * Toboggan(input, 3,1 ) * Toboggan(input, 5, 1) * Toboggan(input, 7, 1) *  Toboggan(input, 1, 2)
print(output2)
