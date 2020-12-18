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
output = Toboggan(input, 3, 1)
print(output)
